# Challenge: Detect Loop in a Linked List - Hashing

from LinkedList import LinkedList, Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def detect_loop(lst):
    # Used to store nodes which we already visited
    visited_nodes = set()
    current_node = lst.get_head()

    # Traverse the set and put each node in the visitedNodes set
    # and if a node appears twice in the map
    # then it means there is a loop in the set
    while current_node:
        if current_node in visited_nodes:
            return True
        visited_nodes.add(current_node)  # Insert node in visitedNodes set
        current_node = current_node.next_element
    return False


if __name__ == '__main__':
    lst = LinkedList()

    lst.insert_at_head(21)
    lst.insert_at_head(14)
    lst.insert_at_head(7)
    print(detect_loop(lst))

    head = lst.get_head()
    node = lst.get_head()

    # Adding a loop
    for i in range(4):
        if node.next_element is None:
            node.next_element = head.next_element
            break
        node = node.next_element

    print(detect_loop(lst))
