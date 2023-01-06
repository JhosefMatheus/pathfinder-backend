import { Pathfinder } from "@prisma/client";

export interface IGetCreatePathfindersParams {
    userId: string;
    pathfinderId?: string;
}

export interface ICrudPathfinder {
    flag: boolean;
    message: string;
    pathfinder?: Pathfinder;
}

export interface IDeleteEditPathfinderParams {
    userId: string;
    pathfinderId: string;
}