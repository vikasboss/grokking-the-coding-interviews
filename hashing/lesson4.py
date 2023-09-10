# Challenge: Find Two Pairs in List such that a+b = c+d
def find_pair(my_list):
    result = []
    # Create a dictionary my_dict with the key being the sum
    # and the value being a pair, i.e key = 3 , value = {1,2}
    # Traverse all possible pairs in my_list and store sums in my_dict
    # If sum already exists then print out the two pairs.
    my_dict = dict()
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            added = my_list[i] + my_list[j]  # calculate sum
            # the 'in' operator on dict() item has a complexity of O(1)
            # This is due to hashing
            # On a list, the 'in' operator would have the complexity of O(n)
            if added not in my_dict:
                # If added is not present in dict then insert it with pair
                my_dict[added] = [my_list[i], my_list[j]]
            else:
                # added already present in the dictionay
                prev_pair = my_dict.get(added)
                # Since list elements are distinct, we don't
                # need to check if any element is common among pairs
                second_pair = [my_list[i], my_list[j]]
                result.append(prev_pair)
                result.append(second_pair)
                return result
    return result


if __name__ == '__main__':
    my_list = [3, 4, 7, 1, 12, 9, 0]
    print(find_pair(my_list))
