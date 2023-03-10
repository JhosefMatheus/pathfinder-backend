import { Injectable } from "@nestjs/common";
import { Class, Prisma, Requirement, RequirementGroup, Subrequirement } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
import { IGetClassData, IGetRequirementsData, IGetSubRequirementsData } from "./interface";

@Injectable()
export class ClassService {
    constructor(private readonly prismaService: PrismaService) {}

    async getClasses(): Promise<Class[]> {
        const classes: Class[] = await this.prismaService.class.findMany({
            orderBy: {
                id: "asc"
            }
        });

        return classes;
    }

    async getClassData(classId: string): Promise<IGetClassData> {
        try {
            const selectedClass = await this.prismaService.class.findFirstOrThrow({
                where: {
                    id: {
                        equals: parseInt(classId)
                    }
                }
            });

            return {
                flag: true,
                message: "Classe encontrada com sucesso.",
                selectedClass
            }
        } catch (error) {
            if (error instanceof Prisma.NotFoundError) {
                return {
                    flag: false,
                    message: "Classe inexistente."
                }
            }
        }
    }
    
    async getRequirementGroups(): Promise<RequirementGroup[]> {
        const requirementGroups: RequirementGroup[] = await this.prismaService.requirementGroup.findMany();

        return requirementGroups;
    }

    async getRequirements(classId: string, requirementGroupId: string): Promise<IGetRequirementsData> {
        try {
            const requirements: Requirement[] = await this.prismaService.requirement.findMany({
                where: {
                    AND: {
                        classId: {
                            equals: parseInt(classId)
                        },
                        requirementGroupId: {
                            equals: parseInt(requirementGroupId)
                        }
                    }
                }
            });

            return {
                flag: true,
                message: "Requisitos encontrados.",
                requirements
            }
        } catch (error) {
            console.log(error);

            return {
                flag: false,
                message: "Requisitos n??o encontrados."
            }
        }
    }

    async getSubRequirements(requirementId: string): Promise<IGetSubRequirementsData> {
        try {
            const subRequirements: Subrequirement[] = await this.prismaService.subrequirement.findMany({
                where: {
                    requirementId: {
                        equals: parseInt(requirementId)
                    }
                }
            });

            return {
                flag: true,
                message: "Sub-requisitos encontrado.",
                subRequirements
            }
        } catch(error) {
            console.log(error);

            return {
                flag: false,
                message: "Sub-requisitos n??o encontrados."
            }
        }
    }
}