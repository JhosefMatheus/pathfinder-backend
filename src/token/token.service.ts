import { Injectable } from "@nestjs/common";
import { ConfigService } from "@nestjs/config";
import { JwtService } from "@nestjs/jwt";
import { ITokenVerify } from "./interface";

@Injectable()
export class TokenService {
    constructor(private readonly configService: ConfigService, private readonly jwtService: JwtService) {}

    async verify(token: string): Promise<ITokenVerify> {
        const tokenOptions: object = {
            secret: this.configService.get("JWT_SECRET"),
            algorithms: "HS256"
        }

        try {
            const tokenData = await this.jwtService.verifyAsync(token, tokenOptions);

            return {
                flag: true,
                message: "Token válido.",
                userInfo: {
                    ...tokenData
                }
            }
        } catch (error) {
            return {
                flag: false,
                message: "Token inválido."
            }
        }
    }
}