-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2023 at 03:00 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_lp_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `figures`
--

CREATE TABLE `figures` (
  `fig_id` bigint(20) NOT NULL,
  `fig_name` varchar(50) DEFAULT NULL,
  `fig_img` varchar(255) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `man_id` int(11) DEFAULT NULL,
  `series_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `figures`
--

INSERT INTO `figures` (`fig_id`, `fig_name`, `fig_img`, `type_id`, `man_id`, `series_id`) VALUES
(1, 'Karin Kakudate', 'f7ba188b5451c348e19fa4ef87248114.png', 1, 3, 1),
(2, 'Nendoroid Hitori Gotoh', '291e3dfd76061c2a5b14966f200f8463.png', 2, 1, 2),
(3, 'POP UP PARADE Mori Calliope', 'a1e3ac8ff69e2d87ab8d80be427d35be.png', 3, 1, 4),
(4, 'Shirogane Noel: Swimsuit Ver.', 'e401a57f66d5d86591b33868cc1684f3.png', 1, 1, 4),
(5, 'Time Compass', '498450c5f89334a71b4cdbcd19cffd10.png', 1, 4, NULL);

--
-- Triggers `figures`
--
DELIMITER $$
CREATE TRIGGER `num_fig_adder` AFTER INSERT ON `figures` FOR EACH ROW begin
    update manufacturers as A
    set A.man_figures =  A.man_figures + 1
    where A.man_id = NEW.man_id;

    update figure_types as B
    set B.type_figures = B.type_figures + 1
    where B.type_id = NEW.type_id;

    update series as C 
    set C.series_figures = C.series_figures + 1
    where C.series_id = NEW.series_id;
end
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `num_fig_subtractor` AFTER DELETE ON `figures` FOR EACH ROW begin
    update manufacturers as A
    set A.man_figures = A.man_figures - 1
    where A.man_id = OLD.man_id;

    update figure_types as B
    set B.type_figures = B.type_figures - 1
    where B.type_id = OLD.type_id;

    update series as C 
    set C.series_figures = C.series_figures - 1
    where C.series_id = OLD.series_id;
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Stand-in structure for view `figure_info`
-- (See below for the actual view)
--
CREATE TABLE `figure_info` (
`id` bigint(20)
,`name` varchar(50)
,`img` varchar(255)
,`type` varchar(20)
,`manufacturer` varchar(25)
,`series` varchar(50)
);

-- --------------------------------------------------------

--
-- Table structure for table `figure_types`
--

CREATE TABLE `figure_types` (
  `type_id` int(11) NOT NULL,
  `type_name` varchar(20) DEFAULT NULL,
  `type_figures` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `figure_types`
--

INSERT INTO `figure_types` (`type_id`, `type_name`, `type_figures`) VALUES
(1, '1/7th scale', 3),
(2, 'nendoroid', 1),
(3, 'pop up parade', 1),
(4, 'figma', 0);

-- --------------------------------------------------------

--
-- Table structure for table `manufacturers`
--

CREATE TABLE `manufacturers` (
  `man_id` int(11) NOT NULL,
  `man_name` varchar(25) DEFAULT NULL,
  `man_figures` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `manufacturers`
--

INSERT INTO `manufacturers` (`man_id`, `man_name`, `man_figures`) VALUES
(1, 'Good Smile Company', 3),
(2, 'FREEing', 0),
(3, 'Max Factory', 1),
(4, 'myethos', 1);

-- --------------------------------------------------------

--
-- Table structure for table `series`
--

CREATE TABLE `series` (
  `series_id` int(11) NOT NULL,
  `series_name` varchar(50) DEFAULT NULL,
  `series_figures` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `series`
--

INSERT INTO `series` (`series_id`, `series_name`, `series_figures`) VALUES
(1, 'Blue archive', 1),
(2, 'bocchi the rock', 1),
(3, 'original', 0),
(4, 'Hololive', 2);

-- --------------------------------------------------------

--
-- Structure for view `figure_info`
--
DROP TABLE IF EXISTS `figure_info`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `figure_info`  AS SELECT `figures`.`fig_id` AS `id`, `figures`.`fig_name` AS `name`, `figures`.`fig_img` AS `img`, `a`.`type_name` AS `type`, `b`.`man_name` AS `manufacturer`, `c`.`series_name` AS `series` FROM (((`figures` join `figure_types` `a` on(`figures`.`type_id` = `a`.`type_id`)) join `manufacturers` `b` on(`figures`.`man_id` = `b`.`man_id`)) join `series` `c` on(`figures`.`series_id` = `c`.`series_id`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `figures`
--
ALTER TABLE `figures`
  ADD PRIMARY KEY (`fig_id`),
  ADD UNIQUE KEY `fig_name` (`fig_name`),
  ADD UNIQUE KEY `fig_img` (`fig_img`),
  ADD KEY `type_id` (`type_id`),
  ADD KEY `man_id` (`man_id`),
  ADD KEY `series_id` (`series_id`);

--
-- Indexes for table `figure_types`
--
ALTER TABLE `figure_types`
  ADD PRIMARY KEY (`type_id`),
  ADD UNIQUE KEY `type_name` (`type_name`);

--
-- Indexes for table `manufacturers`
--
ALTER TABLE `manufacturers`
  ADD PRIMARY KEY (`man_id`),
  ADD UNIQUE KEY `man_name` (`man_name`);

--
-- Indexes for table `series`
--
ALTER TABLE `series`
  ADD PRIMARY KEY (`series_id`),
  ADD UNIQUE KEY `series_name` (`series_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `figures`
--
ALTER TABLE `figures`
  MODIFY `fig_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `figure_types`
--
ALTER TABLE `figure_types`
  MODIFY `type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `manufacturers`
--
ALTER TABLE `manufacturers`
  MODIFY `man_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `series`
--
ALTER TABLE `series`
  MODIFY `series_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `figures`
--
ALTER TABLE `figures`
  ADD CONSTRAINT `figures_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `figure_types` (`type_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `figures_ibfk_2` FOREIGN KEY (`man_id`) REFERENCES `manufacturers` (`man_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `figures_ibfk_3` FOREIGN KEY (`series_id`) REFERENCES `series` (`series_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
