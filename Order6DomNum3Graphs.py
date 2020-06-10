import networkx as nx
import itertools


# This function takes in as inputs a graph g and a number of vertices s, and determines whether or not some set of s
# vertices can dominate g.
def domination_check(g, s):
    dominated = False
    vertices = list(g.nodes)
    subsets_of_size_s = [set(i) for i in itertools.combinations(vertices, s)]
    for vertex_set in subsets_of_size_s:
        if nx.is_dominating_set(g, vertex_set):
            dominated = True
            break
    return dominated


def main():
    # List all of the graphs in graph6c.g6 (contains all connected order-6 graphs up to isomorphism in graph6 format).
    with open("graph6c.g6") as file:
        graph_list = [line.rstrip('\n') for line in file]

    for graph_g6 in graph_list:
        graph_nx = nx.from_graph6_bytes(bytes(graph_g6, encoding='utf-8'))  # convert graph from g6 to networkx format
        # Check whether the graph can be dominated by a set of two vertices.
        if not domination_check(graph_nx, 2):
            print(str(graph_g6) + " | edges: " + str(graph_nx.edges()))


if __name__ == "__main__":
    main()
