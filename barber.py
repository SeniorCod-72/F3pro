from sqlalchemy import Column, Integer, String, create_engine, 
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)



class customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)


