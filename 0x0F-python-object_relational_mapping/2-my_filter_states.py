#!/usr/bin/python3

"""Python script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where name
    matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    """ Connect to MySQL server """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    """ Create a cursor object """
    cursor = db.cursor()

    """ Execute the SQL query """
    query = f"SELECT * FROM states WHERE name = '{state_name}' ORDER BY id ASC"
    cursor.execute(query)

    """ Fetch all the rows and print them """
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """ Close the cursor and database connection """
    cursor.close()
    db.close()
