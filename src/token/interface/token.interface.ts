export interface IUserInfo {
    sub: number;
    nome: string;
    login: string;
    iat: number;
    exp: number;
}

export interface ITokenVerify {
    flag: boolean;
    message: string;
    userInfo?: IUserInfo;
}