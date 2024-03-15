#!/usr/bin/python3
"""
Defines a State model that inherits from Base = declarative_base():
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Representation of a state for the SQL table states.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
