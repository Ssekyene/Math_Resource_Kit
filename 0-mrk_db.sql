-- MySQL dump 10.13  Distrib 5.7.34, for Linux (x86_64)
--
-- Host: localhost    Database: mrk_db
-- ------------------------------------------------------
-- Server version	5.7.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activity`
--

DROP TABLE IF EXISTS `activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activity` (
  `id` varchar(60) NOT NULL,
  `description` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `concept_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `concept_id` (`concept_id`),
  CONSTRAINT `activity_ibfk_1` FOREIGN KEY (`concept_id`) REFERENCES `concept` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity`
--

LOCK TABLES `activity` WRITE;
/*!40000 ALTER TABLE `activity` DISABLE KEYS */;
INSERT INTO `activity` VALUES ('72864aa6-cc9d-484f-b9c6-4ca2d3954b15','His singulis copiose responderi solet, sed quae perspicua sunt longa esse non debent. Quid ergo hoc loco intellegit honestum? Hoc non est positum in nostra actione.','2024-09-14 15:01:38','2024-09-14 15:01:38','22e9f662-31eb-4435-8b90-8a006a5669ad');
/*!40000 ALTER TABLE `activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `concept`
--

DROP TABLE IF EXISTS `concept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `concept` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` varchar(1024) NOT NULL,
  `introduction` text NOT NULL,
  `conclusion` text,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concept`
--

LOCK TABLES `concept` WRITE;
/*!40000 ALTER TABLE `concept` DISABLE KEYS */;
INSERT INTO `concept` VALUES ('22e9f662-31eb-4435-8b90-8a006a5669ad','2024-09-14 14:00:23','2024-09-14 14:30:19','Numbers','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Multoque hoc melius nos veriusque quam Stoici. Quoniam, si dis placet, ab Epicuro loqui discimus. Respondent extrema primis, media utrisque, omnia omnibus. Haec para/doca illi, nos admirabilia dicamus. Cum autem in quo sapienter dicimus, id a primo rectissime dicitur. Duo Reges: constructio interrete. Et ille ridens: Video, inquit, quid agas; Ergo adhuc, quantum equidem intellego, causa non videtur fuisse mutandi nominis.','Equidem, sed audistine modo de Carneade? Quis enim redargueret? Dulce amarum, leve asperum, prope longe, stare movere, quadratum rotundum. Collige omnia, quae soletis: Praesidium amicorum. At eum nihili facit; Etenim semper illud extra est, quod arte comprehenditur. Inscite autem medicinae et',NULL);
/*!40000 ALTER TABLE `concept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `concept_resource`
--

DROP TABLE IF EXISTS `concept_resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `concept_resource` (
  `concept_id` varchar(60) NOT NULL,
  `resource_id` varchar(60) NOT NULL,
  PRIMARY KEY (`concept_id`,`resource_id`),
  KEY `resource_id` (`resource_id`),
  CONSTRAINT `concept_resource_ibfk_1` FOREIGN KEY (`concept_id`) REFERENCES `concept` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `concept_resource_ibfk_2` FOREIGN KEY (`resource_id`) REFERENCES `resource` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concept_resource`
--

LOCK TABLES `concept_resource` WRITE;
/*!40000 ALTER TABLE `concept_resource` DISABLE KEYS */;
INSERT INTO `concept_resource` VALUES ('22e9f662-31eb-4435-8b90-8a006a5669ad','c30fb993-ede0-4588-a260-3f562486cfa2');
/*!40000 ALTER TABLE `concept_resource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `option`
--

DROP TABLE IF EXISTS `option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `option` (
  `id` varchar(60) NOT NULL,
  `description` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `option`
--

LOCK TABLES `option` WRITE;
/*!40000 ALTER TABLE `option` DISABLE KEYS */;
INSERT INTO `option` VALUES ('92187480-ee28-4ccc-8d75-559fb3a47d1d','illa autem voluptas ipsius disputationem volo, nec tua mihi oratio','2024-09-14 15:27:33','2024-09-14 15:27:33'),('ccd36ac7-41eb-4d7c-8877-e54ab901420a','illa autem voluptas ipsius in motu est','2024-09-14 15:27:33','2024-09-14 15:27:33'),('d97dacd6-1d12-47a4-90c5-711246a3372e','illa autem voluptas ipsius','2024-09-14 15:27:33','2024-09-14 15:27:33'),('e570f0e1-edfa-43d8-a2fa-6d1ad9fcb766','illa autem voluptas','2024-09-14 15:27:33','2024-09-14 15:27:33');
/*!40000 ALTER TABLE `option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quiz` (
  `id` varchar(60) NOT NULL,
  `description` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `correct_option` varchar(12) NOT NULL,
  `concept_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `concept_id` (`concept_id`),
  CONSTRAINT `quiz_ibfk_1` FOREIGN KEY (`concept_id`) REFERENCES `concept` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz`
--

LOCK TABLES `quiz` WRITE;
/*!40000 ALTER TABLE `quiz` DISABLE KEYS */;
INSERT INTO `quiz` VALUES ('55a11d7a-4eb6-44af-92ab-542a998567d3','laut cogitari esse aliquod animal, quod se oderit? Quid censes in Latino fore?','2024-09-14 15:08:42','2024-09-14 15:27:33','A','22e9f662-31eb-4435-8b90-8a006a5669ad');
/*!40000 ALTER TABLE `quiz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz_option`
--

DROP TABLE IF EXISTS `quiz_option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quiz_option` (
  `quiz_id` varchar(60) NOT NULL,
  `option_id` varchar(60) NOT NULL,
  PRIMARY KEY (`quiz_id`,`option_id`),
  KEY `option_id` (`option_id`),
  CONSTRAINT `quiz_option_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `quiz_option_ibfk_2` FOREIGN KEY (`option_id`) REFERENCES `option` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz_option`
--

LOCK TABLES `quiz_option` WRITE;
/*!40000 ALTER TABLE `quiz_option` DISABLE KEYS */;
INSERT INTO `quiz_option` VALUES ('55a11d7a-4eb6-44af-92ab-542a998567d3','92187480-ee28-4ccc-8d75-559fb3a47d1d'),('55a11d7a-4eb6-44af-92ab-542a998567d3','ccd36ac7-41eb-4d7c-8877-e54ab901420a'),('55a11d7a-4eb6-44af-92ab-542a998567d3','d97dacd6-1d12-47a4-90c5-711246a3372e'),('55a11d7a-4eb6-44af-92ab-542a998567d3','e570f0e1-edfa-43d8-a2fa-6d1ad9fcb766');
/*!40000 ALTER TABLE `quiz_option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resource`
--

DROP TABLE IF EXISTS `resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resource` (
  `id` varchar(60) NOT NULL,
  `description` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `url` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resource`
--

LOCK TABLES `resource` WRITE;
/*!40000 ALTER TABLE `resource` DISABLE KEYS */;
INSERT INTO `resource` VALUES ('04086e1b-7e5e-4e69-81f8-3e18852c72af','Duo Reges: constructio','2024-09-14 14:03:27','2024-09-14 14:03:27','Non est igitur summum malum dolor'),('c30fb993-ede0-4588-a260-3f562486cfa2','Duo Reges: constructio','2024-09-14 14:30:19','2024-09-14 14:30:19','Non est igitur summum malum dolor');
/*!40000 ALTER TABLE `resource` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-14 15:40:29
