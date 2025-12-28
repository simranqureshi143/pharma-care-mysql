CREATE DATABASE pharmacare;
USE pharmacare;

CREATE TABLE medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DOUBLE,
    description VARCHAR(255)
);
