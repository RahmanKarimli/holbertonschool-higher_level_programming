#!/usr/bin/python3
"""
Connecting to database and safely listing states
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()

    try:
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (argv[4],))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for row in rows:
        print(row)
    cur.close()
    db.close()
