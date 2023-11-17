#!/usr/bin/python3
"""This script lists all cities in a state from the database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    name = sys.argv[3]
    uname = sys.argv[1]
    pwd = sys.argv[2]
    user_input = sys.argv[4]
    host = "localhost"
    s_port = 3306
    my_query = "SELECT name FROM cities WHERE state_id = (SELECT id\
        FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id ASC"
    parameters = (user_input,)

    db = MySQLdb.connect(
        host=host, user=uname, passwd=pwd, db=name, port=s_port
    )

    cursor = db.cursor()
    cursor.execute(my_query, parameters)

    states_tuple = ()  # to hold the cities from the state

    complete_data = cursor.fetchall()

    for data in complete_data:
        state_tuple = state_tuple + data

    print(*states_tuple, sep=", ")

    cursor.close()
    db.close()
