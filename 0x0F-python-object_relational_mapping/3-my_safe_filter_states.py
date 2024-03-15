#!/usr/bin/python3
"""
This script is safe from MySQL injections when displaying state values.
Usage:  <mysql username> <mysql password> <database name> <state name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
