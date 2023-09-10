# Challenge: First Non-Repeating Integer in a List - Hashing


def findFirstUnique(lst):
    # Write your code here
    dicti = dict()
    for element in lst:
        occurence = dicti.get(element, 0)
        occurence += 1
        dicti[element] = occurence
    for element in lst:
        occurence = dicti.get(element, 0)
        if occurence == 1:
            return element
    return -1


if __name__ == '__main__':
    lst = [9, 2, 3, 2, 6, 6]
    lst2 = [9, 4, 5, 1, 2, 0, 4]
    print(findFirstUnique(lst))
    print(findFirstUnique(lst2))
