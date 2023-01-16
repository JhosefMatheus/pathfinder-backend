import { RequirementPathfinder } from "@prisma/client";
import { IsNotEmpty } from "class-validator";

export class SaveRequirementsPathfinderDto {
    @IsNotEmpty()
    requirementsPathfinder: RequirementPathfinder[];
}