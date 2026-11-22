from functions import (apartment_expenses, apartment_totals, change_expenses,
                       matches, positive_integer)
from texttable import Texttable


def show_help():
    table = Texttable(max_width=100)
    table.header(["Command", "Example"])
    table.set_cols_align(["l", "l"])
    table.add_rows(
        [
            ["add <apartment> <type> <amount>", "add 25 gas 100"],
            ["remove <apartment>", "remove 25"],
            ["remove <first> to <last>", "remove 5 to 10"],
            ["remove <type>", "remove gas"],
            ["replace <apartment> <type> with <amount>", "replace 12 gas with 200"],
            ["list", "list"],
            ["list <apartment>", "list 25"],
            ["list <comparison> <amount>", "list > 100"],
            ["filter <type>", "filter gas"],
            ["filter <amount>", "filter 300"],
            ["undo", "Undo the last change"],
            ["help", "Display this menu"],
            ["ariana", "Close the application"],
        ],
        header=False,
    )
    print(table.draw())
    print("Categories: water, heating, electricity, gas, other.")
    print("Apartment numbers and amounts must be positive integers.")
    print("Comparisons: <, =, >. They compare TOTAL expenses per apartment.")
    print("filter <amount> keeps individual expenses strictly below the amount.")
    print("replace updates all matching entries for the apartment and category.")
    print("hey ariana")


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses.")
        return
    for expense in expenses:
        print(
            f"Apartment {expense['apartment']}: {expense['type']} - {expense['amount']} RON"
        )


def show_list(expenses, words):
    if len(words) == 1:
        show_expenses(expenses)
    elif len(words) == 2:
        apartment = positive_integer(words[1])
        show_expenses(apartment_expenses(expenses, apartment))
    elif len(words) == 3 and words[1] in ("<", "=", ">"):
        amount = int(words[2])
        totals = apartment_totals(expenses)
        found = False
        for apartment in sorted(totals):
            if matches(totals[apartment], words[1], amount):
                print(f"Apartment {apartment}: total {totals[apartment]} RON")
                found = True
        if not found:
            print("No apartments match.")
    else:
        raise ValueError("Use list, list <apartment>, or list <comparison> <amount>.")


def main():
    expenses = []
    history = []
    print("Apartment Building Administrator")
    show_help()

    while True:
        words = input("Enter a command: ").lower().split()
        if len(words) == 0:
            continue

        try:
            if words == ["ariana"]:
                return
            elif words == ["help"]:
                show_help()
            elif words == ["undo"]:
                if len(history) == 0:
                    print("There is nothing to undo.")
                else:
                    expenses = history.pop()
                    print("Last change undone.")
            elif words[0] == "list":
                show_list(expenses, words)
            else:
                new_expenses = change_expenses(expenses, words)
                if new_expenses == expenses:
                    print("Nothing changed.")
                else:
                    history.append(expenses)
                    expenses = new_expenses
                    print("Expenses updated.")
        except ValueError as error:
            print("Error:", error)
