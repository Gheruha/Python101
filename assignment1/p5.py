"""
Generate the largest prime number smaller than a given natural number n.
If such a number does not exist, a message should be displayed.
"""


def is_prime(n):
    if n < 2:
        return False

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


def largest_prime_smaller_than(n):
    for candidate in range(n - 1, 1, -1):
        if is_prime(candidate):
            return candidate

    return None


def main():
    n = int(input("Enter a natural number n: "))
    result = largest_prime_smaller_than(n)

    if result is None:
        print(f"No prime number smaller than {n} exists.")
    else:
        print(f"The largest prime number smaller than {n} is {result}.")


if __name__ == "__main__":
    main()
