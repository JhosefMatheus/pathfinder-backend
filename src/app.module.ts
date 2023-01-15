import { Module } from '@nestjs/common';
import { AuthModule } from './auth/auth.module';
import { ClassModule } from './class/class.module';
import { PathfinderModule } from './pathfinder/pathfinder.module';
import { PrismaModule } from './prisma/prisma.module';
import { RequirementPathfinderModule } from './requirementPathfinder/requirementPathfinder.module';
import { TokenModule } from './token/token.module';

@Module({
  imports: [
    PrismaModule,
    AuthModule,
    TokenModule,
    PathfinderModule,
    ClassModule,
    RequirementPathfinderModule
  ]
})
export class AppModule {}
