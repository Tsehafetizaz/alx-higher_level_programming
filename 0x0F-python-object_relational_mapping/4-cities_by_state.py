#!/usr/bin/python3
"""
This script lists all cities from the hbtn_0e_4_usa database.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
