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

export interface IGetPathfinderClassesProgressParams {
    pathfinderId: string;
}

export interface IGetPathfinderClassesProgressData {
    friendProgress: number;
    companionProgress: number;
    researcherProgress: number;
    pioneerProgress: number;
    hikerProgress: number;
    guideProgress: number;
}