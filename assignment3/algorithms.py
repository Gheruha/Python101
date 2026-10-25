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
                if step is not None:
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
                if step is not None:
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
                if step is not None:
                    swaps += 1
                    if swaps % step == 0:
                        print(f"After {swaps} swaps:", number_list)

    return number_list
