# Challenge Implement Depth First Search

from lesson0 import Graph
from stacks import MyStack
# You can check the input graph in console tab


def dfs_traversal_helper(g, source, visited):
    result = ""
    visited[source] = True
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        currentNode = stack.pop()
        result += str(currentNode)
        temp = g.array[currentNode].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited


def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = [False] * num_of_vertices

    # Start from source
    result, visited = dfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result


if __name__ == "__main__":
    g = Graph(7)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        print(dfs_traversal(g, 1))
