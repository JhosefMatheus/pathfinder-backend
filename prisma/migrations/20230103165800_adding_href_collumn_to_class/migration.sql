/*
  Warnings:

  - Added the required column `href` to the `Class` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE `class` ADD COLUMN `href` VARCHAR(191) NOT NULL;
