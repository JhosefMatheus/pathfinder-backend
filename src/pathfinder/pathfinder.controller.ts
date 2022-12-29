import { Controller, Get, Res, UseGuards } from "@nestjs/common";
import { Response } from "express";
import { PathfinderService } from "./pathfinder.service";
import { AuthGuard } from "@nestjs/passport";
import { Pathfinder } from "@prisma/client";

@UseGuards(AuthGuard("jwt"))
@Controller("pathfinder")
export class PathfinderController {
    constructor(private readonly pathfinderService: PathfinderService) {}

    @Get("pathfinders")
    async getPathfinders(@Res() response: Response): Promise<Response> {
        const pathfinders: Pathfinder[] = await this.pathfinderService.getPathfinders();

        return response.status(200).json({
            pathfinders
        });
    }
}