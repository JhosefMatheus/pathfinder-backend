import { Body, Controller, Post, Res } from "@nestjs/common";
import { Response } from "express";
import { AuthService } from "./auth.service";
import { SignInDto, SignUpDto } from "./dto";

@Controller("auth")
export class AuthController {
    constructor(private readonly authService: AuthService) {}

    @Post("signIn")
    async signIn(@Res() response: Response, @Body() signInDto: SignInDto): Promise<Response> {
        const { login, password } = signInDto;

        const { flag, message, token, userInfo } = await this.authService.signIn(login, password);

        if (flag) {
            return response.status(200).json({
                message,
                token,
                userInfo
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Post("signUp")
    async signUp(@Res() response: Response, @Body() signUpDto: SignUpDto): Promise<Response> {
        const { name, login, password } = signUpDto;

        const { flag, message } = await this.authService.signUp(name, login, password);

        if (flag) {
            return response.status(200).json({
                message
            })
        }

        return response.status(401).json({
            message
        });
    }
}