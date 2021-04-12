/*
SQLyog Professional v13.1.1 (64 bit)
MySQL - 5.6.50 : Database - school
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`school` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `school`;

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `course` */

/*Table structure for table `grade` */

DROP TABLE IF EXISTS `grade`;

CREATE TABLE `grade` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `teacher_id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `grade` varchar(45) NOT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  `date_reg` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `teacher_id_UNIQUE` (`teacher_id`),
  KEY `fk_course_teacher_idx` (`teacher_id`),
  CONSTRAINT `fk_course_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `grade` */

/*Table structure for table `shelude` */

DROP TABLE IF EXISTS `shelude`;

CREATE TABLE `shelude` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `grade_id` bigint(20) NOT NULL,
  `course_id` bigint(20) NOT NULL,
  `teacher_id` bigint(20) NOT NULL,
  `date_start` datetime NOT NULL,
  `date_end` datetime NOT NULL,
  `estatus` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_grade_has_course_course1_idx` (`course_id`),
  KEY `fk_grade_has_course_grade1_idx` (`grade_id`),
  KEY `fk_grade_has_course_teacher1_idx` (`teacher_id`),
  CONSTRAINT `fk_grade_has_course_course1` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_grade_has_course_grade1` FOREIGN KEY (`grade_id`) REFERENCES `grade` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_grade_has_course_teacher1` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `shelude` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `identification` varchar(20) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) NOT NULL,
  `second_surname` varchar(100) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  `date_reg` datetime DEFAULT CURRENT_TIMESTAMP,
  `grade_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_student_course1_idx` (`grade_id`),
  CONSTRAINT `fk_student_course1` FOREIGN KEY (`grade_id`) REFERENCES `grade` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

/*Data for the table `student` */

insert  into `student`(`id`,`identification`,`first_name`,`middle_name`,`last_name`,`second_surname`,`age`,`phone`,`address`,`image`,`status`,`date_reg`,`grade_id`) values 
(1,'','Shannon','David','Villa','Cantillo',24,'3017896029','Calle 16#15-135',NULL,1,'2021-02-22 01:55:44',NULL),
(3,'','Danny','Joel','Ospino','Munoz',20,'3245468614','Hcar 3',NULL,1,'2021-02-22 02:03:10',NULL),
(13,'','Jesus',NULL,'Urueta',NULL,21,'3022948801','Cra 41a#33-77',NULL,1,'2021-03-12 19:46:20',NULL),
(14,'','Danny',NULL,'Ospino',NULL,25,'3022222222','Cra 32#28-31',NULL,1,'2021-03-12 19:48:55',NULL),
(15,'','Danny',NULL,'Ospino',NULL,25,'3022222222','Cra 32#28-31',NULL,0,'2021-03-12 22:24:33',NULL),
(16,'','Danny',NULL,'Ospino',NULL,25,'3022222222','Cra 32#28-31',NULL,1,'2021-03-12 22:24:38',NULL),
(17,'','Shannon',NULL,'Villa',NULL,24,'3017896029','Calle 16#15-135',NULL,1,'2021-03-12 22:40:11',NULL),
(18,'','Shannon',NULL,'Villa',NULL,24,'3017896029','Calle 16#15-135','img/imgphotouser.png',1,'2021-03-15 14:27:28',NULL),
(19,'','Shannon',NULL,'Villa',NULL,24,'3017896029','Calle 16#15-135','img/imgphotouser.png',1,'2021-03-15 14:28:34',NULL),
(20,'','Shannon',NULL,'Villa',NULL,24,'3017896029','Calle 16#15-135','img/imgphotouser.png',1,'2021-03-15 14:28:54',NULL),
(21,'','Shannon',NULL,'Villa',NULL,24,'3017896029','Calle 16#15-135','img/imgphotouserShannon.png',1,'2021-03-15 14:30:03',NULL),
(22,'','Jesus',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','img/imgphotouserJesus.png',1,'2021-03-15 14:31:52',NULL),
(23,'','Jesusa',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','img/imgphotouserJesusa.png',1,'2021-03-15 14:56:27',NULL),
(24,'','Jesusa',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','img/imgphotouserJesusa.png',1,'2021-03-15 14:58:57',NULL),
(25,'','Jesusa',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','img/imgphotouserJesusa.png',1,'2021-03-15 14:59:24',NULL),
(26,'','Jesus',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST0ZJTEUAAQEAAAIYAAAAAAIQAABtbnRyUkdCIFhZWiAAAAAAAAAAAAAAAABh',1,'2021-03-15 16:57:01',NULL),
(27,'','JesusD',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','JPEG',1,'2021-03-15 16:58:12',NULL),
(28,'','Jesus',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','C:\\Users\\User\\Documents\\Proyectos\\application/img/imgphotouserJesus.png',1,'2021-03-15 17:10:42',NULL),
(29,'','Jesus David',NULL,'Urueta',NULL,20,'3022948801','Cra 41a#33-77','C:\\Users\\User\\Documents\\Proyectos\\application/img/imgphotouserJesus David.png',1,'2021-03-15 17:11:01',NULL),
(30,'','Ignacia',NULL,'Cantillo',NULL,20,'3022948801','Cra 41a#33-77','C:\\Users\\User\\Documents\\Proyectos\\application/img/imgphotouserIgnacia.png',1,'2021-03-15 17:11:42',NULL),
(31,'','Andres',NULL,'Cantillo',NULL,20,'3022948801','Cra 41a#33-77','C:\\Users\\User\\Documents\\Proyectos\\application/img/imgphotouserAndres.png',1,'2021-03-16 16:22:55',NULL),
(32,'','Andres',NULL,'Cantillo',NULL,20,'3022948801','Cra 41a#33-77','/img/imgphotouserAndres.png',1,'2021-03-16 16:24:35',NULL),
(33,'','Yutri',NULL,'Cantillo',NULL,20,'3022948801','Cra 41a#33-77','/img/imgphotouserYutri.png',1,'2021-03-16 16:24:48',NULL);

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) NOT NULL,
  `second_surname` varchar(100) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `address` varchar(100) NOT NULL,
  `identification` varchar(45) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT '1',
  `date_reg` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `identification_UNIQUE` (`identification`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `teacher` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
