import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { Pathfinder } from "@prisma/client";

@Injectable()
export class PathfinderService {
    constructor(private readonly prismaService: PrismaService) {}

    async getPathfinders(): Promise<Pathfinder[]> {
        const pathfinders: Pathfinder[] = await this.prismaService.pathfinder.findMany();

        return pathfinders;
    }
}