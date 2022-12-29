/*
  Warnings:

  - You are about to drop the column `idClub` on the `user` table. All the data in the column will be lost.
  - You are about to drop the column `idPosition` on the `user` table. All the data in the column will be lost.
  - You are about to drop the `club` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `position` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE `user` DROP FOREIGN KEY `User_idClub_fkey`;

-- DropForeignKey
ALTER TABLE `user` DROP FOREIGN KEY `User_idPosition_fkey`;

-- AlterTable
ALTER TABLE `user` DROP COLUMN `idClub`,
    DROP COLUMN `idPosition`;

-- DropTable
DROP TABLE `club`;

-- DropTable
DROP TABLE `position`;
