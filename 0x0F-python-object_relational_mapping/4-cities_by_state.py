#!/usr/bin/python3
"""This script lists all states from the cities table in the database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    name = sys.argv[3]
    uname = sys.argv[1]
    pwd = sys.argv[2]
    host = "localhost"
    s_port = 3306
    my_query = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON states.id = cities.state_id\
            ORDER BY cities.id"

    db = MySQLdb.connect(
        host=host, user=uname, passwd=pwd, db=name, port=s_port
    )

    cursor = db.cursor()
    cursor.execute(my_query)

    complete_data = cursor.fetchall()

    for data in complete_data:
        print(data)

    cursor.close()
    db.close()
