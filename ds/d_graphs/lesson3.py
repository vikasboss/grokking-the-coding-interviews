# Challenge Detect Cycle in a Directed Graph

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
            if visited[neighbour_of_temp.data]:
                return visited, True
            else:
                stack.push(neighbour_of_temp.data)
                visited[neighbour_of_temp.data] = True
            neighbour_of_temp = neighbour_of_temp.next_element
    return visited, False


def detect_cycle(g):
    num_of_vertices = g.vertices
    if num_of_vertices <= 1:
        return False
    visited = [False]*num_of_vertices
    for i in range(num_of_vertices):
        if not visited[i]:
            visited, cycle_found = dfs_traversal(g, i, visited)
            if cycle_found:
                return True
    return False


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
        print(detect_cycle(g))
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
        g.add_edge(2, 1)
        print(detect_cycle(g))
