#!/usr/bin/python3

'''
script to add new model cities
'''

from model_city import City
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base

if __name__ == '__main__':
    engine = \
        create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                      argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = State(name='California')
    city = City(name='San Francisco')

    state.cities.append(city)
    session.add(state)
    session.commit()
    session.close()
