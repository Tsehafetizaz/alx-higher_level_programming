import MySQLdb
import sys

if __name__ == "__main__":

    # Handle potential errors gracefully
    try:
        if len(sys.argv) != 5:
            raise ValueError("Usage: python script_name.py <username> <password> <state_name>")

        db = MySQLdb.connect(host="localhost",
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        cur = db.cursor()

        # Use parameterized query for security
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (sys.argv[4],))  # Tuple for single parameter

        for row in cur.fetchall():
            if row[1].lower() == sys.argv[4].lower():  # Case-insensitive comparison
                print(row)

        cur.close()
        db.close()

    except (ValueError, MySQLdb.Error) as e:
        print(f"Error: {e}")
