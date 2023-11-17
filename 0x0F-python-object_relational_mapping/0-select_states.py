#!/usr/bin/python3
"""This script lists all states from the database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    name = sys.argv[3]
    uname = sys.argv[1]
    pwd = sys.argv[2]
    host = "localhost"
    port = 3306
    my_query = "SELECT * FROM states ORDER BY id ASC"

    db = MySQLdb.connect(host=host, user=_name, passwd=pwd, db=name, port=port)

    cursor = db.cursor()
    cursor.execute(my_query)

    complete_data = cursor.fetchall()

    for data in complete_data:
        print(data)

    cursor.close()
    db.close()
