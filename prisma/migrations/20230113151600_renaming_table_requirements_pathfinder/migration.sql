/*
  Warnings:

  - You are about to drop the `requirementspathfinder` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `requirementspathfinder` DROP FOREIGN KEY `RequirementsPathfinder_pathfinderId_fkey`;

-- DropForeignKey
ALTER TABLE `requirementspathfinder` DROP FOREIGN KEY `RequirementsPathfinder_requirementId_fkey`;

-- DropTable
DROP TABLE `requirementspathfinder`;

-- CreateTable
CREATE TABLE `RequirementPathfinder` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `pathfinderId` INTEGER NOT NULL,
    `requirementId` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `RequirementPathfinder` ADD CONSTRAINT `RequirementPathfinder_pathfinderId_fkey` FOREIGN KEY (`pathfinderId`) REFERENCES `Pathfinder`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RequirementPathfinder` ADD CONSTRAINT `RequirementPathfinder_requirementId_fkey` FOREIGN KEY (`requirementId`) REFERENCES `Requirement`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
