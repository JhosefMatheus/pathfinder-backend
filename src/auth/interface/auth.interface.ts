export interface ISignInSignUp {
    flag: boolean;
    message: string;
    token?: string;
}

export interface IJwtPayload {
    sub: number;
    nome: string;
    login: string;
}

export interface IJwtOptions {
    expiresIn: string;
    secret: string;
}