# Challenge: Find Two Numbers That Add Up to "n"

def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    # Write your code here!
    lst.sort()
    i = 0
    j = len(lst)-1
    while i < j:
        if lst[i]+lst[j] < n:
            i += 1
        elif lst[i]+lst[j] > n:
            j -= 1
        else:
            return [lst[i], lst[j]]
    return [-1]


if __name__ == "__main__":
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    n = 81
    print(find_sum(lst, n))
