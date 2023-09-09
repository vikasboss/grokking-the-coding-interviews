# Challenge: Implement Breadth First Search

# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex
from lesson0 import Graph
from queueC import MyQueue


def bfs_traversal_helper(g, source, visited):
    result = ""
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True
    while not queue.is_empty():
        currentNode = queue.dequeue()
        result += str(currentNode)
        temp = g.array[currentNode].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited


def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    visited = [False]*num_of_vertices
    # Write - Your - Code
    # For the above graph, it should return "01234" or "02143" etc

    result, visited = bfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result


if __name__ == "__main__":
    g = Graph(4)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        print(bfs_traversal(g, 0))

'''
0->2 1 
1-> 4 3 



'''
