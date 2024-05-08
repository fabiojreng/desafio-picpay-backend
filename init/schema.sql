CREATE DATABASE IF NOT EXISTS picpay;

CREATE TABLE IF NOT EXISTS `picpay`.`users`(
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    registration_number VARCHAR(100) NOT NULL,
    user_type VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS `picpay`.`transactions`(
    id VARCHAR(50) PRIMARY KEY,
    payer VARCHAR(100) NOT NULL,
    payee VARCHAR(100) NOT NULL,
    value DECIMAL(10, 2) NOT NULL
);
