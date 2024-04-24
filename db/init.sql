/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - scrapnet
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`scrapnet` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `scrapnet`;

/*Table structure for table `certificate` */

DROP TABLE IF EXISTS `certificate`;

CREATE TABLE `certificate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sdid` varchar(90) DEFAULT NULL,
  `cert` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `certificate` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `dealer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`cid`,`uid`,`dealer_id`,`complaint`,`date`,`reply`) values 
(1,5,2,'asd','2023-02-15','its ok'),
(2,5,2,'qwert','2023-02-23','ok'),
(3,5,2,'asdfgh','2023-03-02','okda'),
(4,5,2,'zxcvbnm','2023-03-02','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(90) DEFAULT NULL,
  `password` varchar(90) DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'rto','rto','rto'),
(2,'hasna123','hasna123','Scrapdealer'),
(5,'u','u','User'),
(11,'gokul','gokul','Scrapdealer');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `sdid` int(11) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rid`,`uid`,`sdid`,`rating`) values 
(1,5,2,3),
(2,5,2,5),
(3,5,2,5),
(4,5,2,4.5),
(5,5,11,3.5);

/*Table structure for table `scrapdealer` */

DROP TABLE IF EXISTS `scrapdealer`;

CREATE TABLE `scrapdealer` (
  `sdid` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) DEFAULT NULL,
  `sdname` varchar(90) DEFAULT NULL,
  `place` varchar(90) DEFAULT NULL,
  `post` varchar(90) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(15) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `proof` text,
  PRIMARY KEY (`sdid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `scrapdealer` */

insert  into `scrapdealer`(`sdid`,`loginid`,`sdname`,`place`,`post`,`pin`,`phone`,`email`,`proof`) values 
(1,2,'Hasna','Parappanangadi','Malappuram',542425,873244790,'has@gmail.com','dbconnectionnew.txt'),
(6,11,'gokul','kannur','kkk',670000,9996787878,'gokulspa@gmail.com','6b4a4cfe79f9423fcf6c105d117ec620.jpg');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) DEFAULT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pin` bigint(10) DEFAULT NULL,
  `phone` bigint(15) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`loginid`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,5,'thani','t','','','',0,0,'');

/*Table structure for table `userrequest` */

DROP TABLE IF EXISTS `userrequest`;

CREATE TABLE `userrequest` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `sdid` varchar(90) DEFAULT NULL,
  `vid` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `userrequest` */

insert  into `userrequest`(`rid`,`sdid`,`vid`,`date`,`status`) values 
(1,'2','1','2023-03-02','Accepted'),
(2,'2','2','2023-03-02','Forwarded'),
(5,'11','4','2023-03-30','Accepted'),
(7,'2','4','2023-03-30','Accepted'),
(8,'2','4','2023-03-30','Accepted');

/*Table structure for table `vehicle` */

DROP TABLE IF EXISTS `vehicle`;

CREATE TABLE `vehicle` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `model` varchar(20) DEFAULT NULL,
  `rc` varchar(500) DEFAULT NULL,
  `fitness` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `vehicle` */

insert  into `vehicle`(`vid`,`uid`,`model`,`rc`,`fitness`) values 
(1,5,'renault duster','20230302_130150.jpg','20230302_130150.jpg'),
(2,5,'ferrari','20230302_132441.jpg','20230302_132441.jpg'),
(4,5,'gwagon','20230302_135651.jpg','20230302_135651.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
