from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import DateTime
from sqlalchemy import datetime 



Base = declarative_base()


class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)

    appointments = relationship('Appointment', back_populates='barber')




class customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)

    appointments = relationship('Appointment', back_populates='customer')



class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    barber_id = Column(Integer, ForeignKey('barbers.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)


    