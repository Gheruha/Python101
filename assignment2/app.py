def read_integer(message, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(message))
        except ValueError:
            print("⚠️ You must enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"⚠️ Enter a number greater than or equal to {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"⚠️ Enter a number less than or equal to {maximum}.")
        else:
            return value


def generate_list_random(number_list):
    from random import randint

    n = read_integer("Enter how many elements you want: ", minimum=1)

    number_list.clear()
    for _ in range(n):
        number_list.append(randint(0, 1000))

    print("✅ Generated list:", number_list)


def generate_list_manual(number_list):
    n = read_integer("Enter how many elements you want: ", minimum=1)

    number_list.clear()
    for x in range(n):
        elem = read_integer(f"[{x + 1}] Enter a natural number: ", minimum=0)
        number_list.append(elem)

    print("✅ Entered list:", number_list)


def binary_search(number_list, target):
    left = 0
    right = len(number_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if number_list[middle] == target:
            return middle
        elif number_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def search_menu(number_list, list_sorted):
    if not number_list:
        print("⚠️ Generate a list first.")
        return

    if not list_sorted:
        print("⚠️ Sort the list before using binary search.")
        return

    target = read_integer("Enter the number to search for: ", minimum=0)
    index = binary_search(number_list, target)

    if index == -1:
        print(f"{target} was not found in the list.")
    else:
        print(f"{target} was found at index {index} (indexes start at 0).")


def cocktail_sort(number_list, step):
    start = 0
    end = len(number_list) - 1
    swaps = 0

    while start < end:
        swapped = False

        for i in range(start, end):
            if number_list[i] > number_list[i + 1]:
                number_list[i], number_list[i + 1] = (
                    number_list[i + 1],
                    number_list[i],
                )
                swapped = True
                swaps += 1

                if swaps % step == 0:
                    print(f"After {swaps} swaps:", number_list)

        if not swapped:
            break

        end -= 1
        swapped = False

        for i in range(end, start, -1):
            if number_list[i - 1] > number_list[i]:
                number_list[i - 1], number_list[i] = (
                    number_list[i],
                    number_list[i - 1],
                )
                swapped = True
                swaps += 1

                if swaps % step == 0:
                    print(f"After {swaps} swaps:", number_list)

        start += 1

        if not swapped:
            break

    return number_list


def comb_sort(number_list, step):
    gap = len(number_list)
    swapped = True
    swaps = 0

    while gap > 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False

        for i in range(len(number_list) - gap):
            if number_list[i] > number_list[i + gap]:
                number_list[i], number_list[i + gap] = (
                    number_list[i + gap],
                    number_list[i],
                )
                swapped = True
                swaps += 1

                if swaps % step == 0:
                    print(f"After {swaps} swaps:", number_list)

    return number_list


def sort_menu(number_list):
    if not number_list:
        print("⚠️ Generate a list first.")
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

        step = read_integer("Display the list after how many swaps? ", minimum=1)

        selected_sort = switcher[sort_option]
        selected_sort(number_list, step)
        sorted_here = True

        print("✅ Sorted list:", number_list)


def main():
    number_list = []
    list_sorted = False

    switcher = {
        0: lambda: False,
        1: lambda: generate_list_random(number_list),
        2: lambda: generate_list_manual(number_list),
        3: lambda: search_menu(number_list, list_sorted),
        4: lambda: sort_menu(number_list),
    }

    print("💻 Assignment 02 - Searching. Sorting")
    while True:
        print("\n--------------------------------------------------")
        print("0. EXIT.")
        print("1. Generate a list of random natural numbers.")
        print("2. Generate a manual list of natural numbers.")
        print("3. Search for an item using Binary Search.")
        print("4. Sort the list using Cocktail Sort or Comb Sort.")

        menu_option = read_integer("Choose an option (0–4): ", 0, 4)
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
