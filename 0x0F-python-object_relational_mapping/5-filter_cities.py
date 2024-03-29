#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check and validate command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password>"
              .format(sys.argv[0]))
        print("       <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute the SQL query to fetch cities of the given state
    query = (
        "SELECT cities.name FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name=%s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row[0])

    # Close the cursor and database connection
    cursor.close()
    db.close()
