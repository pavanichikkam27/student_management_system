CREATE DATABASE student_db;
USE student_db;

CREATE TABLE students (
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(5)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
);

INSERT INTO users (username, password)
VALUES ('pavani', 'admin275@');
