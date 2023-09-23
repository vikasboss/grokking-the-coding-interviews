# Challenge: Arrange a Binary List


def sort_binary_list(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """
    count0 = 0
    count1 = 0
    for element in lst:
        if element == 0:
            count0 += 1
        elif element == 1:
            count1 += 1
    for i in range(count0):
        lst[i] = 0
    for i in range(count1):
        lst[i+count0] = 1
    return lst


def sort_binary_list2(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """
    j = 0
    for i in range(len(lst)):
        if lst[i] < 1:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    return lst


if __name__ == "__main__":
    lst = [1, 0, 1, 0, 1, 1, 0, 0]
    print(sort_binary_list(lst))
    print(sort_binary_list2(lst))
