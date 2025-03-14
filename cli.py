from barber import Barber,Customer, Appointment,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

my_db_url = "sqlite:///bssm.db"
engine = create_engine(my_db_url)
session = sessionmaker(bind=engine)
session = session()

def add_barber():
    """Add a new Barber"""
    name = input("Enter barbers's name")
    phone =
    
    