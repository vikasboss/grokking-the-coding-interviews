# Challenge: Find the Maximum Product of Two Integers in a List
# Decimal library to assign infinite numbers
from decimal import Decimal
import sys


def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """
    first_largest = -sys.maxsize - 1
    second_largest = -sys.maxsize - 1
    first_smallest = sys.maxsize
    second_smallest = sys.maxsize
    for element in lst:
        if element < 0:
            if element <= first_smallest:
                second_smallest = first_smallest
                first_smallest = element
            elif element < second_smallest:
                second_smallest = element
        else:
            if element >= first_largest:
                second_largest = first_largest
                first_largest = element
            elif element > second_largest:
                second_largest = element
    result1 = 0
    result2 = 0
    if first_largest >= 0 and second_largest >= 0:
        result1 = first_largest*second_largest
    if first_smallest < 0 and second_smallest < 0:
        result2 = first_smallest*second_smallest
    if result1 > result2:
        return first_largest, second_largest
    else:
        return first_smallest, second_smallest


if __name__ == "__main__":
    lst = [1, 3, 5, 2, 6]
    print(find_max_prod(lst))
    print(find_max_prod([1, 2, 3, 4, 5, 6, 7, 8]))
    print(find_max_prod([0, 1, 0, 1, 0, 1]))
