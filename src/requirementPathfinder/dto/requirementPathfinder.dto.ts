import { IsNotEmpty } from "class-validator";

export interface RequirementPathfinderDto {
    id?: number;
    pathfinderId: string;
    requirementId: number;
}

export class SaveRequirementsPathfinderDto {
    @IsNotEmpty()
    addedRequirementsPathfinder: RequirementPathfinderDto[];
    
    @IsNotEmpty()
    deletedRequirementsPathfinder: RequirementPathfinderDto[];
}