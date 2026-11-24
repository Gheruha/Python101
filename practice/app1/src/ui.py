# UI
from functions import change_flights, show_flights
from texttable import Texttable

# Show help function: shows the menu options which an example for each option


def show_menu():
    table = Texttable(max_width=100)
    table.header(["Command", "Example"])
    table.set_cols_align(["l", "l"])
    table.add_rows(
        [
            [
                "add <flight code> <duration> <departure> <destination>",
                "add QF1000 180 Rome Zurich",
            ],
            ["modify <flight code> <duration>", "modify QF1000 240"],
            ["reroute <destination> <new destination>", "reroute Zurich Geneva"],
            ["show <departure>", "show Zurich"],
            ["help", "Display the menu"],
            ["exit", "Stop the application"],
        ],
        header=False,
    )

    print(table.draw())
    print("The flight code should be written in the following format: (XX0000).")
    print("The duration is written in minutes, for 180 means 3 hours.")
    print(
        "The destination should be a city, and the name should be written with more than 3 characters."
    )
    print("The departure has the same rule as destination.")


def main():
    show_menu()
    flights = []

    # Keeping the app running and calling the chosen functions
    while True:
        words = input("Enter a command: ").lower().split()
        if len(words) == 0:
            continue

        try:
            if words == ["exit"]:
                return False
            elif words == ["help"]:
                show_menu()
            elif words[0] == "show":
                show_flights(words, flights)
            else:
                flights = change_flights(words, flights)
                print(flights)

        except ValueError as error:
            print("Error", error)
