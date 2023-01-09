import { Controller, Res, UseGuards, Get, Param } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { RequirementGroup } from "@prisma/client";
import { Response } from "express";
import { ClassService } from "./class.service";
import { IGetClassDataParams, IGetRequirementsParams, IGetSubRequirementParams } from "./interface";

@UseGuards(AuthGuard("jwt"))
@Controller("class")
export class ClassController {
    constructor(private readonly classService: ClassService) {}

    @Get("/classes")
    async getClasses(@Res() response: Response): Promise<Response> {
        const classes = await this.classService.getClasses();

        return response.status(200).json({
            classes
        });
    }

    @Get("/classes/requirementGroups")
    async getRequirementGrouops(@Res() response: Response): Promise<Response> {
        const requirementGroups: RequirementGroup[] = await this.classService.getRequirementGroups();
        
        return response.status(200).json({
            requirementGroups
        });
    }

    @Get("/classes/requirements/:classId/:requirementGroupId/")
    async getRequirements(@Res() response: Response, @Param() params: IGetRequirementsParams): Promise<Response> {
        const { classId, requirementGroupId } = params;

        const { flag, message, requirements } = await this.classService.getRequirements(classId, requirementGroupId);

        if (flag) {
            return response.status(200).json({
                message,
                requirements
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Get("/classes/subRequirements/:requirementId")
    async getSubRequirements(@Res() response: Response, @Param() params: IGetSubRequirementParams): Promise<Response> {
        const { requirementId } = params;

        const { flag, message, subRequirements } = await this.classService.getSubRequirements(requirementId);

        if (flag) {
            return response.status(200).json({
                message,
                subRequirements
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Get("/:classId")
    async getClassData(@Res() response: Response, @Param() params: IGetClassDataParams): Promise<Response> {
        const { classId } = params;

        const { flag, message, selectedClass } = await this.classService.getClassData(classId);

        if (flag) {
            return response.status(200).json({
                message,
                selectedClass
            });
        }

        return response.status(401).json({
            message
        });
    }
}