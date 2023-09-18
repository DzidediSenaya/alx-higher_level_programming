#!/usr/bin/python3
"""
Script that displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
(safe from SQL injection).
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use a parameterized query to safely retrieve
    # states matching the provided argument
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"

    # Execute the query with the parameter
    cursor.execute(query, (state_name,))

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close cursor and database connections
    cursor.close()
    db.close()
