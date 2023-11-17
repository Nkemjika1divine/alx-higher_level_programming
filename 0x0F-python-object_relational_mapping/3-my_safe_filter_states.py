#!/usr/bin/python3
"""This script lists all Arizona states from the database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    name = sys.argv[3]
    uname = sys.argv[1]
    pwd = sys.argv[2]
    user_input = sys.argv[4]
    host = "localhost"
    s_port = 3306
    q = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    parameters = (user_input,)

    db = MySQLdb.connect(
        host=host, user=uname, passwd=pwd, db=name, port=s_port
    )

    cursor = db.cursor()
    cursor.execute(q, parameters)

    complete_data = cursor.fetchall()

    for data in complete_data:
        print(data)

    cursor.close()
    db.close()
