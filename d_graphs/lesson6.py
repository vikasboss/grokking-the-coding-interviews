# Challenge Check if path exists in a Graph

from lesson0 import Graph
from stacks import MyStack
# You can check the input graph in console tab


def dfs_traversal(g, source, destination):
    num_of_vertices = g.vertices
    visited = [False]*num_of_vertices
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    while not stack.is_empty():
        current_node = stack.pop()
        neighbour_of_temp = g.array[current_node].head_node
        while neighbour_of_temp is not None:
            if not visited[neighbour_of_temp.data]:
                if destination == neighbour_of_temp.data:
                    return True
                stack.push(neighbour_of_temp.data)
                visited[neighbour_of_temp.data] = True
            neighbour_of_temp = neighbour_of_temp.next_element
    return False


def check_path(g, source, destination):
    if source == destination:
        return True
    return dfs_traversal(g, source=source, destination=destination)


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
        print(check_path(g, 1, 5))
        print(check_path(g, 5, 3))
