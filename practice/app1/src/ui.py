# UI
from texttable import Texttable

# Show help function: shows the menu options which an example for each option


def show_help():
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
    show_help()
