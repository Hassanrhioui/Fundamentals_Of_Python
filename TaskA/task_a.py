# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Hassan Rhioui according to given task


from datetime import datetime


def main():
    # Read one reservation line from the file
    with open("reservations.txt", "r") as file:
        reservation = file.readline().strip()

    # Reservation number
    reservation_id = int(reservation.split("|")[0])
    print("Reservation number:", reservation_id)

    # Booker name
    booker = reservation.split("|")[1]
    print("Booker:", booker)

    # Date (convert from string to date)
    day = datetime.strptime(
        reservation.split("|")[2], "%Y-%m-%d"
    ).date()
    print("Date:", day.strftime("%d.%m.%Y"))

    # Time (convert from string to time)
    time = datetime.strptime(
        reservation.split("|")[3], "%H:%M"
    ).time()
    print("Start time:", time.strftime("%H.%M"))

    # Number of hours
    hours = int(reservation.split("|")[4])
    print("Number of hours:", hours)

    # Hourly price
    hourly_price = float(reservation.split("|")[5])
    print(
        "Hourly price:",
        f"{hourly_price:.2f}".replace(".", ","),
        "€"
    )

    # Total price
    total_price = hours * hourly_price
    print(
        "Total price:",
        f"{total_price:.2f}".replace(".", ","),
        "€"
    )

    # Payment status
    paid = reservation.split("|")[6] == "True"
    print("Paid:", "Yes" if paid else "No")

    # Location
    location = reservation.split("|")[7]
    print("Location:", location)

    # Phone number
    phone = reservation.split("|")[8]
    print("Phone:", phone)

    # Email
    email = reservation.split("|")[9]
    print("Email:", email)


if __name__ == "__main__":
    main()

