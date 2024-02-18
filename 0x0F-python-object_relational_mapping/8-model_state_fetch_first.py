#!/usr/bin/python
"""
Script that prints the first State object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = \
        create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                      sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    state_list = session.query(State).order_by(State.id).first()

    if state_list:
        print('{}: {}'.format(state_list.id, state_list.name))
    else:
        print('Nothing')
    session.close()
