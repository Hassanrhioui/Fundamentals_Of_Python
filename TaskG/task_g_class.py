# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# Modified by Hassan Rhioui according to given task

from datetime import datetime


class Reservation:
    def __init__(self, reservation_id, name, email, phone,
                 date, time, duration, price,
                 confirmed, resource, created):

        self.reservation_id = reservation_id
        self.name = name
        self.email = email
        self.phone = phone
        self.date = date
        self.time = time
        self.duration = duration
        self.price = price
        self.confirmed = confirmed
        self.resource = resource
        self.created = created

    def is_confirmed(self) -> bool:
        return self.confirmed

    def is_long(self) -> bool:
        return self.duration >= 3

    def total_price(self) -> float:
        return self.duration * self.price


def convert_reservation(data: list[str]) -> Reservation:
    """
    Convert reservation data into object
    """
    return Reservation(
        reservation_id=int(data[0]),
        name=data[1],
        email=data[2],
        phone=data[3],
        date=datetime.strptime(data[4], "%Y-%m-%d").date(),
        time=datetime.strptime(data[5], "%H:%M").time(),
        duration=int(data[6]),
        price=float(data[7]),
        confirmed=True if data[8].strip() == "True" else False,
        resource=data[9],
        created=datetime.strptime(data[10].strip(), "%Y-%m-%d %H:%M:%S")
    )


def fetch_reservations(filename: str) -> list[Reservation]:
    """
    Read and convert reservations
    """
    reservations = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if len(line) > 1:
                fields = line.split("|")
                reservations.append(convert_reservation(fields))

    return reservations


def confirmed_reservations(reservations: list[Reservation]) -> None:
    print("1) Confirmed Reservations")
    for r in reservations:
        if r.is_confirmed():
            print(f" - {r.name}, {r.resource}, {r.date.strftime('%d.%m.%Y')} at {r.time.strftime('%H.%M')}")


def long_reservations(reservations: list[Reservation]) -> None:
    print("2) Long Reservations (≥ 3 h)")
    for r in reservations:
        if r.is_long():
            print(f" - {r.name}, {r.date.strftime('%d.%m.%Y')} at {r.time.strftime('%H.%M')}, duration {r.duration} h, {r.resource}")


def confirmation_statuses(reservations: list[Reservation]) -> None:
    print("3) Reservation Confirmation Status")
    for r in reservations:
        print(f" - {r.name} → {'Confirmed' if r.confirmed else 'NOT Confirmed'}")


def confirmation_summary(reservations: list[Reservation]) -> None:
    print("4) Confirmation Summary")

    confirmed_count = len([r for r in reservations if r.is_confirmed()])
    not_confirmed = len(reservations) - confirmed_count

    print(f" - Confirmed reservations: {confirmed_count} pcs")
    print(f" - Not confirmed reservations: {not_confirmed} pcs")


def total_revenue(reservations: list[Reservation]) -> None:
    print("5) Total Revenue from Confirmed Reservations")

    revenue = sum(r.total_price() for r in reservations if r.is_confirmed())
    print(f"Total revenue from confirmed reservations: {revenue:.2f} €".replace('.', ','))
    print("Thanks Ville, this was a great course!")


def main():
    reservations = fetch_reservations("reservations.txt")

    confirmed_reservations(reservations)
    long_reservations(reservations)
    confirmation_statuses(reservations)
    confirmation_summary(reservations)
    total_revenue(reservations)


if __name__ == "__main__":
    main()
    
    
