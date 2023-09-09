# Challenge: Find the Shortest Path Between Two Vertices


from lesson0 import Graph
from stacks import MyStack
# You can check the input graph in console tab
min_distance = 999999999


def dfs(g, source, destination, visited, distance=0):
    global min_distance
    visited[source] = True
    if source == destination:
        min_distance = min(distance, min_distance)
    adjacent = g.array[source].head_node
    while adjacent:
        if not visited[adjacent.data]:
            dfs(g, source=adjacent.data, destination=destination,
                visited=visited, distance=distance+1)
        adjacent = adjacent.next_element


def find_min(g, source, destination):
    # Write your code here
    if source == destination:
        return 0
    visited = [False]*g.vertices
    dfs(g, source, destination, visited)
    return -1 if min_distance == 999999999 else min_distance


if __name__ == "__main__":

    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 5)
    g.add_edge(2, 4)
    g.add_edge(5, 4)

    print(find_min(g, 0, 4))
