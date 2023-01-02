import { IsNotEmpty } from "class-validator";

export class CreatePathfinderDto {
    @IsNotEmpty()
    pathfinderName: string;
}