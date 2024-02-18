#!/usr/bin/python3
"""
The class definition of a State
"""
from sqlalchemy import create_engine, Column, String, Integer, VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class State(Base):
    """
    Create the Class State
    """
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(128), nullable=False)