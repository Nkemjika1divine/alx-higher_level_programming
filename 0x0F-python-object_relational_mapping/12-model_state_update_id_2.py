#!/usr/bin/python3
"""This finds a state occurrence in a database in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    updateState = session.query(State).filter_by(id=2).first()

    if updateState:
        updateState.name = 'New Mexico'
    session.commit()
    session.close()

    """sessionmaker(bind=engine) is used to initiate a session.
    It is also used to create the class Session() which is used for operations
    commit() is used to commit changes to database
    close() is used to close the session
    """
