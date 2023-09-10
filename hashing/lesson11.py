from LinkedList import LinkedList, Node


def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    unique_values = set()
    result = LinkedList()

    start = list1.get_head()

    # Traverse the first list till the tail
    while start:
        unique_values.add(start.data)
        start = start.next_element

    start = list2.get_head()

    # Traverse the second list till the tail
    while start:
        unique_values.add(start.data)
        start = start.next_element

    # Add elements of unique_vales to result
    for x in unique_values:
        result.insert_at_head(x)
    return result


def intersection(list1, list2):

    result = LinkedList()
    visited_nodes = set()  # Keep track of all the visited nodes
    current_node = list1.get_head()

    # Traversing list1 and adding all unique nodes into the hash set
    while current_node is not None:
        value = current_node.data
        if value not in visited_nodes:
            visited_nodes.add(value)  # Visiting current_node for first time
        current_node = current_node.next_element

    start = list2.get_head()

    # Traversing list 2
    # Nodes which are already present in visited_nodes are added to result
    while start is not None:
        value = start.data
        if value in visited_nodes:
            result.insert_at_head(start.data)
        start = start.next_element
    result.remove_duplicates()
    return result


if __name__ == '__main__':
    ulist1 = LinkedList()
    ulist2 = LinkedList()
    ulist1.insert_at_head(8)
    ulist1.insert_at_head(22)
    ulist1.insert_at_head(15)

    ulist2.insert_at_head(21)
    ulist2.insert_at_head(14)
    ulist2.insert_at_head(15)
    ulist2.insert_at_head(7)

    new_list = union(ulist1, ulist2)

    new_list.print_list()

    ilist1 = LinkedList()
    ilist2 = LinkedList()

    ilist1.insert_at_head(14)
    ilist1.insert_at_head(22)
    ilist1.insert_at_head(15)

    ilist2.insert_at_head(21)
    ilist2.insert_at_head(14)
    ilist2.insert_at_head(15)

    lst = intersection(ilist1, ilist2)
    lst.print_list()
