import { IsNotEmpty } from "class-validator";

export class CreateEditPathfinderDto {
    @IsNotEmpty()
    pathfinderName: string;
}