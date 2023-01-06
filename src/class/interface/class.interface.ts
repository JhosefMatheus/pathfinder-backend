import { Class, Requirement } from "@prisma/client";

export interface IGetClassDataParams {
    classId: string;
}

export interface IGetClassData {
    flag: boolean;
    message: string;
    selectedClass?: Class;
}

export interface IGetRequirementsParams {
    requirementGroupId: string;
    classId: string;
}

export interface IGetRequirementsData {
    flag: boolean;
    message: string;
    requirements?: Requirement[]
}