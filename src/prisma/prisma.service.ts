import { PrismaClient } from "@prisma/client";
import { ConfigService } from "@nestjs/config/dist";
import { Injectable } from "@nestjs/common/decorators";

@Injectable()
export class PrismaService extends PrismaClient {
    constructor(readonly config: ConfigService) {
        super({
            datasources: {
                db: {
                    url: config.get("DATABASE_URL")
                }
            }
        })
    }
}