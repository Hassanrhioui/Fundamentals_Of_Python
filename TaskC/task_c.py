# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Hassan Rhioui according to given task




from datetime import datetime


def convert_reservation_data(reservation: list) -> list:
    """
    Converts raw string reservation data into correct Python data types.
    """

    reservation_id = int(reservation[0])
    customer_name = reservation[1]
    email = reservation[2]
    phone = reservation[3]

    reservation_date = datetime.strptime(reservation[4], "%Y-%m-%d").date()
    reservation_time = datetime.strptime(reservation[5], "%H:%M").time()

    duration_hours = int(reservation[6])
    price = float(reservation[7])

    confirmed = reservation[8] == "True"
    reserved_resource = reservation[9]

    created_at = datetime.strptime(reservation[10], "%Y-%m-%d %H:%M:%S")

    return [
        reservation_id,
        customer_name,
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




def print_confirmed_reservations(reservations: list) -> None:
    print("1) Confirmed Reservations")

    for r in reservations:
        if r[8]:
            date_text = r[4].strftime("%d.%m.%Y")
            time_text = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {r[9]}, {date_text} at {time_text}")

    print()


def print_long_reservations(reservations: list) -> None:
    print("2) Long Reservations (≥ 3 h)")

    for r in reservations:
        if r[6] >= 3:
            date_text = r[4].strftime("%d.%m.%Y")
            time_text = r[5].strftime("%H.%M")
            print(f"- {r[1]}, {date_text} at {time_text}, duration {r[6]} h, {r[9]}")

    print()


def print_confirmation_statuses(reservations: list) -> None:
    print("3) Reservation Confirmation Status")

    for r in reservations:
        status = "Confirmed" if r[8] else "Not confirmed"
        print(f"- {r[1]}: {status}")

    print()


def print_summary_counts(reservations: list) -> None:
    print("4) Confirmation Summary")

    total = len(reservations)
    confirmed = sum(1 for r in reservations if r[8])

    print(f"- Total reservations: {total}")
    print(f"- Confirmed reservations: {confirmed}")
    print()


def print_total_revenue(reservations: list) -> None:
    print("5) Total Revenue from Confirmed Reservations")

    revenue = 0.0

    for r in reservations:
        if r[8]:
            revenue += r[6] * r[7]

    revenue_text = f"{revenue:.2f}".replace(".", ",") + " €"
    print(f"- {revenue_text}")
    print()



def main() -> None:
    reservations = []

    with open("reservations.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                raw = line.split("|")
                converted = convert_reservation_data(raw)
                reservations.append(converted)

    print_confirmed_reservations(reservations)
    print_long_reservations(reservations)
    print_confirmation_statuses(reservations)
    print_summary_counts(reservations)
    print_total_revenue(reservations)


if __name__ == "__main__":
    main()
