# Challenge: Dutch National Flag Problem


def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """
    low = 0
    high = len(lst)-1
    mid = 0
    print(lst)
    while mid <= high:
        if lst[mid] == 0:
            lst[mid], lst[low] = lst[low], lst[mid]
            low += 1
            mid += 1
        elif lst[mid] == 1:
            mid += 1
        elif lst[mid] == 2:
            lst[high], lst[mid] = lst[mid], lst[high]
            high -= 1
    return lst


if __name__ == "__main__":
    lst = [2, 0, 0, 1, 2, 1, 0]
    print(dutch_national_flag(lst))
