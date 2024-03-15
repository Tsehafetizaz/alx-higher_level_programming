#!/usr/bin/python3
"""
Definition of the State model with a relationship to the City model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    The State class corresponds to the states table in the database
    and includes a relationship to the City class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
