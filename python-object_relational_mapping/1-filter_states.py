#!/usr/bin/python3
"""
SQL
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()
    try:
        cursor.execute("""SELECT * FROM states WHERE name LIKE "N%" ORDER BY id""")
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for i in rows:
        print(i)
    cursor.close()
    db.close()
