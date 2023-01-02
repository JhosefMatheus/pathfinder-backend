interface UserInfo {
    id: number;
    name: string;
    login: string;
}

export interface ISignInSignUp {
    flag: boolean;
    message: string;
    token?: string;
    userInfo?: UserInfo
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