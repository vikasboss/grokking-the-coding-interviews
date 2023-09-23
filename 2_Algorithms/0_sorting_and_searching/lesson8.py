# Challenge: Search Position


def search_insert_position(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = low+(high-low)//2
        if value == lst[mid]:
            return mid
        elif value < lst[mid]:
            high = mid-1

        else:
            low = mid+1
    return low


if __name__ == "__main__":
    lst = [1, 3, 5, 6]
    value = 5
    print(search_insert_position(lst, value=value))
