#!/usr/bin/python3
"""
A script taht lists all State objects from
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

    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
