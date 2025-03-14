from barber import Barber, Customer, Appointment, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

bssm_url = "sqlite:///bssm.db"
engine = create_engine(bssm_url)
Session = sessionmaker(bind=engine)
session = Session()

def add_barber():
    """Add a new barber"""
    name = input("Enter barber's name: ")
    phone = input("Enter barber's phone number: ")
    specialization = input("Enter barber's specialization (e.g., Haircut, Shave): ")
    years_of_experience = int(input("Enter num1ber of years of experience: "))
    status = input("Enter barber's status (Available, Not Available): ")

    barber = Barber(name=name, phone=phone, specialization=specialization,
                    years_of_experience=years_of_experience, status=status)
    session.add(barber)
    session.commit()
    print(f"Added barber: {name}, Specialization: {specialization}, Experience: {years_of_experience} years, Status: {status}")

def add_customer():
    """Add a new customer"""
    name = input("Enter customer's name: ")
    phone = input("Enter customer's phone number: ")

    customer = Customer(name=name, phone=phone)
    session.add(customer)
    session.commit()
    print(f"Added customer: {name}")

def create_appointment():
    """Create a new appointment"""
    barber_name = input("Enter barber's name: ")
    customer_name = input("Enter customer's name: ")
    date_time_str = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")

    barber = session.query(Barber).filter_by(name=barber_name).first()
    customer = session.query(Customer).filter_by(name=customer_name).first()

    if barber and customer:
        appointment = Appointment(barber=barber, customer=customer, date_time=date_time)
        session.add(appointment)
        session.commit()
        print(f"Created appointment for {customer_name} with {barber_name} on {date_time}")
    else:
        print("Barber or Customer not found. Please check the details.")

def list_barbers():
    """List all barbers"""
    barbers = session.query(Barber).all()
    if barbers:
        for barber in barbers:
            print(f"Barber: {barber.name}, Phone: {barber.phone}, Specialization: {getattr(barber, 'specialization', 'N/A')}, "
                  f"Experience: {getattr(barber, 'years_of_experience', 'N/A')} years, Status: {getattr(barber, 'status', 'N/A')}")
    else:
        print("No barbers found.")

def list_appointments():
    """List all appointments"""
    appointments = session.query(Appointment).all()
    if appointments:
        for appointment in appointments:
            print(f"Appointment for {appointment.customer.name} with {appointment.barber.name} on {appointment.date_time}")
    else:
        print("No appointments found.")

def main():
    """Main menu for the Barber Shop System Management"""
    while True:
        print("\n--- Barber Shop System Management ---")
        print("1. Add Barber")
        print("2. Add Customer")
        print("3. Create Appointment")
        print("4. List Barbers")
        print("5. List Appointments")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_barber()
        elif choice == '2':
            add_customer()
        elif choice == '3':
            create_appointment()
        elif choice == '4':
            list_barbers()
        elif choice == '5':
            list_appointments()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
