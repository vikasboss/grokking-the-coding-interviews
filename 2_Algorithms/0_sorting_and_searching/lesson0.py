def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]


def bubble_sort(lst):
    """
    Bubble sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through all list elements
    for i in range(len(lst)):

        # Last i elements are already in place
        for j in range(0, len(lst) - i - 1):

            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
            # Checking if any element was left
            while i < len(left):
                lst[k] = left[i]
                i += 1
                k += 1

            # Checking if any element was right
            while j < len(right):
                lst[k] = right[j]
                j += 1
                k += 1


    # Driver code to test above
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)

    lst = [3, 2, 1, 5, 4]
    bubble_sort(lst)  # Calling bubble sort function

    print("Sorted list is: ", lst)

    lst = [3, 2, 1, 5, 4]
    merge_sort(lst)

    print("Sorted list is: ", lst)
