# Challenge: Detect Loop in a Linked List - Hashing

from LinkedList import LinkedList, Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def remove_duplicates(lst):
    current_node = lst.get_head()
    prev_node = lst.get_head()
    # To store values of nodes which we already visited
    visited_nodes = set()
    # If List is not empty and there is more than 1 element in List
    if not lst.is_empty() and current_node.next_element:
        while current_node:
            value = current_node.data
            if value in visited_nodes:
                # current_node is already in the HashSet
                # connect prev_node with current_node's next element
                # to remove it
                prev_node.next_element = current_node.next_element
                current_node = current_node.next_element
                continue
            # Visiting currentNode for first time
            visited_nodes.add(current_node.data)
            prev_node = current_node
            current_node = current_node.next_element


if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_head(7)
    lst.insert_at_head(7)
    lst.insert_at_head(22)
    lst.insert_at_head(14)
    lst.insert_at_head(21)
    lst.insert_at_head(14)
    lst.insert_at_head(7)

    lst.print_list()

    remove_duplicates(lst)
    lst.print_list()
