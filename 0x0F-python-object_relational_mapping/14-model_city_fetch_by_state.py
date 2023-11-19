#!/usr/bin/python3
"""
A script that prints all City objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

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

    query = session.query(City, State).join(State)

    for _city, _state in query.all():
        print('{}: ({:d}) {}'.format(_state.name, _city.id, _city.name))
    session.commit()
    session.close()
