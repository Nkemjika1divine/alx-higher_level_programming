#!/usr/bin/python3
"""This script lists all states starting with "N" from the database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    name = sys.argv[3]
    uname = sys.argv[1]
    pwd = sys.argv[2]
    ui = sys.argv[4]
    host = "localhost"
    s_port = 3306
    q = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY id ASC".format(ui)

    db = MySQLdb.connect(
        host=host, user=uname, passwd=pwd, db=name, port=s_port
    )

    cursor = db.cursor()
    cursor.execute(q)

    complete_data = cursor.fetchall()

    for data in complete_data:
        print(data)

    cursor.close()
    db.close()
