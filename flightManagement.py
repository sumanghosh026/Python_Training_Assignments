# Custom Exceptions
class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass

try:
    # Outer try: File handling
    f = open("exception_handling/flight.txt", "r")

    # Load flights into a dictionary
    flights = {}
    for line in f:
        flight_number, seats, price = line.strip().split()
        flights[flight_number] = {"seats": int(seats), "price": int(price)}

    # User inputs
    flight_no = input("Enter Flight Number: ")

    try:
        # Inner try: Booking operations

        if flight_no not in flights:
            raise FlightNotFoundError(f"Flight {flight_no} does not exist!")

        num_tickets = int(input("Enter number of tickets to book: "))

        # Check seats
        if num_tickets > flights[flight_no]["seats"]:
            raise SeatsUnavailableError("Requested seats exceed available seats!")

        # Calculate cost
        total_cost = flights[flight_no]["price"] * num_tickets

        # Discount per ticket (may cause ZeroDivisionError)
        discount = total_cost / num_tickets

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

    except SeatsUnavailableError as e:
        print("Custom Exception:", e)

    except FlightNotFoundError as e:
        print("Custom Exception:", e)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be zero!")

    else:
        # If no exception occurred
        print("Flight:", flight_no)
        print("Tickets Booked:", num_tickets)
        print("Price per Ticket:", flights[flight_no]["price"])
        print("Total Cost:", total_cost)
        print("Discount per Ticket:", discount)

except FileNotFoundError:
    print("Error: flights.txt file not found!")

finally:
    try:
        f.close()
        print("\nFile closed successfully.")
    except:
        print("\nFile could not be closed (maybe it never opened).")
