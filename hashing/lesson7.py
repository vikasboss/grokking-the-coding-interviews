# Challenge: Find Two Numbers that Add up to "k" - Hashing


def findSum(lst, k):
    # Write your code here
    dicti = dict()
    for element in lst:
        if dicti.get(k-element, None) is None:
            dicti[element] = True
        else:
            return [k-element, element]
    return None


if __name__ == '__main__':
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81
    print(findSum(lst, k))
