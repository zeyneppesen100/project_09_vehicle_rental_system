from vehicles import (add_vehicle, update_vehicle, set_vehicle_status, list_available_vehicles)
from customers import (load_customers, save_customers, register_customer,authenticate_customer,update_customer_profile, add_customer)
from reservations import (create_reservation, complete_rental, cancel_reservation, check_availability, calculate_invoice)
from reports import (utilization_report,revenue_summary,upcoming_returns, export_report)
from storage import (load_state, save_state, backup_state)

DATA = "data"
BACKUP = "backups"
def main():
    vehicles, customers, reservations = load_state(DATA)
    print("\n--- Vehicle Rental System ---")
    print("1. Add vehicle")
    print("2. Add customer")
    print("3. Create reservation")
    print("4. Complete rental (check-in)")
    print("5. Reports")
    print("6. Backup data")
    print("0. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        make = input("Make: ")
        model = input("Model: ")
        rate = float(input("Rate per day: "))

        vehicle = add_vehicle(vehicles, make, model, rate)
        print("Added vehicle:", vehicle)

    elif choice == "2":
        name = input("Customer name: ")
        email = input("Email: ")

        customer = add_customer(customers, name, email)
        print("Added customer:", customer)

    elif choice == "3":
        vehicle_id = input("Vehicle ID: ")
        customer_id = input("Customer ID: ")
        start = input("Start date (YYYY-MM-DD): ")
        end = input("End date (YYYY-MM-DD): ")
        try:
            reservation = create_reservation(
                reservations,
                vehicles,
                vehicle_id,
                customer_id,
                start,
                end
            )
            print("Reservation created:", reservation)
        except ValueError:
            print("Error:")
            
    elif choice == "4":
        res_id = input("Reservation ID: ")
        odometer = int(input("Return odometer: "))
        fuel = input("Fuel level (full/half/empty): ")
        damage = input("Any damages? (yes/no): ").lower() == "yes"
        try:
            completed = complete_rental(
                reservations,
                res_id,
                {
                    "return_odometer": odometer,
                    "fuel_level": fuel,
                    "damages": damage
                },
                vehicles
            )
            print("Rental completed.")
            print("Invoice:", completed["invoice"])
        except Exception as e:
            print("Error:", e)

    elif choice == "5":
        print("\n--- Reports ---")
        print("1. Utilization")
        print("2. Revenue")
        print("3. Upcoming returns")
        r_choice = input("Choose report: ")
        if r_choice == "1":
            start = input("Start date: ")
            end = input("End date: ")
            report = utilization_report(reservations, vehicles, (start, end))
            print(report)
        elif r_choice == "2":
            start = input("Start date: ")
            end = input("End date: ")
            report = revenue_summary(reservations, (start, end))
            print(report)
        elif r_choice == "3":
            ref = input("Reference date: ")
            report = upcoming_returns(reservations, ref)
            print(report)
    elif choice == "6":
        backups = backup_state(DATA, BACKUP)
        print("Backup created:")
        for b in backups:
            print("-", b)

    elif choice == "0":
        save_state(DATA, vehicles, customers, reservations)
        

    else:
        print("Invalid")
if __name__ == "__main__":
    main()
