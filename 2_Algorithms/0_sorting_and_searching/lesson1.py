def linear_search(lst, key):
    """
    Linear search function
    :param lst: lst of unsorted integers
    :param key: A key to be searched in the list
    """
    if len(lst) <= 0:  # Sanity check
        return -1

    for i in range(len(lst)):
        if lst[i] == key:
            return i  # If found return index
    return -1  # Return -1 otherwise


def binary_search(lst, left, right, key):
    """
    Binary search function
    :param lst: lst of unsorted integers
    :param left: Left sided index of the list
    :param right: Right sided index of the list
    :param key: A key to be searched in the list
    """

    while left <= right:

        mid = left + (right - left) // 2

        # Check if key is present at mid
        if lst[mid] == key:
            return mid

        # If key is greater, ignore left half
        elif lst[mid] < key:
            left = mid + 1

        # If key is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, then the element was not present
    return -1


# Driver code to test above
if __name__ == '__main__':

    lst = [5, 4, 1, 0, 5, 95, 4, -100, 200, 0]
    key = 95

    index = linear_search(lst, key)
    if index != -1:
        print("Key:", key, "is found at index:", index)
    else:
        print(key, " is not found in the list.")

    lst = [1, 2, 3, 10, 20, 40, 111, 244, 14444, 800000]
    key = 111

    # Function call
    result = binary_search(lst, 0, len(lst) - 1, key)

    if result != -1:
        print("Element is present at index:", result)
    else:
        print("Element is not present in the list")
