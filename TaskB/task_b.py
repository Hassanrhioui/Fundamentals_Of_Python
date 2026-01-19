# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Hassan Rhioui according to given task


from datetime import datetime


def print_reservation_number(reservation: list) -> None:
    """
    Prints the reservation number.

    Parameters:
    reservation (list): reservation data split by |
    """
    reservation_id = int(reservation[0])
    print(f"Reservation number: {reservation_id}")


def print_booker(reservation: list) -> None:
    """
    Prints the booker name.
    """
    booker = reservation[1]
    print(f"Booker: {booker}")


def print_date(reservation: list) -> None:
    """
    Prints the reservation date in Finnish format.
    """
    day = datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_day = day.strftime("%d.%m.%Y")
    print(f"Date: {finnish_day}")


def print_start_time(reservation: list) -> None:
    """
    Prints the start time.
    """
    time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = time.strftime("%H.%M")
    print(f"Start time: {finnish_time}")


def print_hours(reservation: list) -> None:
    """
    Prints the number of hours.
    """
    hours = int(reservation[4])
    print(f"Hours: {hours}")


def print_hourly_price(reservation: list) -> None:
    """
    Prints the hourly price.
    """
    price = float(reservation[5])
    price_text = f"{price:.2f}".replace(".", ",") + " €"
    print(f"Hourly price: {price_text}")


def print_total_price(reservation: list) -> None:
    """
    Prints the total price.
    """
    hours = int(reservation[4])
    price = float(reservation[5])
    total_price = hours * price
    total_text = f"{total_price:.2f}".replace(".", ",") + " €"
    print(f"Total price: {total_text}")


def print_paid(reservation: list) -> None:
    """
    Prints payment status.
    """
    paid = reservation[6] == "True"

    if paid:
        print("Paid: Yes")
    else:
        print("Paid: No")


def print_location(reservation: list) -> None:
    """
    Prints the location.
    """
    location = reservation[7]
    print(f"Location: {location}")


def print_phone(reservation: list) -> None:
    """
    Prints the phone number.
    """
    phone = reservation[8]
    print(f"Phone: {phone}")


def print_email(reservation: list) -> None:
    """
    Prints the email address.
    """
    email = reservation[9]
    print(f"Email: {email}")


def main() -> None:
    """
    Reads the reservation file and prints all reservation details.
    """
    with open("reservations.txt", "r") as file:
        line = file.readline().strip()

    reservation = line.split("|")

    print_reservation_number(reservation)
    print_booker(reservation)
    print_date(reservation)
    print_start_time(reservation)
    print_hours(reservation)
    print_hourly_price(reservation)
    print_total_price(reservation)
    print_paid(reservation)
    print_location(reservation)
    print_phone(reservation)
    print_email(reservation)


if __name__ == "__main__":
    main()
