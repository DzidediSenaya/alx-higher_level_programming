#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check for the correct number of command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
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

        # Execute the query to retrieve states starting with 'N' (uppercase)
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE 'N%' COLLATE utf8_bin "
            "ORDER BY id"
        )
        cursor.execute(query)

        # Fetch all the results
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    finally:
        # Close cursor and database connections
        cursor.close()
        db.close()
