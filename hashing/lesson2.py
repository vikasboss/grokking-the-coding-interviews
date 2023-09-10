# Challenge: Find Symmetric Pairs in a List


def find_symmetric(my_list):
    # Write your code here
    set1 = set()
    result = []
    for pair in my_list:
        pair_tuple = tuple(pair)  # Convert the list to a tuple
        if pair_tuple[::-1] in set1:
            result.append(list(pair_tuple[::-1]))
            result.append(list(pair_tuple))
        else:
            set1.add(pair_tuple)
    return result


if __name__ == '__main__':
    list1 = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
    print(find_symmetric(list1))
