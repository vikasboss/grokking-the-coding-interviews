# Check if a Given Undirected Graph is Tree or not?


from lesson0 import Graph
from stacks import MyStack
# You can check the input graph in console tab


def is_tree(g):
    # All vertices unvisited
    visited = [False] * g.vertices

    # Check cycle using recursion stack
    # Also mark nodes visited to check connectivity
    if check_cycle(g, 0, visited, -1):
        return False

    # Check if all nodes we visited from the source (graph is connected)
    for i in range(len(visited)):
        # Graph is not connected
        if not visited[i]:
            return False
    # Not cycle and connected graph
    return True


def check_cycle(g, node, visited, parent):
    # Mark node as visited
    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node
    while adjacent:
        if not visited[adjacent.data]:
            if check_cycle(g, adjacent.data, visited, node):
                return True

        # If adjacent is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            # Cycle found
            return True
        adjacent = adjacent.next_element

    return False


if __name__ == "__main__":

    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print(is_tree(g))
