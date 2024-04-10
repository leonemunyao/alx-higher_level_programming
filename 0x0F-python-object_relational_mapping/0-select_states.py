#!/usr/bin/python3
"""Python Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Get command line arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connect to MySQL server"""
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password, db=database
        )

    """Create a cursor object"""
    cursor = db.cursor()

    """Execute the query"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all the rows"""
    rows = cursor.fetchall()

    """Print the results"""
    for row in rows:
        print(row)

    """Close the cursor and database connection"""
    cursor.close()
    db.close()
    
