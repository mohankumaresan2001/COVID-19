-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 04, 2023 at 03:19 AM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covid19`
--

-- --------------------------------------------------------

--
-- Table structure for table `cases_history`
--

DROP TABLE IF EXISTS `cases_history`;
CREATE TABLE IF NOT EXISTS `cases_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(50) NOT NULL,
  `confirmed_cases` double NOT NULL,
  `death_cases` double NOT NULL,
  `recovered_cases` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cases_history`
--

INSERT INTO `cases_history` (`id`, `date`, `confirmed_cases`, `death_cases`, `recovered_cases`) VALUES
(15, '08-10-2022', 2604, 1365, 2972),
(8, '01-10-2022', 746, 43, 509),
(16, '09-10-2022', 2480, 48, 260),
(9, '02-10-2022', 576, 75, 608),
(10, '03-10-2022', 1086, 124, 769),
(11, '04-10-2022', 1089, 124, 769),
(12, '05-10-2022', 564, 68, 296),
(13, '06-10-2022', 876, 54, 32),
(14, '07-10-2022', 654, 87, 165);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `user_name`, `password`) VALUES
(2, 'MOHAN K', '12345', '12345'),
(5, 'BALAJI S', '1234', '1234');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
