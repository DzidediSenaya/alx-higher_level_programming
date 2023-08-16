-- Compute the average score of all records in the table second_table
USE %s;
SELECT AVG(score) AS average FROM second_table;
