#!/usr/bin/python3
'''
script to add new model cities
'''

from model_city import City
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = \
        create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                      argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    list = session.query(State,
                         City).join(City).order_by(State.id).all()

    for (state, city) in list:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
