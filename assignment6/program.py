# Assignment 06: A1 (distinct subarray) and B1 (increasing modulus subsequence).
# Dictionary representation is active; list functions are commented out.
# To use lists, uncomment the six list functions and comment out the six
# dictionary functions. Keep only one representation active at a time.


# Functions to deal with complex numbers -- list representation
# No input or print statements.


# def create_number(real, imaginary):
#     return [real, imaginary]


# def get_real(number):
#     return number[0]


# def get_imaginary(number):
#     return number[1]


# def set_real(number, real):
#     number[0] = real
#     return number


# def set_imaginary(number, imaginary):
#     number[1] = imaginary
#     return number


# def to_str(number):
#     real = get_real(number)
#     imaginary = get_imaginary(number)
#     if imaginary < 0:
#         return f"{real:g} - {abs(imaginary):g}i"
#     return f"{real:g} + {imaginary:g}i"


# Functions to deal with complex numbers -- dictionary representation
# To use lists, comment out these six definitions and uncomment those above.


def create_number(real, imaginary):
    return {"real": real, "imaginary": imaginary}


def get_real(number):
    return number["real"]


def get_imaginary(number):
    return number["imaginary"]


def set_real(number, real):
    number["real"] = real
    return number


def set_imaginary(number, imaginary):
    number["imaginary"] = imaginary
    return number


def to_str(number):
    real = get_real(number)
    imaginary = get_imaginary(number)
    if imaginary < 0:
        return f"{real:g} - {abs(imaginary):g}i"
    return f"{real:g} + {imaginary:g}i"


def modulus_squared(number):
    return get_real(number) ** 2 + get_imaginary(number) ** 2


def longest_distinct_subarray(numbers):
    """
    A1: Return a longest consecutive subarray with no repeated complex numbers.
    Input: a list of complex numbers in the active representation.
    Output: a list of the selected numbers; [] for empty input.
    Equal numbers have equal real AND imaginary parts.
    If several answers have the same length, keep the first.
    Naive method: try each start and extend until a repeated number occurs.
    Time: O(n^3) worst case, because list membership takes O(n).
    Extra space: O(n).
    """
    best_start = 0
    best_length = 0

    for start in range(len(numbers)):
        current = []
        for end in range(start, len(numbers)):
            if numbers[end] in current:
                break

            current.append(numbers[end])
            if len(current) > best_length:
                best_start = start
                best_length = len(current)

    return numbers[best_start : best_start + best_length]


def longest_increasing_subsequence(numbers):
    """
    B1: Return a longest subsequence with strictly increasing modulus.
    Input: a list of complex numbers in the active representation.
    Output: a list in original order; elements may be skipped.
    Empty input returns []. Equal moduli cannot extend a subsequence.
    Method: dynamic programming with a length and predecessor for each position.
    Time: O(n^2). Extra space: O(n).
    """
    if len(numbers) == 0:
        return []

    n = len(numbers)
    values = [modulus_squared(number) for number in numbers]

    lengths = [1] * n

    previous = [-1] * n

    for i in range(n):
        for j in range(i):
            if values[j] < values[i]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    previous[i] = j

    best_end = 0
    for i in range(1, n):
        if lengths[i] > lengths[best_end]:
            best_end = i

    result = []
    while best_end != -1:
        result.append(numbers[best_end])
        best_end = previous[best_end]

    result.reverse()
    return result


def initial_numbers():
    return [
        create_number(1, 0),
        create_number(3, 4),
        create_number(1, 0),
        create_number(0, 2),
        create_number(2, 2),
        create_number(-3, 0),
        create_number(3, 4),
        create_number(0, -1),
        create_number(6, 0),
        create_number(0, 7),
    ]


# UI section
def read_number():
    while True:
        text = input("Enter a complex number, for example 3 + 2i or 4 - i: ")
        text = text.replace(" ", "").replace("i", "j")
        try:
            value = complex(text)
            from math import isfinite

            if not isfinite(value.real) or not isfinite(value.imag):
                raise ValueError
            return create_number(value.real, value.imag)
        except ValueError:
            print("Enter a valid finite complex number, for example 3 + 2i.")


def write_number(number):
    print(to_str(number))


def read_numbers():
    while True:
        try:
            count = int(input("How many complex numbers do you want to enter? "))
            if count >= 0:
                break
        except ValueError:
            pass
        print("Enter a whole number greater than or equal to 0.")

    numbers = []
    for i in range(count):
        print(f"Number {i + 1}:")
        numbers.append(read_number())
    return numbers


def write_numbers(numbers):
    if len(numbers) == 0:
        print("The list is empty.")
    for number in numbers:
        write_number(number)


def show_properties(numbers):
    result = longest_distinct_subarray(numbers)
    print("\nA(1): Longest consecutive subarray of distinct numbers")
    print("Length:", len(result))
    write_numbers(result)

    result = longest_increasing_subsequence(numbers)
    print("\nB(1): Longest subsequence with increasing modulus")
    print("Length:", len(result))
    write_numbers(result)


def main():
    numbers = initial_numbers()
    print("The program has 10 complex numbers already.")

    while True:
        print("\n1. Read a new list of complex numbers;")
        print("2. Display the list;")
        print("3. Display the A(1) and B(1) result;")
        print("4. Exit;")
        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            numbers = read_numbers()
        elif option == "2":
            write_numbers(numbers)
        elif option == "3":
            show_properties(numbers)
        elif option == "4":
            return
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
