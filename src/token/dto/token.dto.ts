import { IsNotEmpty, IsString } from "class-validator";

export class TokenHeadersDto {
    @IsNotEmpty()
    authorization: string;

    [props: string]: any;
}