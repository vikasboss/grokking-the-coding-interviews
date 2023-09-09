# Challenge: Find a "Mother Vertex" in a Directed Graph


from lesson0 import Graph
from stacks import MyStack
# You can check the input graph in console tab


def dfs_traversal(g, source, visited):
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    while not stack.is_empty():
        current_node = stack.pop()
        neighbour_of_temp = g.array[current_node].head_node
        while neighbour_of_temp is not None:
            if not visited[neighbour_of_temp.data]:
                stack.push(neighbour_of_temp.data)
                visited[neighbour_of_temp.data] = True
            neighbour_of_temp = neighbour_of_temp.next_element
    return visited


def find_mother_vertex(g):
    # Write - Your - Code
    num_of_vertices = g.vertices
    visited = [False]*num_of_vertices
    last_visited = None
    for i in range(num_of_vertices):
        if not visited[i]:
            last_visited = i
            visited = dfs_traversal(g, i, visited=visited)
    # check whther that last visited index is the one which has visited all the indices
    visited = [False]*num_of_vertices
    visited = dfs_traversal(g, last_visited, visited=visited)
    if any(not element for element in visited):
        return -1
    else:
        return last_visited


# Create helper functions here


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
        print(find_mother_vertex(g))
