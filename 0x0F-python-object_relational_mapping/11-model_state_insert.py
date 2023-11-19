#!/usr/bin/python3
"""
A script taht add State objects Lousiana to
the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    """
    Access to the database and get the statess
    from the database
    """

    db_uri = 'mysql://{}:{}@localhost:3306/{}'.format(argv[1],
                                                      argv[2], argv[3])

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_name = State(name='Louisiana')
    session.add(state_name)
    session.commit()
    print('{}'.format(state_name.id))
    session.close()
