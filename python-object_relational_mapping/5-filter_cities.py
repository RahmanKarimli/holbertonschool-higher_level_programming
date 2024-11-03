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

    query = """SELECT cities.id, cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;"""

    cur.execute(query, (argv[4],))
    rows = cur.fetchall()

    city_names = ", ".join([row[1] for row in rows])
    print(city_names)

    cur.close()
    db.close()
