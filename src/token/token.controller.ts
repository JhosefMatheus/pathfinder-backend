import { Controller, Get, Headers, Res } from "@nestjs/common";
import { Response } from "express";
import { TokenHeadersDto } from "./dto";
import { TokenService } from "./token.service";

@Controller("token")
export class TokenController {
    constructor(private readonly tokenService: TokenService) {}

    @Get("verify")
    async verify(@Res() response: Response, @Headers() tokenHeadersDto: TokenHeadersDto): Promise<Response> {
        const { authorization } = tokenHeadersDto;

        if (authorization) {
            const token: string = authorization.replace("Bearer ", "");
    
            const { flag, message, userInfo } = await this.tokenService.verify(token);

            if (flag) {
                return response.status(200).json({
                    message,
                    userInfo: {
                        ...userInfo
                    }
                });
            }

            return response.status(401).json({
                message
            });
        }

        return response.status(401).json({
            message: "Token faltante."
        });
    }
}