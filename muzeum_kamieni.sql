-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 18 Mar 2022, 23:58
-- Wersja serwera: 10.4.22-MariaDB
-- Wersja PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `muzeum_kamieni`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `ceny`
--

CREATE TABLE `ceny` (
  `id` int(11) NOT NULL,
  `waluta` varchar(50) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `skrot_nazwy` varchar(10) NOT NULL,
  `kurs` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `kamienie`
--

CREATE TABLE `kamienie` (
  `id` int(11) NOT NULL,
  `Gatunek` varchar(150) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `Rocznik` date NOT NULL,
  `Kraj_id` int(11) NOT NULL,
  `Kolor` varchar(50) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `Wielkosc` double NOT NULL,
  `Waga` float NOT NULL,
  `Opis` varchar(500) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `klienci`
--

CREATE TABLE `klienci` (
  `id` int(11) NOT NULL,
  `typ_biletu` varchar(100) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `cena_id` int(11) NOT NULL,
  `potrzebny_dowod` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `kraj`
--

CREATE TABLE `kraj` (
  `id` int(11) NOT NULL,
  `Panstwo` varchar(100) NOT NULL,
  `Kontynent` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `muzeum`
--

CREATE TABLE `muzeum` (
  `id` int(11) NOT NULL,
  `Kamienie_id` int(11) NOT NULL,
  `Klienci_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `ceny`
--
ALTER TABLE `ceny`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `kamienie`
--
ALTER TABLE `kamienie`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Kraj_id` (`Kraj_id`);

--
-- Indeksy dla tabeli `klienci`
--
ALTER TABLE `klienci`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cena_id` (`cena_id`);

--
-- Indeksy dla tabeli `kraj`
--
ALTER TABLE `kraj`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `muzeum`
--
ALTER TABLE `muzeum`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Kamienie_id` (`Kamienie_id`),
  ADD KEY `Klienci_id` (`Klienci_id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `ceny`
--
ALTER TABLE `ceny`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `kamienie`
--
ALTER TABLE `kamienie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `klienci`
--
ALTER TABLE `klienci`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `kraj`
--
ALTER TABLE `kraj`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `muzeum`
--
ALTER TABLE `muzeum`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `kamienie`
--
ALTER TABLE `kamienie`
  ADD CONSTRAINT `kamienie_ibfk_1` FOREIGN KEY (`Kraj_id`) REFERENCES `kraj` (`id`);

--
-- Ograniczenia dla tabeli `klienci`
--
ALTER TABLE `klienci`
  ADD CONSTRAINT `klienci_ibfk_1` FOREIGN KEY (`cena_id`) REFERENCES `ceny` (`id`);

--
-- Ograniczenia dla tabeli `muzeum`
--
ALTER TABLE `muzeum`
  ADD CONSTRAINT `muzeum_ibfk_1` FOREIGN KEY (`Kamienie_id`) REFERENCES `kamienie` (`id`),
  ADD CONSTRAINT `muzeum_ibfk_2` FOREIGN KEY (`Klienci_id`) REFERENCES `klienci` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
