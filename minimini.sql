-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2024 at 05:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `minimini`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `eid` int(11) NOT NULL,
  `ename` varchar(255) NOT NULL,
  `erole` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`eid`, `ename`, `erole`, `password`) VALUES
(0, 'vikram', 'manager', '123456'),
(1, 'Ajay', 'waiter', 'ajay1'),
(2, 'Ravi ', 'waiter', '75321'),
(3, 'Sanjay', 'waiter', 'gfdjgewgfyue'),
(4, 'Rohit ', 'waiter', '125478'),
(5, 'Anil', 'waiter', '797578'),
(6, 'adarsh', 'waiter', '154789');

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE `food` (
  `fname` varchar(255) NOT NULL,
  `fdescription` varchar(255) NOT NULL,
  `fprice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`fname`, `fdescription`, `fprice`) VALUES
('Sushi', 'A Japanese dish of vinegared rice topped with various savory ingredients such as seafood, vegetables, and eggs.', 245),
('Pizza', 'An Italian dish of a baked dough topped with tomato sauce and cheese, often with additional ingredients such as anchovies, mushrooms, onions, olives, pineapple, meat, etc', 320),
('Tacos', 'A Mexican dish made with a small, hard corn tortilla filled with various ingredients such as seasoned ground beef, shredded chicken, or fish, lettuce, cheese, tomatoes, onions, and salsa.', 99),
('Pad Thai', 'A stir-fried rice noodle dish from Thailand, commonly made with eggs, peanuts, dried shrimp, vegetables, and a tamarind-based sauce.', 129),
('Butter Chicken', 'Tender chicken cooked in a creamy tomato-based sauce with aromatic spices.', 156),
('Biryani', 'Fragrant basmati rice cooked with marinated chicken or lamb, spices, and herbs.', 120);

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `iid` int(11) NOT NULL,
  `iname` varchar(11) NOT NULL,
  `quantity` varchar(11) NOT NULL,
  `eid` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`iid`, `iname`, `quantity`, `eid`) VALUES
(1, 'Chicken', '20 units', 0),
(2, 'Milk', '10 liter', 0),
(3, 'Eggs', '35', 0),
(4, 'Pasta ', '5 kg', 0),
(5, 'Cheese', '8 kg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `ouname` varchar(255) DEFAULT NULL,
  `ofname` varchar(255) DEFAULT NULL,
  `odate` date NOT NULL DEFAULT curdate(),
  `otime` time NOT NULL DEFAULT curtime(),
  `oprice` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`ouname`, `ofname`, `odate`, `otime`, `oprice`) VALUES
('palak', 'Butter Chicken', '2024-03-03', '15:11:59', 156),
('palak', 'Tacos', '2024-03-03', '15:11:59', 99),
('kanisha', 'Pizza', '2024-03-09', '13:49:58', 320),
('kanisha', 'Tacos', '2024-03-09', '13:49:58', 99),
('prajwal', 'Pizza', '2024-03-09', '14:05:18', 320),
('prajwal', 'Tacos', '2024-03-09', '14:05:19', 99);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `pid` int(11) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `pdate` date NOT NULL DEFAULT current_timestamp(),
  `ptype` varchar(255) NOT NULL,
  `amount` int(11) NOT NULL,
  `status` varchar(20) DEFAULT 'PENDING'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pid`, `pname`, `pdate`, `ptype`, `amount`, `status`) VALUES
(15, 'palak', '2024-03-03', 'online', 255, 'Delivered'),
(19, 'kanisha', '2024-03-09', 'cash', 418, 'Delivered'),
(20, 'prajwal', '2024-03-09', 'cash', 417, 'Delivered');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `table_no` int(11) DEFAULT NULL,
  `uname` varchar(255) NOT NULL,
  `uphone` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`table_no`, `uname`, `uphone`) VALUES
(5, 'kanisha', '479340385'),
(1, 'palak', '7975783131'),
(3, 'prajwal', '47934885');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`eid`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`iid`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uname`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `iid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
