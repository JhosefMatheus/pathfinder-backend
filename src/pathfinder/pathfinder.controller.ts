import { Controller, Get, Param, Res, UseGuards, Post, Body, Delete } from "@nestjs/common";
import { Response } from "express";
import { PathfinderService } from "./pathfinder.service";
import { AuthGuard } from "@nestjs/passport";
import { Pathfinder } from "@prisma/client";
import { IDeletePathfinderParams, IGetCreatePathfindersParams } from "./interface";
import { CreatePathfinderDto } from "./dto";

@UseGuards(AuthGuard("jwt"))
@Controller("pathfinder")
export class PathfinderController {
    constructor(private readonly pathfinderService: PathfinderService) {}

    @Get("pathfinders/:userId")
    async getPathfinders(@Res() response: Response, @Param() params: IGetCreatePathfindersParams): Promise<Response> {
        const { userId } = params;

        const pathfinders: Pathfinder[] = await this.pathfinderService.getPathfinders(userId);

        return response.status(200).json({
            pathfinders
        });
    }

    @Post("create/:userId")
    async createPathfinder(@Res() response: Response, @Param() params: IGetCreatePathfindersParams, @Body() createPathfinderDto: CreatePathfinderDto): Promise<Response> {
        const { userId } = params;
        const { pathfinderName } = createPathfinderDto;

        const { flag, message } = await this.pathfinderService.createPathfinder(userId, pathfinderName);

        if (flag) {
            return response.status(200).json({
                message
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Delete("delete/:userId/:pathfinderId")
    async deletePathfinder(@Res() response: Response, @Param() params: IDeletePathfinderParams): Promise<Response> {
        const { userId, pathfinderId } = params;

        const { flag, message } = await this.pathfinderService.deletePathfinder(userId, pathfinderId);

        if (flag) {
            return response.status(200).json({
                message
            });
        }

        return response.status(401).json({
            message
        });
    }
}