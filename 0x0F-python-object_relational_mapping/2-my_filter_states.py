#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument in a case-sensitive manner.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Extract command-line arguments
    username, password, database, search_name = sys.argv[1:]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Create the SQL query with user input using format and case-sensitive COLLATE
    query = (
        "SELECT * FROM states "
        "WHERE name COLLATE utf8_bin = '{}' "
        "ORDER BY id ASC"
    ).format(search_name)

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
