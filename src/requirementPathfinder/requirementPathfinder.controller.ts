import { Body, Controller, Get, Param, Post, Res } from "@nestjs/common";
import { Response } from "express";
import { SaveRequirementsPathfinderDto } from "./dto";
import { IGetRequirementsPathfinderParams } from "./interface";
import { RequirementPathfinderService } from "./requirementPathfinder.service";

@Controller("requirementPathfinder")
export class RequirementPathfinderController {
    constructor(private readonly requirementPathfinderService: RequirementPathfinderService) {}

    @Get("requirementsPathfinder/:pathfinderId/:requirementId")
    async getRequirementsPathfinder(@Res() response: Response, @Param() params: IGetRequirementsPathfinderParams): Promise<Response> {
        const { pathfinderId, requirementId } = params;

        const {flag, message, requirementPathfinder } = await this.requirementPathfinderService.getRequirementsPathfinder(pathfinderId, requirementId);

        if (flag) {
            return response.status(200).json({
                message,
                requirementPathfinder
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Post("requirementsPathfinder/save")
    saveRequirementsPathfinder(@Res() response: Response, @Body() saveRequirementsPathfinderDto: SaveRequirementsPathfinderDto): Response {
        const { addedRequirementsPathfinder, deletedRequirementsPathfinder } = saveRequirementsPathfinderDto;

        this.requirementPathfinderService.saveRequirementsPathfinder(addedRequirementsPathfinder, deletedRequirementsPathfinder);

        return response.status(200).json({
            message: "Requisitos do desbravador salvos com sucesso!"
        });
    }
}