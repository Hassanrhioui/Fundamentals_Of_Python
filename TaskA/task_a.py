from datetime import datetime

def main():
    with open("reservations.txt", "r") as file: # we open the reservations.txt file in read mode
        reservation = file.readline().strip() # we read the first line of the file and remove any leading/trailing whitespace


# we use "|" to split the reservation string into a list
    reservation = reservation.split("|")
    
# theses variables are using elements from the reservation list that is in reservations.txt
# each element is separated by a "|"
# each is stored in an indexed position in the list
    reservation_number = int(reservation[0])
# we use int() to convert the reservation number from string to integer
    booker = reservation[1]

#we use datetime.strptime() to convert the date and time strings into date and time objects

    date = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    time = datetime.strptime(reservation[3], "%H:%M").time()

    hours = int(reservation[4])
    hourly_price = float(reservation[5])
    paid = reservation[6] == "True" # it checks payment is done or not

    location = reservation[7]
    phone = reservation[8]
    email = reservation[9]

    total_price = hours * hourly_price

    print(f"Reservation number: {reservation_number}")
    print(f"Booker: {booker}")
    print(f"Date: {date.strftime('%d.%m.%Y')}")
    print(f"Start time: {time.strftime('%H.%M')}")
    print(f"Number of hours: {hours}")
    print(f"Hourly price: {hourly_price:.2f}".replace(".", ",") + " €")
    print(f"Total price: {total_price:.2f}".replace(".", ",") + " €")
    print(f"Paid: {'Yes' if paid else 'No'}")
    print(f"Location: {location}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

if __name__ == "__main__":
    main()
