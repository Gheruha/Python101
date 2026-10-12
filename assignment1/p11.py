"""
PROBLEM 11: The numbers n1 and n2 have the property P if their writing in base 10 uses the same digits
(e.g. 2113 and 323121). Determine whether two given natural numbers have property P.
"""


def get_digits(number):
    number = abs(number)
    digits = set()

    if number == 0:
        digits.add(0)

    while number != 0:
        digits.add(number % 10)
        number //= 10

    return digits


def main():
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))

    if get_digits(n1) == get_digits(n2):
        print("n1 and n2 have the property P.")
    else:
        print("n1 and n2 do not have the property P.")


if __name__ == "__main__":
    main()
