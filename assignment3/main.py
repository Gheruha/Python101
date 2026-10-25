from algorithms import binary_search, cocktail_sort, comb_sort
from cases import best_case, random_case, worst_case


def read_integer(message, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("You must enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Enter a number greater than or equal to {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"Enter a number less than or equal to {maximum}.")
        else:
            return value


def generate_list_random(number_list):
    from random import randint

    n = read_integer("Enter how many elements you want: ", minimum=1)

    number_list.clear()
    for _ in range(n):
        number_list.append(randint(0, 1000))

    print("Generated list:", number_list)


def generate_list_manual(number_list):
    n = read_integer("Enter how many elements you want: ", minimum=1)

    number_list.clear()
    for x in range(n):
        elem = read_integer(f"[{x + 1}] Enter a natural number: ", minimum=0)
        number_list.append(elem)

    print("Entered list:", number_list)


def search_menu(number_list, list_sorted):
    if not number_list:
        print("Generate a list first.")
        return

    if not list_sorted:
        print("Sort the list before using binary search.")
        return

    target = read_integer("Enter the number to search for: ", minimum=0)
    index = binary_search(number_list, target)

    if index == -1:
        print(f"{target} was not found in the list.")
    else:
        print(f"{target} was found at index {index} (indexes start at 0).")


def sort_menu(number_list):
    if not number_list:
        print("Generate a list first.")
        return

    switcher = {
        1: cocktail_sort,
        2: comb_sort,
    }

    sorted_here = None

    while True:
        print("\nSorting algorithms MENU.")
        print("0. Return to the main menu.")
        print("1. Select Cocktail Sort.")
        print("2. Select Comb Sort.")

        sort_option = read_integer("Choose an option (0–2): ", 0, 2)

        if sort_option == 0:
            return sorted_here

        step = read_integer("Display the list after how many swaps: ", minimum=1)

        selected_sort = switcher[sort_option]
        selected_sort(number_list, step)
        sorted_here = True

        print("Sorted list:", number_list)


def main():
    number_list = []
    list_sorted = False

    switcher = {
        0: lambda: False,
        1: lambda: generate_list_random(number_list),
        2: lambda: generate_list_manual(number_list),
        3: lambda: search_menu(number_list, list_sorted),
        4: lambda: sort_menu(number_list),
        5: lambda: best_case(),
        6: lambda: random_case(),
        7: lambda: worst_case(),
    }

    print("MENU")
    while True:
        print("\n--------------------------------------------------")
        print("0. EXIT.")
        print("1. Generate a list of random natural numbers.")
        print("2. Generate a manual list of natural numbers.")
        print("3. Search for an item using Binary Search.")
        print("4. Sort the list using Cocktail Sort or Comb Sort.")
        print(
            "5. Illustrate the runtime for the Searching and Sorting algorithms (BEST CASE)"
        )
        print(
            "6. Illustrate the runtime for the Searching and Sorting algorithms (RANDOM CASE)"
        )
        print(
            "7. Illustrate the runtime for the Searching and Sorting algorithms (WORST CASE)"
        )

        menu_option = read_integer("Choose an option (0–7): ", 0, 7)
        selected_function = switcher[menu_option]
        result = selected_function()

        if result is False:
            break

        if menu_option in (1, 2):
            list_sorted = False
        elif menu_option == 4 and result is True:
            list_sorted = True


if __name__ == "__main__":
    main()
