import { Injectable } from "@nestjs/common";
import { Prisma, RequirementPathfinder } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
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
}