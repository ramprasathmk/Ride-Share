-- DATABASE `ridesharing` Creation
CREATE DATABASE ridesharing;

-- Using `ridesharing` Database
use ridesharing;

-- TABLE `users` Creation
CREATE TABLE users (
    Id INT(3) UNSIGNED AUTO_INCREMENT,
    Name VARCHAR(20) NOT NULL,
    Phone Bigint(10) NOT NULL UNIQUE,
    -- Age int(3) NOT NULL,
    DOB DATE NOT NULL,
    Address VARCHAR(30) NOT NULL,
    City VARCHAR(15) NOT NULL,
    Email VARCHAR(20) NOT NULL UNIQUE,
    Username VARCHAR(15) NOT NULL UNIQUE,
    Password VARCHAR(15) NOT NULL UNIQUE,
    PRIMARY KEY(Id)
);