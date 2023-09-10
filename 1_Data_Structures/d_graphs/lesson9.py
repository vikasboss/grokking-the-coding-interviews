# Challenge: Remove Edge


from lesson0 import Graph
from stacks import MyStack


def remove_edge(graph, source, dest):
    # If empty graph
    if len(graph.array) == 0:
        return graph
    # check if source valid
    if source >= len(graph.array) or source < 0:
        return graph
    # check if dest valid
    if dest >= len(graph.array) or dest < 0:
        return graph
    # Delete by calling delete on head of LinkedList
    # Note: the delete method caters for if the edge does not exist
    graph.array[source].delete(dest)
    return graph


if __name__ == "__main__":

    g = Graph(5)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 0)

    g.print_graph()

    remove_edge(g, 1, 3)

    g.print_graph()
