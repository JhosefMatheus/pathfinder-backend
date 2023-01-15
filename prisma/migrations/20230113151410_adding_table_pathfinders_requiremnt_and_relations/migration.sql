-- CreateTable
CREATE TABLE `RequirementsPathfinder` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `pathfinderId` INTEGER NOT NULL,
    `requirementId` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `RequirementsPathfinder` ADD CONSTRAINT `RequirementsPathfinder_pathfinderId_fkey` FOREIGN KEY (`pathfinderId`) REFERENCES `Pathfinder`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RequirementsPathfinder` ADD CONSTRAINT `RequirementsPathfinder_requirementId_fkey` FOREIGN KEY (`requirementId`) REFERENCES `Requirement`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
