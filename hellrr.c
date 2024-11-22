NAME :farman ali
ROLL_NO:23BSAI49
    -- Q#1: 
CREATE DATABASE IF NOT EXISTS University;


-- Q#2: 
USE University;


-- Q#3: 
CREATE TABLE IF NOT EXISTS Student (
    Roll_No CHAR(10),
    Name VARCHAR(20),
    Address VARCHAR(50),
    Age INT,
    Department VARCHAR(30)
);

-- Q#4: 

INSERT INTO Student (Roll_No, Name, Address, Age, Department)
VALUES 
('23IT31', 'ALI MAGSI', 'lahore', 20, 'Computer Science'),
('23EE41', 'MUHAMMMAD MAGSI', 'hyd', 22, 'Electrical Engineering'),
('23ME61', 'AKBAR  MAGSI', 'sakrand', 21, 'Mechanical Engineering');


-- Q#5: 
ALTER TABLE Student
ADD COLUMN F_Name VARCHAR(20);


-- Q#6: 
ALTER TABLE Student
MODIFY COLUMN Roll_No VARCHAR(10);


-- Q#7:
ALTER TABLE Student
DROP COLUMN F_Name;


-- Q#8:

-- a_part
UPDATE Student
SET Address = 'Larkana'
WHERE Roll_No = '11IT02';

-- b_part
DELETE FROM Student
WHERE Roll_No = '11EE01';

-- c_part
UPDATE Student
SET Address = 'Nawabshah', Department = 'ME';

-- d_part
DROP TABLE IF EXISTS Student;

-- e_part
DROP DATABASE IF EXISTS University;