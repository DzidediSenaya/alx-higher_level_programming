-- List all records of the table second_table with a name value, ordered by descending score
USE %s;
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
