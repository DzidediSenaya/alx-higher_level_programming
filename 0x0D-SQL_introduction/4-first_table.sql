-- Create a table called first_table in the specified database
USE %s;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
