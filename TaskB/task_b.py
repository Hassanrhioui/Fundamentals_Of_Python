# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Hassan Rhioui according to given task


from datetime import datetime
"""Print reservation number."""
def print_reservstion_number(reservation: list) -> None: 
    number = int(reservation[0])
    print(f"Reservation number: {number}")


def print_booker(reservation: list) -> None:
    booker = reservation[1]
    print(f"Booker: {booker}")

def print_dates(reservation: list) -> None:
    date =datetime.strptime(reservation[2], "%Y-%m-%d").date()
    finnish_date = date.strftime("%d.%m.%Y")
    print(f"Date: {finnish_date}")

def print_start_time(reservation: list) -> None:
    time = datetime.strptime(reservation[3], "%H:%M").time()
    finnish_time = time.strftime("%H.%M")
    print(f"Start time: {finnish_time}")

def print_hours(reservation: list) -> None:
    hours = int(reservation[4])
    print(f"Hours: {hours}")

def print_hourly_price(reservation: list) -> None:
    price = float(reservation[5])
    price_output = f"{price:.2f}" .replace(".",",") + "€"
    print(f"Hourly price: {price_output}")


def print_total_price(reservation: list) -> None:
    hours = int(reservation[4])
    price = float(reservation[5])
    total_price = hours * price
    total_price_output = f"{total_price:.2f}" .replace(".",",") + "€"
    print(f"Total price: {total_price_output}")

def print_paid(reservation: list) -> None:
    paid = reservation[6]
    is_paid = paid == "True"

    if is_paid:
        print("Paid: Yes")
    else:
        print("Paid: No")

def print_location(reservation: list) -> None:
    location = reservation[7]
    print(f"Location: {location}")

def print_phone(reservation: list) -> None:
    phone = reservation[8]
    print(f"Phone: {phone}")

def print_email(reservation: list) -> None:
    email = reservation[9]
    print(f"Email: {email}")



def main() -> None:
    with open("reservations.txt", "r") as file:
        line = file.readline().strip()

    reservation = line.split("|")


    print_reservstion_number(reservation)
    print_booker(reservation)
    print_dates(reservation)
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
