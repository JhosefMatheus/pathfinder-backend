import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { Pathfinder, Prisma, Requirement, RequirementPathfinder, User } from "@prisma/client";
import { ICrudPathfinder, IGetPathfinderClassesProgressData } from "./interface";

@Injectable()
export class PathfinderService {
    constructor(private readonly prismaService: PrismaService) {}

    async getPathfinders(userId: string): Promise<Pathfinder[]> {
        const pathfinders: Pathfinder[] = await this.prismaService.pathfinder.findMany({
            where: {
                userId: {
                    equals: parseInt(userId)
                }
            }
        });

        return pathfinders;
    }

    async createPathfinder(userId: string, pathfinderName: string): Promise<ICrudPathfinder> {
        try {
            const user: User = await this.prismaService.user.findFirstOrThrow({
                where: {
                    id: {
                        equals: parseInt(userId)
                    }
                }
            });

            await this.prismaService.pathfinder.create({
                data: {
                    name: pathfinderName,
                    userId: user.id
                }
            });

            return {
                flag: true,
                message: "Desbravador cadastrado com sucesso."
            }
        } catch (error) {
            if (error instanceof Prisma.NotFoundError) {
                return {
                    flag: false,
                    message: "Usuário inexistente."
                }
            }
        }
    }

    async deletePathfinder(userId: string, pathfinderId: string): Promise<ICrudPathfinder> {
        let user: User;
        
        try {
            user = await this.prismaService.user.findFirstOrThrow({
                where: {
                    id: {
                        equals: parseInt(userId)
                    }
                }
            });
        } catch (error) {
            if (error instanceof Prisma.NotFoundError) {
                return {
                    flag: false,
                    message: "Usuário inexistente."
                }
            }
        }

        try {
            await this.prismaService.requirementPathfinder.deleteMany({
                where: {
                    pathfinderId: parseInt(pathfinderId)
                }
            });
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Desbravador inexistente."
                    }
                }
            }
        }

        try {
            await this.prismaService.pathfinder.delete({
                where: {
                    id: parseInt(pathfinderId)
                }
            });

            return {
                flag: true,
                message: "Desbravador deletado com sucesso."
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Desbravador inexistente."
                    }
                }
            }
        }
    }

    async editPathfinder(userId: string, pathfinderId: string, pathfinderName: string): Promise<ICrudPathfinder> {
        let user: User;

        try {
            user = await this.prismaService.user.findFirstOrThrow({
                where: {
                    id: {
                        equals: parseInt(userId)
                    }
                }
            });
        } catch (error) {
            if (error instanceof Prisma.NotFoundError) {
                return {
                    flag: false,
                    message: "Usuário inexistente."
                }
            }
        }

        try {
            await this.prismaService.pathfinder.update({
                data: {
                    name: pathfinderName
                },
                where: {
                    id: parseInt(pathfinderId)
                }
            });

            return {
                flag: true,
                message: "Desbravador atualizado com sucesso."
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Desbravador inexistente."
                    }
                }
            }
        }
    }

    async getPathfinder(userId: string, pathfinderId: string): Promise<ICrudPathfinder> {
        let user: User, pathfinder: Pathfinder;

        try {
            user = await this.prismaService.user.findFirstOrThrow({
                where: {
                    id: {
                        equals: parseInt(userId)
                    }
                }
            });
        } catch (error) {
            if (error instanceof Prisma.NotFoundError) {
                return {
                    flag: false,
                    message: "Usuário inexistente."
                }
            }
        }

        try {
            pathfinder = await this.prismaService.pathfinder.findFirstOrThrow({
                where: {
                    AND: {
                        id: {
                            equals: parseInt(pathfinderId)
                        },
                        userId: {
                            equals: user.id
                        }
                    }
                }
            });
            
            return {
                flag: true,
                message: "Desbravador encontrado com sucesso.",
                pathfinder
            }
        } catch(error) {
            if (error instanceof Prisma.NotFoundError) {
                return {
                    flag: false,
                    message: "Desbravador inexistente."
                }
            }
        }
    }

    private async getPathfinderClassProgress(pathfinderId: string, classId: number): Promise<number> {
        const classRequirements: Requirement[] = await this.prismaService.requirement.findMany({
            where: {
                classId: {
                    equals: classId
                }
            }
        });

        const pathfinderClassRequirements: RequirementPathfinder[] = await this.prismaService.requirementPathfinder.findMany({
            where: {
                AND: {
                    pathfinderId: parseInt(pathfinderId),
                    requirement: {
                        classId: {
                            equals: classId
                        }
                    }
                }
            }
        });

        return Math.floor((pathfinderClassRequirements.length/classRequirements.length)*100);
    }

    async getPathfinderClassesProgress(pathfinderId: string): Promise<IGetPathfinderClassesProgressData> {
        const friendProgress = await this.getPathfinderClassProgress(pathfinderId, 1);
        const companionProgress = await this.getPathfinderClassProgress(pathfinderId, 2);
        const researcherProgress = await this.getPathfinderClassProgress(pathfinderId, 3);
        const pioneerProgress = await this.getPathfinderClassProgress(pathfinderId, 4);
        const hikerProgress = await this.getPathfinderClassProgress(pathfinderId, 5);
        const guideProgress = await this.getPathfinderClassProgress(pathfinderId, 6);

        return {
            friendProgress,
            companionProgress,
            researcherProgress,
            pioneerProgress,
            hikerProgress,
            guideProgress
        }
    }
}