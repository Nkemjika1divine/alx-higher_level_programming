#!/usr/bin/python3
"""This links a class to a table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    """The create_engine method creates a connection to the database.
    It takes some parameters, a link to the database and some other parameters
    -> pool_pre_ping pings the database to know if the connection exists.
    If the connection doesn't exist, it creates the connection
    -> Base.metadata.create_all establishes the operation
    Base.metadata.create_all(engine)
    """
