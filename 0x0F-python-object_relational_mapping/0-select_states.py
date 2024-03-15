#!/usr/bin/python3
"""
This script lists all states from the hbtn_0e_0_usa database.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
