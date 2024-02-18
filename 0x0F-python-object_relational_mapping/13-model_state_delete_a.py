#!/usr/bin/python3
'''
script to delet old record"""  """
'''

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

    state_update = session.query(State).filter(State.name.like('%a%')).all()
    for delete in state_update:
        session.delete(delete)
    session.commit()
    state_list = session.query(State).order_by(State.id).all()
    for i in state_list:
        print('{}: {}'.format(i.id, i.name))
    session.close()
