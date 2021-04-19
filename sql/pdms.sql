/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80023
 Source Host           : localhost:3306
 Source Schema         : pdms

 Target Server Type    : MySQL
 Target Server Version : 80023
 File Encoding         : 65001

 Date: 20/04/2021 00:28:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_phish_tank_website_info
-- ----------------------------
DROP TABLE IF EXISTS `t_phish_tank_website_info`;
CREATE TABLE `t_phish_tank_website_info`  (
  `phish_id` bigint(0) NULL DEFAULT NULL,
  `url` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `phish_detail_url` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `submission_time` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `verified` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `verification_time` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `online` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `target` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
