# Challenge: Trace the Complete Path of a Journey


def trace_path(my_dict):
    result = []
    # Create a reverse dict of the given dict i.e if the given dict has (N,C)
    # then reverse dict will have (C,N) as key-value pair
    # Traverse original dict and see if it's key exists in reverse dict
    # If it doesn't exist then we found our starting point.
    # After the starting point is found, simply trace the complete path
    # from the original dict.
    reverse_dict = dict()
    # To fill reverse dict, iterate through the given dict
    keys = my_dict.keys()
    for key in keys:
        reverse_dict[my_dict.get(key)] = key
    # Find the starting point of itinerary
    from_loc = None
    for key in keys:
        if key not in reverse_dict:
            from_loc = key
            break
            # Trace complete path
    to = my_dict.get(from_loc)
    while to is not None:
        result.append([from_loc, to])
        from_loc = to
        to = my_dict.get(to)
    return result


if __name__ == '__main__':
    my_dict = dict()
    my_dict["NewYork"] = "Chicago"
    my_dict["Boston"] = "Texas"
    my_dict["Missouri"] = "NewYork"
    my_dict["Texas"] = "Missouri"
    print(trace_path(my_dict))
