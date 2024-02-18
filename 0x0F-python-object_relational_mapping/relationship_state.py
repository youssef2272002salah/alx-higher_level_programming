#!/usr/bin/python3

"""
The class definition of a State
"""

from sqlalchemy import create_engine, Column, String, Integer, VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()


class State(Base):

    """
    state class that inherits from Base

    Attributes:
        id: Id of states
        name: Name of the states
    """

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state'
                          )
