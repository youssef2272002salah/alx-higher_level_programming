#!/usr/bin/python3
'''
model class for city
'''
from sqlalchemy import Column, create_engine,column,String,Integer,VARCHAR,Nullable,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base
from model_state import Base



class City(Base):
    __tablename__="cities"
    id = Column('id',Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128),nullable =False)

    state_id = Column(Integer,ForeignKey('states.id'),nullable=False)
