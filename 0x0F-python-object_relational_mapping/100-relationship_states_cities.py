#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
in the database hbtn_0e_100_usa.
Usage: ./100-rel<mysql password> <database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Create an engine and bind it to the database
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State "California" with one associated City "San Francisco"
    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]

    # Add the new State with its City to the session and commit to the database
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
