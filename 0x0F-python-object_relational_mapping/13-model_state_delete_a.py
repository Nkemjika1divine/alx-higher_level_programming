#!/usr/bin/python3
"""This finds a states in a database that has a in them
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
    deleteStates = session.query(State).filter(State.name.like(f'%a%')).all()
    if deleteStates:
        for state in deleteStates:
            session.delete(state)
        session.commit()

    # delete() is used to delete data after querying
