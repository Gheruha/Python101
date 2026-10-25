from random import randint
from time import perf_counter

from algorithms import binary_search, cocktail_sort, comb_sort


def make_input(size, case):
    if case == "best":
        return list(range(size))
    if case == "worst":
        return list(range(size - 1, -1, -1))

    data = []
    for _ in range(size):
        data.append(randint(0, 10 * size))
    return data


def measure_search(data, target):
    # Check the answer before timing
    index = binary_search(data, target)
    if index == -1:
        if target in data:
            raise ValueError("Search missed an existing value.")
    else:
        if index < 0 or index >= len(data):
            raise ValueError("Search returned an invalid index.")
        if data[index] != target:
            raise ValueError("Search returned the wrong position.")

    # Repeat the same search because one search is too fast
    repetitions = 10000
    start = perf_counter()
    for _ in range(repetitions):
        binary_search(data, target)
    end = perf_counter()

    return (end - start) / repetitions


def measure_sort(algorithm, original):
    total_time = 0
    repetitions = 5
    expected = sorted(original)

    for _ in range(repetitions):
        data = original.copy()

        start = perf_counter()
        algorithm(data, None)  # None disables the A2 assignment sort swap displays.
        end = perf_counter()

        if data != expected:
            raise ValueError("The list was not sorted correctly.")
        total_time += end - start

    return total_time / repetitions


def print_result(name, size, duration, previous):
    if previous == 0:
        ratio = "-"
    else:
        ratio = f"{duration / previous:.2f}"

    print(f"{name:<16} {size:>6} {duration * 1000000:>14.3f} {ratio:>8}")


def run_experiment(case):
    size = 128
    previous_search = 0
    previous_cocktail = 0
    previous_comb = 0

    print(f"\n{case.upper()} CASE")
    if case == "random":
        print("Random integers from 0 to 10*n inclusive; duplicates allowed.")
        print("One random search target per size, from the same range.")
    if case == "worst":
        print("Comb Sort uses reverse order as a challenge.")
    print(f"{'Algorithm':<16} {'Size':>6} {'Mean time (us)':>14} {'Ratio':>8}")

    for _ in range(5):
        original = make_input(size, case)
        search_data = sorted(original)

        if case == "best":
            target = search_data[(size - 1) // 2]
        elif case == "worst":
            target = search_data[-1] + 1
        else:
            target = randint(0, 10 * size)

        search_time = measure_search(search_data, target)
        cocktail_time = measure_sort(cocktail_sort, original)
        comb_time = measure_sort(comb_sort, original)

        print_result("Binary Search", size, search_time, previous_search)
        print_result("Cocktail Sort", size, cocktail_time, previous_cocktail)
        print_result("Comb Sort", size, comb_time, previous_comb)
        print()

        previous_search = search_time
        previous_cocktail = cocktail_time
        previous_comb = comb_time
        size *= 2


def best_case():
    run_experiment("best")


def random_case():
    run_experiment("random")


def worst_case():
    run_experiment("worst")
