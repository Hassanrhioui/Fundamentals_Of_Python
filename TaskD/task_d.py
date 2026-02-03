# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# Modified by Hassan Rhioui according to given task


from datetime import datetime, date


def read_data(filename: str) -> list:
    data = []

    with open(filename, "r", encoding="utf-8") as file:
        next(file)

        for line in file:
            row = line.strip().split(";")

            timestamp = datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S")

            data.append([
                timestamp,
                float(row[1]),
                float(row[2]),
                float(row[3]),
                float(row[4]),
                float(row[5]),
                float(row[6]),
            ])

    return data



def day_information(day: date, database: list) -> str:
    """
    Calculates daily consumption and production by phase
    and returns one formatted report line.
    """

    c1 = c2 = c3 = 0.0
    p1 = p2 = p3 = 0.0

    for row in database:
        if row[0].date() == day:
            c1 += row[1] / 1000
            c2 += row[2] / 1000
            c3 += row[3] / 1000
            p1 += row[4] / 1000
            p2 += row[5] / 1000
            p3 += row[6] / 1000

    c1 = f"{c1:.2f}".replace(".", ",")
    c2 = f"{c2:.2f}".replace(".", ",")
    c3 = f"{c3:.2f}".replace(".", ",")

    p1 = f"{p1:.2f}".replace(".", ",")
    p2 = f"{p2:.2f}".replace(".", ",")
    p3 = f"{p3:.2f}".replace(".", ",")

    return (
        f"{day.strftime('%A'):<11}"
        f"{day.strftime('%d.%m.%Y'):<12}"
        f"{c1:>7}  {c2:>7}  {c3:>7}     "
        f"{p1:>7}  {p2:>7}  {p3:>7}"
    )


def main() -> None:
    """
    Main function.
    Reads data, computes totals, prints the report.
    """

    db = read_data("week42.csv")

    print("Week 42 electricity consumption and production (kWh, by phase)\n")

    print("Day          Date        Consumption [kWh]               Production [kWh]")
    print("            (dd.mm.yyyy)  v1      v2      v3             v1     v2     v3")

    print(day_information(date(2025, 10, 14), db))
    print(day_information(date(2025, 10, 15), db))
    print(day_information(date(2025, 10, 16), db))
    print(day_information(date(2025, 10, 17), db))
    print(day_information(date(2025, 10, 18), db))
    print(day_information(date(2025, 10, 19), db))


if __name__ == "__main__":
    main()
