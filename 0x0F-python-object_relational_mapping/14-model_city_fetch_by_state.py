#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create a SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}'
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and order them by id
    cities = session.query(City).order_by(City.id).all()

    # Print the results in the format: <state name>: (<city id>) <city name>
    for city in cities:
        state_name = city.state.name
        city_id = city.id
        city_name = city.name
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    # Close the session
    session.close()
