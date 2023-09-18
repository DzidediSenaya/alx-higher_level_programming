#!/usr/bin/python3
"""
Script that lists all states with a name starting with
N from the database hbtn_0e_0_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    session = Session(engine)

    # Query all states starting with 'N'
    states = (
        session.query(State)
        .filter(State.name.like('N%'))
        .order_by(State.id)
        .all()
    )

    # Print the IDs and names of the matching states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
