/*
  Warnings:

  - You are about to drop the `requirementsubrequirement` table. If the table is not empty, all the data it contains will be lost.
  - Added the required column `classId` to the `Requirement` table without a default value. This is not possible if the table is not empty.
  - Added the required column `requirementId` to the `Subrequirement` table without a default value. This is not possible if the table is not empty.

*/
-- DropForeignKey
ALTER TABLE `requirementsubrequirement` DROP FOREIGN KEY `RequirementSubrequirement_requirementId_fkey`;

-- DropForeignKey
ALTER TABLE `requirementsubrequirement` DROP FOREIGN KEY `RequirementSubrequirement_subrequirementId_fkey`;

-- AlterTable
ALTER TABLE `requirement` ADD COLUMN `classId` INTEGER NOT NULL;

-- AlterTable
ALTER TABLE `subrequirement` ADD COLUMN `requirementId` INTEGER NOT NULL;

-- DropTable
DROP TABLE `requirementsubrequirement`;

-- AddForeignKey
ALTER TABLE `Requirement` ADD CONSTRAINT `Requirement_classId_fkey` FOREIGN KEY (`classId`) REFERENCES `Class`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Subrequirement` ADD CONSTRAINT `Subrequirement_requirementId_fkey` FOREIGN KEY (`requirementId`) REFERENCES `Requirement`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
