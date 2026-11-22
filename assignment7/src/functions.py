"""
Hey, Ariana, if you want to run it -> python3 start.py in your terminal, or hit the run while being on start.py file.
Problem 5: Apartment Building Administrator.
Each expense stores an apartment number, a category, and an amount in RON.
"""


def positive_integer(text):
    number = int(text)
    if number <= 0:
        raise ValueError("The number must be greater than 0.")
    return number


def check_category(category):
    if category not in ("water", "heating", "electricity", "gas", "other"):
        raise ValueError("Category must be water, heating, electricity, gas, or other.")


def add_expense(expenses, apartment, category, amount):
    expense = {"apartment": apartment, "type": category, "amount": amount}
    return expenses + [expense]


def remove_apartments(expenses, start, end):
    if start > end:
        raise ValueError("The first apartment must not exceed the last.")

    result = []
    for expense in expenses:
        if not start <= expense["apartment"] <= end:
            result.append(expense)
    return result


def remove_category(expenses, category):
    result = []
    for expense in expenses:
        if expense["type"] != category:
            result.append(expense)
    return result


def replace_amount(expenses, apartment, category, amount):
    result = []
    found = False
    for expense in expenses:
        updated = expense.copy()
        if expense["apartment"] == apartment and expense["type"] == category:
            updated["amount"] = amount
            found = True
        result.append(updated)

    if not found:
        raise ValueError("No expense matches that apartment and category.")
    return result


def filter_category(expenses, category):
    result = []
    for expense in expenses:
        if expense["type"] == category:
            result.append(expense)
    return result


def filter_amount(expenses, limit):
    result = []
    for expense in expenses:
        if expense["amount"] < limit:
            result.append(expense)
    return result


def apartment_expenses(expenses, apartment):
    result = []
    for expense in expenses:
        if expense["apartment"] == apartment:
            result.append(expense)
    return result


def apartment_totals(expenses):
    totals = {}
    for expense in expenses:
        apartment = expense["apartment"]
        if apartment not in totals:
            totals[apartment] = 0
        totals[apartment] += expense["amount"]
    return totals


def matches(total, operator, amount):
    if operator == "<":
        return total < amount
    if operator == "=":
        return total == amount
    if operator == ">":
        return total > amount
    raise ValueError("Use <, =, or > for the comparison.")


def change_expenses(expenses, words):
    command = words[0]

    if command == "add" and len(words) == 4:
        apartment = positive_integer(words[1])
        check_category(words[2])
        amount = positive_integer(words[3])
        return add_expense(expenses, apartment, words[2], amount)

    if command == "remove":
        if len(words) == 2:
            if words[1].isalpha():
                check_category(words[1])
                return remove_category(expenses, words[1])
            apartment = positive_integer(words[1])
            return remove_apartments(expenses, apartment, apartment)

        if len(words) == 4 and words[2] == "to":
            start = positive_integer(words[1])
            end = positive_integer(words[3])
            return remove_apartments(expenses, start, end)

    if command == "replace" and len(words) == 5 and words[3] == "with":
        apartment = positive_integer(words[1])
        check_category(words[2])
        amount = positive_integer(words[4])
        return replace_amount(expenses, apartment, words[2], amount)

    if command == "filter" and len(words) == 2:
        if words[1].isalpha():
            check_category(words[1])
            return filter_category(expenses, words[1])
        limit = positive_integer(words[1])
        return filter_amount(expenses, limit)

    raise ValueError("Invalid command format. Enter help to see the commands.")
