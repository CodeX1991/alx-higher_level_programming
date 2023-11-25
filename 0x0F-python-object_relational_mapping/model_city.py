#!/usr/bin/python3
"""
A python file that contains the class definition of a State
and an instance Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """City class


    Attributes:
        __tablename__(str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
