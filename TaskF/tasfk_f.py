# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# Modified by Hassan Rhioui according to given task

from datetime import datetime, date
from typing import List, Dict
import csv


def read_data(filename: str) -> List[Dict]:
    """Reads CSV file and returns a list."""
    data: List[Dict] = []

    with open(filename, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)

        for row in reader:
            timestamp = datetime.fromisoformat(row[0].replace("+02:00", ""))
            consumption = float(row[1].replace(",", "."))
            production = float(row[2].replace(",", "."))
            temperature = float(row[3].replace(",", "."))

            data.append({
                "datetime": timestamp,
                "date": timestamp.date(),
                "month": timestamp.month,
                "consumption": consumption,
                "production": production,
                "temperature": temperature
            })

    return data


def show_main_menu() -> str:
    """Shows main menu and returns user choice."""
    print("\nChoose a report type:")
    print("1) Daily summary for a date range")
    print("2) Monthly summary for one month")
    print("3) Full year 2025 summary")
    print("4) Exit the program")
    return input("Enter choice: ").strip()


def create_daily_report(data: List[Dict]) -> List[str]:
    """Creates daily summary for a selected date range."""
    start = datetime.strptime(input("Enter start date (dd.mm.yyyy): "), "%d.%m.%Y").date()
    end = datetime.strptime(input("Enter end date (dd.mm.yyyy): "), "%d.%m.%Y").date()

    daily: Dict[date, Dict] = {}

    for row in data:
        if start <= row["date"] <= end:
            day = row["date"]
            if day not in daily:
                daily[day] = {"cons": 0.0, "prod": 0.0, "temps": []}

            daily[day]["cons"] += row["consumption"]
            daily[day]["prod"] += row["production"]
            daily[day]["temps"].append(row["temperature"])

    total_cons = sum(v["cons"] for v in daily.values())
    total_prod = sum(v["prod"] for v in daily.values())
    daily_avg_temps = [sum(v["temps"]) / len(v["temps"]) for v in daily.values()]
    avg_temp = sum(daily_avg_temps) / len(daily_avg_temps)

    lines = [
        "-" * 53,
        f"Report for the period {start.day}.{start.month}.{start.year}–{end.day}.{end.month}.{end.year}",
        f"- Total consumption: {format_number(total_cons)} kWh",
        f"- Total production: {format_number(total_prod)} kWh",
        f"- Average temperature: {format_number(avg_temp)} °C"
    ]

    return lines


def create_monthly_report(data: List[Dict]) -> List[str]:
    """Creates monthly summary for one selected month."""
    month = int(input("Enter month number (1–12): "))

    daily: Dict[date, Dict] = {}

    for row in data:
        if row["month"] == month:
            day = row["date"]
            if day not in daily:
                daily[day] = {"cons": 0.0, "prod": 0.0, "temps": []}

            daily[day]["cons"] += row["consumption"]
            daily[day]["prod"] += row["production"]
            daily[day]["temps"].append(row["temperature"])

    total_cons = sum(v["cons"] for v in daily.values())
    total_prod = sum(v["prod"] for v in daily.values())
    daily_avg_temps = [sum(v["temps"]) / len(v["temps"]) for v in daily.values()]
    avg_temp = sum(daily_avg_temps) / len(daily_avg_temps)

    month_name = datetime(2025, month, 1).strftime("%B")

    lines = [
        "-" * 53,
        f"Report for the month: {month_name}",
        f"- Total consumption: {format_number(total_cons)} kWh",
        f"- Total production: {format_number(total_prod)} kWh",
        f"- Average temperature: {format_number(avg_temp)} °C"
    ]

    return lines


def create_yearly_report(data: List[Dict]) -> List[str]:
    """Creates full year summary report."""
    daily: Dict[date, Dict] = {}

    for row in data:
        day = row["date"]
        if day not in daily:
            daily[day] = {"cons": 0.0, "prod": 0.0, "temps": []}

        daily[day]["cons"] += row["consumption"]
        daily[day]["prod"] += row["production"]
        daily[day]["temps"].append(row["temperature"])

    total_cons = sum(v["cons"] for v in daily.values())
    total_prod = sum(v["prod"] for v in daily.values())
    daily_avg_temps = [sum(v["temps"]) / len(v["temps"]) for v in daily.values()]
    avg_temp = sum(daily_avg_temps) / len(daily_avg_temps)

    lines = [
        "-" * 53,
        "Report for the year: 2025",
        f"- Total consumption: {format_number(total_cons)} kWh",
        f"- Total production: {format_number(total_prod)} kWh",
        f"- Average temperature: {format_number(avg_temp)} °C"
    ]

    return lines


def print_report_to_console(lines: List[str]) -> None:
    """Prints report lines to console."""
    for line in lines:
        print(line)


def write_report_to_file(lines: List[str]) -> None:
    """Writes report lines to report.txt."""
    with open("report.txt", "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def format_number(value: float) -> str:
    """Formats number with two decimals and comma separator."""
    return f"{value:.2f}".replace(".", ",")


def main() -> None:
    """Main program loop."""
    data = read_data("2025.csv")

    while True:
        choice = show_main_menu()

        if choice == "1":
            report = create_daily_report(data)
        elif choice == "2":
            report = create_monthly_report(data)
        elif choice == "3":
            report = create_yearly_report(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
            continue

        print_report_to_console(report)

        print("\nWhat would you like to do next?")
        print("1) Write the report to the file report.txt")
        print("2) Create a new report")
        print("3) Exit the program") 

        next_choice = input("Enter choice: ").strip()

        if next_choice == "1":
            write_report_to_file(report)
            print("Report written to report.txt")
        elif next_choice == "3":
            break


if __name__ == "__main__":
    main()
