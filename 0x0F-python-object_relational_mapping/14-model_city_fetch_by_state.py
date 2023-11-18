#!/usr/bin/python3
"""This finds a states in a database that has a in them
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from model_city import City
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
    result = session.query(City, State).\
        join(State, State.id == City.state_id).all()
    if result:
        for city, state in result:
            print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
