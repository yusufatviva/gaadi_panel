/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.46-0ubuntu0.14.04.2 : Database - gaadi_panel
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gaadi_panel` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;

USE `gaadi_panel`;

/*Table structure for table `menu` */

DROP TABLE IF EXISTS `menu`;

CREATE TABLE `menu` (
  `menu_id` int(11) NOT NULL,
  `menu_name` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `menu_type` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `order` int(11) DEFAULT NULL,
  `url` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `icon` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`menu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `menu` */

insert  into `menu`(`menu_id`,`menu_name`,`menu_type`,`parent_id`,`order`,`url`,`icon`) values (1,'menu1','main_menu',0,1,'/a','fa fa-lg fa-bullhorn'),(2,'menu12','sub_menu',1,1,'/b','fa fa-lg fa-volume-up'),(3,'menu2','main_menu',0,2,'/c','fa fa-lg fa-desktop'),(4,'menu21','sub_menu',3,1,'/d','fa fa-lg fa-download'),(5,'menu22','sub_menu',3,2,'/e','fa fa-lg fa-gear'),(6,'menu3','main_menu',0,3,'/d','fa fa-lg fa-volume-up'),(7,'menu31','sub_menu',6,1,'/f','fa fa-lg fa-volume-up'),(8,'menu32','sub_menu',6,2,'/f','fa fa-lg fa-volume-up'),(9,'menu33','sub_menu',6,3,'/f','fa fa-lg fa-volume-up'),(10,'menu34','sub_menu',6,4,'/f','fa fa-lg fa-volume-up');

/*Table structure for table `role` */

DROP TABLE IF EXISTS `role`;

CREATE TABLE `role` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `role` */

insert  into `role`(`role_id`,`role_name`) values (1,'admin'),(2,'client');

/*Table structure for table `role_menu` */

DROP TABLE IF EXISTS `role_menu`;

CREATE TABLE `role_menu` (
  `role_id` int(11) DEFAULT NULL,
  `menu_id` int(11) DEFAULT NULL,
  KEY `roleidmapping` (`role_id`),
  KEY `menuidmapping` (`menu_id`),
  CONSTRAINT `menuidmapping` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`menu_id`),
  CONSTRAINT `roleidmapping` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `role_menu` */

insert  into `role_menu`(`role_id`,`menu_id`) values (1,1),(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,5);

/*Table structure for table `user_master` */

DROP TABLE IF EXISTS `user_master`;

CREATE TABLE `user_master` (
  `user_id` int(11) NOT NULL,
  `username` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `password` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

/*Data for the table `user_master` */

insert  into `user_master`(`user_id`,`username`,`password`,`role_id`) values (1,'admin','admin',1),(2,'client','client',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
