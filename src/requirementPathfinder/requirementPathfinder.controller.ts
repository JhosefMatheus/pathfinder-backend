import { Controller, Get, Param, Res } from "@nestjs/common";
import { Response } from "express";
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
}