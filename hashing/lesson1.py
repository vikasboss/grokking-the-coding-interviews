# Challenge: Check if Lists are Disjoint

def is_disjoint(list1, list2):
    # Write your code here
    set1 = set(list1)  # Create set of list1 elements
    for element in list1:
        set1.add(element)
    for element in list2:
        if element in set1:
            return False
    return True


if __name__ == '__main__':
    list1 = [9, 4, 7, 1, -2, 6, 5]
    list2 = [7, 1, -2]
    print(is_disjoint(list1, list2))
    list3 = [98, 99]
    print(is_disjoint(list1, list3))
