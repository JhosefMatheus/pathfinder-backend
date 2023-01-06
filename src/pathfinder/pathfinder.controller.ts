import { Controller, Get, Param, Res, UseGuards, Post, Body, Delete, Put } from "@nestjs/common";
import { Response } from "express";
import { PathfinderService } from "./pathfinder.service";
import { AuthGuard } from "@nestjs/passport";
import { Pathfinder } from "@prisma/client";
import { IDeleteEditPathfinderParams, IGetCreatePathfindersParams } from "./interface";
import { CreateEditPathfinderDto } from "./dto";

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
    
    @Get(":userId/:pathfinderId")
    async getPathfinder(@Res() response: Response, @Param() params: IGetCreatePathfindersParams): Promise<Response> {
        const { userId, pathfinderId } = params;

        console.log("entrou nessa função aqui.");

        const { flag, message, pathfinder } = await this.pathfinderService.getPathfinder(userId, pathfinderId);

        if (flag) {
            return response.status(200).json({
                message,
                pathfinder
            });
        }

        return response.status(401).json({
            message,
            pathfinder
        });
    }

    @Post("create/:userId")
    async createPathfinder(@Res() response: Response, @Param() params: IGetCreatePathfindersParams, @Body() createPathfinderDto: CreateEditPathfinderDto): Promise<Response> {
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
    async deletePathfinder(@Res() response: Response, @Param() params: IDeleteEditPathfinderParams): Promise<Response> {
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

    @Put("edit/:userId/:pathfinderId")
    async editPathfinder(@Res() response: Response, @Param() params: IDeleteEditPathfinderParams, @Body() editPathfinderDto: CreateEditPathfinderDto): Promise<Response> {
        const { userId, pathfinderId } = params;
        const { pathfinderName } = editPathfinderDto;

        const { flag, message } = await this.pathfinderService.editPathfinder(userId, pathfinderId, pathfinderName);

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