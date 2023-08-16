-- List all records of the table second_table ordered by score (top first)
USE %s;
SELECT score, name FROM second_table ORDER BY score DESC;
