-- List all records with a score >= 10 in the table second_table ordered by score (top first)
USE %s;
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
