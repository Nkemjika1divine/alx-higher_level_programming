#!/usr/bin/python3
"""This finds a state occurrence in a database in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        transaction = connection.begin()
        query = insert(State).values(name="Louisiana")
        connection.execute(query)
        query = select(State).where(State.name == "Louisiana")
        state = connection.execute(query).fetchone()
        if state:
            print(state.id)
        transaction.commit()

    engine.dispose()

    """ begin() is used to start a transaction/session within a database
    In these sessions, you can update or modify contents to a database
    commit() is used to commit the changes to the database
    """
