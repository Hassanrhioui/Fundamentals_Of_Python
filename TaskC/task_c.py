# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Hassan Rhioui according to given task




from datetime import datetime



def convert_reservation_data(row):
    """Convert one reservation row (list of strings) into correct data types."""

    reservation_id = int(row[0])
    name = row[1]
    email = row[2]
    phone = row[3]

    reservation_date = datetime.strptime(row[4], "%Y-%m-%d").date()
    reservation_time = datetime.strptime(row[5], "%H:%M").time()

    duration_hours = int(row[6])
    price = float(row[7])
    confirmed = (row[8] == "True")

    reserved_resource = row[9]
    created_at = datetime.strptime(row[10], "%Y-%m-%d %H:%M:%S")

    return [
        reservation_id,
        name,
        email,
        phone,
        reservation_date,
        reservation_time,
        duration_hours,
        price,
        confirmed,
        reserved_resource,
        created_at
    ]


def read_reservations():
    """Read reservations.txt and return converted reservation lists."""
    reservations = []
    with open("reservations.txt", "r", encoding="utf-8") as file:
        for line in file:
            row = line.strip().split("|")
            reservations.append(convert_reservation_data(row))
    return reservations




def confirmed_reservations(reservations):
    print("1) Confirmed Reservations")
    for r in reservations:
        if r[8]:  
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {r[9]}, {date_str} at {time_str}")
    print()


def long_reservations(reservations):
    print("2) Long Reservations (≥ 3 h)")
    for r in reservations:
        if r[6] >= 3:
            date_str = r[4].strftime("%d.%m.%Y")
            time_str = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {date_str} at {time_str}, duration {r[6]} h, {r[9]}")
    print()


def confirmation_statuses(reservations):
    print("3) Reservation Confirmation Status")
    for r in reservations:
        status = "Confirmed" if r[8] else "NOT Confirmed"
        print(f"{r[1]} → {status}")
    print()


def confirmation_summary(reservations):
    print("4) Confirmation Summary")
    confirmed_count = sum(1 for r in reservations if r[8])
    not_confirmed_count = len(reservations) - confirmed_count

    print(f"- Confirmed reservations: {confirmed_count} pcs")
    print(f"- Not confirmed reservations: {not_confirmed_count} pcs")
    print()


def total_revenue(reservations):
    print("5) Total Revenue from Confirmed Reservations")
    total = sum(r[7] * r[6] for r in reservations if r[8])
    total_str = f"{total:.2f}".replace(".", ",")
    print(f"Total revenue from confirmed reservations: {total_str} €")
    print()



def main():
    reservations = read_reservations()

    confirmed_reservations(reservations)
    long_reservations(reservations)
    confirmation_statuses(reservations)
    confirmation_summary(reservations)
    total_revenue(reservations)


if __name__ == "__main__":
    main()

