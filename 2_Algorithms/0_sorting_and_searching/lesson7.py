# Challenge: Search in a 2D List


def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Write your code here!
    pass
    m = len(lst)
    if m < 1:
        return False
    n = len(lst[0])
    low = 0
    high = m*n-1
    while low <= high:
        mid = low+(high-low)//2
        iIndexofMid = mid // m
        jIndexofMid = mid % n
        if lst[iIndexofMid][jIndexofMid] == number:
            return True
        elif number < lst[iIndexofMid][jIndexofMid]:
            high = mid-1
        else:
            low = mid+1
    return False


if __name__ == "__main__":
    lst = [[10, 11, 12, 13],
           [14, 15, 16, 17],
           [27, 29, 30, 31],
           [32, 33, 39, 50]]

    print(find_in(lst, 30))
