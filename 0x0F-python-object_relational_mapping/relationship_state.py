#!/usr/bin/python3
"""
A python file that contains the class definition of a State
and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """States class


    Attributes:
        __tablename__(str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")