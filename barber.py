from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship,sessionmaker
from sqlalchemy import DateTime
from datetime import datetime 



Base = declarative_base()


class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    

    appointments = relationship('Appointment', back_populates='barber')




class Customer(Base):
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
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)


    barber = relationship('Barber', back_populates='appointments')
    customer = relationship('Customer', back_populates='appointments')


# engine = create_engine('sqlite:///bssm.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
#session = Session()