import { RequirementPathfinder } from "@prisma/client";

export interface IGetRequirementsPathfinderParams {
    pathfinderId: string;
    requirementId: string;
}

export interface IGetRequirementsPathfinder {
    flag: boolean;
    message: string;
    requirementPathfinder?: RequirementPathfinder;
}