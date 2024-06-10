-- Create the database
CREATE DATABASE QUIZZ;

-- Use the database
USE QUIZZLY;
SELECT @@SERVERNAME
-- Create the Questions table
CREATE TABLE Library (
    ID INT PRIMARY KEY ,
    Question TEXT NOT NULL,
    Answer_A TEXT NOT NULL,
    Answer_B TEXT NOT NULL,
    Answer_C TEXT NOT NULL,
    Answer_D TEXT NOT NULL,
    Correct_Answer CHAR(1) NOT NULL
);
-- Insert sample questions into the Questions table
INSERT INTO Library (ID, Question, AnsA, AnsB, AnsC, AnsD, CorrectAns) VALUES
('1','What is the capital of France?', 'Berlin', 'Madrid', 'Paris', 'Rome', 'C'),
('2','Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'B'),
('3','What is the largest ocean on Earth?', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean', 'D'),
('4','Who wrote "To Kill a Mockingbird"?', 'Harper Lee', 'J.K. Rowling', 'Jane Austen', 'Mark Twain', 'A'),
('5','What is the chemical symbol for gold?', 'Au', 'Ag', 'Pb', 'Fe', 'A'),
('6','Which element has the atomic number 1?', 'Helium', 'Oxygen', 'Hydrogen', 'Nitrogen', 'C'),
('7','Who painted the Mona Lisa?', 'Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet', 'C'),
('8','What is the smallest country in the world?', 'Monaco', 'Vatican City', 'San Marino', 'Liechtenstein', 'B'),
('9','In what year did the Titanic sink?', '1910', '1912', '1914', '1916', 'B'),
('10','What is the powerhouse of the cell?', 'Nucleus', 'Ribosome', 'Mitochondria', 'Endoplasmic Reticulum', 'C');

DELETE FROM Library;
-- Select all records from the Questions table
SELECT * FROM Library;
