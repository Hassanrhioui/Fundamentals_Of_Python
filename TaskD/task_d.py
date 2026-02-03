import csv
from datetime import datetime, date
from typing import List, Dict


def read_data(filename: str) -> List[Dict]:
    
    rows = []

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)  

        for row in reader:
            timestamp = datetime.fromisoformat(row[0])
            values = list(map(float, row[1:]))

            rows.append({
                "date": timestamp.date(),
                "values": values
            })

    return rows


def calculate_daily_totals(rows: List[Dict]) -> Dict[date, Dict[str, List[float]]]:
    
    totals = {}

    for row in rows:
        d = row["date"]

        if d not in totals:
            totals[d] = {
                "consumption": [0.0, 0.0, 0.0],
                "production": [0.0, 0.0, 0.0]
            }

        values = row["values"]

        for i in range(3):
            totals[d]["consumption"][i] += values[i] / 1000
            totals[d]["production"][i] += values[i + 3] / 1000

    return totals


def format_kwh(value: float) -> str:
    
    return f"{value:.2f}".replace(".", ",")


def print_report(totals: Dict[date, Dict[str, List[float]]]) -> None:
    
    weekdays = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    print("Week 42 electricity consumption and production (kWh, by phase)\n")
    print("Day        Date           Consumption [kWh]               Production [kWh]")
    print("          (dd.mm.yyyy)    v1       v2      v3            v1      v2      v3")
    print("-" * 75)

    for d in sorted(totals.keys()):
        weekday = weekdays[d.weekday()]
        date_str = d.strftime(" %d.%m.%Y")

        cons = totals[d]["consumption"]
        prod = totals[d]["production"]

        print(
            f"{weekday:<10} {date_str:<10}  "
            f"{format_kwh(cons[0]):>6}  {format_kwh(cons[1]):>6}  {format_kwh(cons[2]):>6}        "
            f"{format_kwh(prod[0]):>6}  {format_kwh(prod[1]):>6}  {format_kwh(prod[2]):>6}"
        )


def main() -> None:
    
    
    data = read_data("week42.csv")
    totals = calculate_daily_totals(data)
    print_report(totals)


if __name__ == "__main__":
    main()
