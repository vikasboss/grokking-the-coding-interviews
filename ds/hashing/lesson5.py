# Challenge: A Sublist with a Sum of 0


def find_sub_zero(my_list):
    # Write your code here
    dicti = dict()
    curr_sum = 0
    for element in my_list:
        curr_sum += element
        if dicti.get(curr_sum, None) is not None:
            return True
        else:
            dicti[curr_sum] = True
    return False


if __name__ == '__main__':
    list1 = [6, 4, -7, 3, 12, 9]
    list2 = [-7, 4, 6, 3, 12, 9]
    print(find_sub_zero(list1))
    print(find_sub_zero(list2))
