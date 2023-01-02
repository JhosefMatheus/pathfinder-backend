export interface IGetCreatePathfindersParams {
    userId: string;
}

export interface ICreateDeletePathfinder {
    flag: boolean;
    message: string;
}

export interface IDeletePathfinderParams {
    userId: string;
    pathfinderId: string;
}