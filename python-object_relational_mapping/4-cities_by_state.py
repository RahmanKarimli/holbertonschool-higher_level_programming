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
        query = """SELECT c.id, c.name, s.name FROM cities c
                    INNER JOIN states s ON c.state_id = s.id
                    ORDER BY c.id"""
        cur.execute(query)
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for row in rows:
        print(row)
    cur.close()
    db.close()
