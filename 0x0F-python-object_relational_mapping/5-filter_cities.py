#!/usr/bin/python3
"""
This script lists all cities of a given state from the hbtn_0e_4_usa database.
Usage: <mysql username> <mysql password> <database name> <state name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (sys.argv[4],))

    cities = [city[0] for city in cur.fetchall()]
    print(", ".join(cities))

    cur.close()
    db.close()
