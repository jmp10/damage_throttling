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


# This function takes in a graph g as an input and determines if dmg_1(g)=1. To do so, it determines if there is any
# vertex where removing it and its neighbors from the graph results in a graph of disconnected vertices. If such a
# vertex exists, the cop can place on it, forcing the robber to place on a nonadjacent vertex and stay on that vertex
# the entire game, since the cop dominates all of the vertices adjacent to the robber.
def one_damage_equals_one(g):
    result = False
    edges = list(g.edges)
    vertices = list(g.nodes)
    for cop_placement in vertices:
        neighbors = list(g.neighbors(cop_placement))
        closed_neighborhood = neighbors + [cop_placement]
        h = nx.Graph()
        h.add_edges_from(edges)  # h is an identical copy of g, so that we do not remove vertices from g directly
        h.remove_nodes_from(closed_neighborhood)
        if len(h.edges) == 0:
            result = True
            break
    return result


def main():
    # List all of the graphs in graph7c.g6 (contains all connected order-7 graphs up to isomorphism in graph6 format).
    with open("graph7c.g6") as file:
        graph_list = [line.rstrip('\n') for line in file]

    for graph_g6 in graph_list:
        marker = "dmg1G=1"
        graph_nx = nx.from_graph6_bytes(bytes(graph_g6, encoding='utf-8'))  # convert graph from g6 to networkx format
        # If 2 vertices cannot dominate the graph, check if it's a tree/chordal/cycle, or if it has dmg_1(G)>1.
        if not domination_check(graph_nx, 2):
            if nx.is_tree(graph_nx):
                marker = " tree  "
            elif nx.is_chordal(graph_nx):
                marker = "chordal"
            elif nx.is_isomorphic(graph_nx, nx.cycle_graph(7)):
                marker = " cycle "
            elif not one_damage_equals_one(graph_nx):
                marker = "dmg1G>1"
            print(str(graph_g6) + " | " + str(marker) + " | " + str(graph_nx.edges()))


if __name__ == "__main__":
    main()
