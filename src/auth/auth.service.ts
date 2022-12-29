import { Injectable } from "@nestjs/common";
import { Prisma, User } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
import { IJwtOptions, IJwtPayload, ISignInSignUp } from "./interface";
import * as argon2 from "argon2";
import { JwtService } from "@nestjs/jwt";
import { ConfigService } from "@nestjs/config";

@Injectable()
export class AuthService {
    constructor(private readonly prismaService: PrismaService, private readonly jwtService: JwtService, private readonly configService: ConfigService) {}

    private async generateToken(user: User): Promise<string> {
        const jwtPayload: IJwtPayload = {
            sub: user.id,
            nome: user.name,
            login: user.login
        }

        const jwtOptions: IJwtOptions = {
            expiresIn: "2d",
            secret: this.configService.get("JWT_SECRET")
        }

        const token: string = await this.jwtService.signAsync(jwtPayload, jwtOptions);

        return token;
    }

    async signIn(login: string, password: string): Promise<ISignInSignUp> {
        const user: User = await this.prismaService.user.findFirst({
            where: {
                login: {
                    equals: login
                }
            }
        });

        if (user) {
            const hashedPassword = user.password;

            const passwordVerify = await argon2.verify(hashedPassword, password);

            if (passwordVerify) {
                const token: string = await this.generateToken(user);

                return {
                    flag: true,
                    message: "Usuário logado com sucesso.",
                    token
                }
            }
        }

        return {
            flag: false,
            message: "Login ou senha inválidos."
        }
    }

    async signUp(name: string, login: string, password: string): Promise<ISignInSignUp> {
        try {
            const hashedPassword: string = await argon2.hash(password);

            await this.prismaService.user.create({
                data: {
                    name: name,
                    login: login,
                    password: hashedPassword
                }
            });

            return {
                flag: true,
                message: "Usuário cadastrado com sucesso."
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2002") {
                    return {
                        flag: false,
                        message: "Login já está sendo usado, por favor forneça outro login."
                    }
                }
            }
        }
    }
}