# Challenge: A List as a Subset of Another List

def is_subset(list1, list2):
    # Write your code here
    set1 = set()
    for item in list1:
        set1.add(item)
    for element in list2:
        if element not in set1:
            return False
    return True


if __name__ == '__main__':
    list1 = [9, 4, 7, 1, -2, 6, 5]
    list2 = [7, 1, -2]
    print(is_subset(list1, list2))
    list3 = [7, 1, -2, 11]
    print(is_subset(list1, list3))
