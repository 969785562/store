/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80025
Source Host           : localhost:3306
Source Database       : bank

Target Server Type    : MYSQL
Target Server Version : 80025
File Encoding         : 65001

Date: 2021-10-14 11:07:14
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `username` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `password` int DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `
province` varchar(255) DEFAULT NULL,
  `street` varchar(255) DEFAULT NULL,
  `gate` varchar(255) DEFAULT NULL,
  `money` int DEFAULT NULL,
  `bank` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
