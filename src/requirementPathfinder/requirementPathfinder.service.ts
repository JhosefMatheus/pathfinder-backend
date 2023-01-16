import { Injectable } from "@nestjs/common";
import { Prisma, RequirementPathfinder } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
import { RequirementPathfinderDto } from "./dto";
import { IGetRequirementsPathfinder } from "./interface";

@Injectable()
export class RequirementPathfinderService {
    constructor(private readonly prismaService: PrismaService) {}

    async getRequirementsPathfinder(pathfinderId: string, requirementId: string): Promise<IGetRequirementsPathfinder> {
        try {
            const requirementPathfinder: RequirementPathfinder = await this.prismaService.requirementPathfinder.findFirstOrThrow({
                where: {
                    AND: {
                        pathfinderId: {
                            equals: parseInt(pathfinderId)
                        },
                        requirementId: {
                            equals: parseInt(requirementId)
                        }
                    }
                }
            });

            return {
                flag: true,
                message: "Requisito do desbravador encontrado com sucesso.",
                requirementPathfinder
            }
        } catch (error) {
            if (error instanceof Prisma.NotFoundError) {
                return {
                    flag: false,
                    message: "Requisito não encontrado. Possíveis casos: Desbravador inexistente, requisito inexistente ou o desbravador ainda não cumpriu esse requisito."
                }
            }
        }
    }

    private addRequirementsPathfinder(addedRequirementsPathfinder: RequirementPathfinderDto[]): void {
        addedRequirementsPathfinder.forEach(async (e) => {
            const { id, pathfinderId, requirementId } = e;

            const pathfinderVerify = await this.prismaService.pathfinder.findFirst({
                where: {
                    id: {
                        equals: parseInt(pathfinderId)
                    }
                }
            });

            const requirementVerify = await this.prismaService.requirement.findFirst({
                where: {
                    id: {
                        equals: requirementId
                    }
                }
            });

            if (!id && pathfinderVerify && requirementVerify) {
                await this.prismaService.requirementPathfinder.create({
                    data: {
                        pathfinderId: parseInt(pathfinderId),
                        requirementId: requirementId
                    }
                });
            }
        });
    }

    private deleteRequirementsPathfinder(deletedRequirementsPathfinder: RequirementPathfinderDto[]): void {
        deletedRequirementsPathfinder.forEach(async (e) => {
            const { id, pathfinderId, requirementId } = e;

            const pathfinderVerify = await this.prismaService.pathfinder.findFirst({
                where: {
                    id: {
                        equals: parseInt(pathfinderId)
                    }
                }
            });

            const requirementVerify = await this.prismaService.requirement.findFirst({
                where: {
                    id: {
                        equals: requirementId
                    }
                }
            });

            if (id && pathfinderVerify && requirementVerify) {
                await this.prismaService.requirementPathfinder.delete({
                    where: {
                        id: id
                    }
                });
            }
        });
    }

    saveRequirementsPathfinder(addedRequirementsPathfinder: RequirementPathfinderDto[], deletedRequirementsPathfinder: RequirementPathfinderDto[]): void {
        this.addRequirementsPathfinder(addedRequirementsPathfinder);
        this.deleteRequirementsPathfinder(deletedRequirementsPathfinder);
    }
}