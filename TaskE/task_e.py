# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# Modified by Hassan Rhioui according to given task

from datetime import datetime, date
from typing import List, Dict


def read_data(filename: str) -> List[list]:
    rows = []

    with open(filename, "r", encoding="utf-8") as file:
        header = file.readline()
        for line in file:
            row = line.strip().split(";")
            rows.append(row)

    return rows


def parse_timestamp(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def calculate_daily_summaries(rows: List[list]) -> Dict[date, dict]:
    summary: Dict[date, dict] = {}

    for row in rows:
        timestamp = parse_timestamp(row[0])
        day = timestamp.date()

        cons = [float(row[1]), float(row[2]), float(row[3])]
        prod = [float(row[4]), float(row[5]), float(row[6])]

        if day not in summary:
            summary[day] = {
                "consumption": [0.0, 0.0, 0.0],
                "production": [0.0, 0.0, 0.0]
            }

        for i in range(3):
            summary[day]["consumption"][i] += cons[i] / 1000
            summary[day]["production"][i] += prod[i] / 1000

    return summary


def format_kwh(value: float) -> str:
    return f"{value:.2f}".replace(".", ",")


def weekday_fi(day: date) -> str:
    names = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    return names[day.weekday()]


def format_week_report(week_number: int, daily: Dict[date, dict]) -> List[str]:
    lines = []

    lines.append(
        f"Week {week_number} electricity consumption and production (kWh, by phase)"
    )
    lines.append("")
    lines.append(
        "Day          Date        Consumption [kWh]               Production [kWh]"
    )
    lines.append(
        "            (dd.mm.yyyy)  v1      v2      v3             v1     v2     v3"
    )
    lines.append(
        "-" * 75
    )

    for day in sorted(daily.keys()):
        data = daily[day]

        cons = data["consumption"]
        prod = data["production"]

        date_str = day.strftime("%d.%m.%Y")
        line = (
            f"{weekday_fi(day):<11}"
            f"{date_str:<12}"
            f"{format_kwh(cons[0]):>7}  "
            f"{format_kwh(cons[1]):>6}  "
            f"{format_kwh(cons[2]):>6}        "
            f"{format_kwh(prod[0]):>5}  "
            f"{format_kwh(prod[1]):>5}  "
            f"{format_kwh(prod[2]):>5}"
        )
        lines.append(line)

    lines.append("")
    return lines


def write_report(lines: List[str]) -> None:
    """
    Writes the report to summary.txt.
    """
    with open("summary.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def main() -> None:
    """
    Main function.
    Reads data from three weeks and writes summary report.
    """
    all_lines: List[str] = []

    weeks = {
        41: "week41.csv",
        42: "week42.csv",
        43: "week43.csv"
    }

    for week, filename in weeks.items():
        rows = read_data(filename)
        daily = calculate_daily_summaries(rows)
        week_lines = format_week_report(week, daily)
        all_lines.extend(week_lines)

    write_report(all_lines)
    print("summary.txt created successfully.")


if __name__ == "__main__":
    main()
