#!/usr/bin/python3
"""
This script displays values in the states table where name
Usage: ./2-my_filter_states.py <mysql username>
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
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC").format(sys.argv[4])
    cur.execute(query)

    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)

    cur.close()
    db.close()
