#!/usr/bin/python3
'''
model class for cites
'''
from sqlalchemy import Column, create_engine, column, String, Integer, \
    VARCHAR, Nullable, ForeignKey
from relationship_state import Base


class City(Base):

    '''
    city class which inhert from base class

    attributes:
    id
    name
    state_id
    '''

    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
