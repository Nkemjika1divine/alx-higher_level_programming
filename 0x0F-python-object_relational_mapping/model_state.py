#!/usr/bin/python3
"""model state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ This is a State class inheriting from Base """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    """First you import the sqlalchemy module and then you import th necessary
    tools needed for the table you wantto create eg Column, Integer, etc...
    Thrn you import declarative_base from sqlalchemy.ext.declarative
    It will be used to creatr thr table class
    """
