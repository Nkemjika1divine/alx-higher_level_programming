#!/usr/bin/python3
"""This finds a state occurrence in a database in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    name_of_state = sys.argv[4]
    with engine.connect() as connection:
        query = select(State).where(State.name == name_of_state)
        states = connection.execute(query).first()
        if states:
            print(states.id)
        else:
            print("Not found")

    engine.dispose()
