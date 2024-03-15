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
    State class:
    - Inherits from Base (declarative_base()).
    - Links to the MySQL table states.
    - Attributes:
        - id: Integer, primary key, autoincremented, can't be null.
        - name: String (128 characters), can't be null.
        - cities: Relationship with the City class, cascade deletion.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
