#!/usr/bin/python3
"""This links a class to a table in database
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
    with engine.connect() as connection:
        query = select(State).order_by(State.id.asc())
        states = connection.execute(query)
        for state in states:
            print(f"{state.id}: {state.name}")

    engine.dispose()

    """ connect() is used to establish a connection.
    The connection is then used to execute the query using execute()
    dispose() is used to ensure that the total connection is closed
    """
