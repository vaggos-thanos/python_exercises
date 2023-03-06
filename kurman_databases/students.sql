CREATE TABLE students (
id INT PRIMARY KEY,
scorel INT NOT NULL,
score2 INT NOT NULL
);

INSERT INTO students VALUES (1,12,13);
INSERT INTO students VALUES (2,13,14);
INSERT INTO students VALUES (3,14,15); 
INSERT INTO students VALUES (4,15,16);
INSERT INTO students VALUES (5,16,17);

UPDATE students SET scorel=5, score2=8 WHERE id = 1;
UPDATE students SET scorel = 10, score2 = 8 WHERE id=2; 
UPDATE students SET scorel = 8, score2=3 WHERE id = 3;
UPDATE students SET scorel = 10, score2 = 7 WHERE id = 4;
UPDATE students SET scorel = 10, score2 = 7 WHERE id = 5;

select * from students
