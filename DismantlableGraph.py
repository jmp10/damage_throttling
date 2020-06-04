import networkx as nx


# This function determines the closed neighborhood of a vertex v in a graph g.
def closed_neighborhood(g, v):
    cn = list(g.neighbors(v))
    cn += [v]
    return cn


# This function checks each vertex in g to determine if it is a corner, and returns the first one it finds (or returns
# False if none were found). To do so, it picks a vertex i, then picks a vertex j adjacent to i, then checks if every
# vertex adjacent to i is also in the closed neighborhood of j (note that i is already in the closed neighborhood of j
# by virtue of being adjacent to it).
def find_corner(g):
    vertices = list(g.nodes)
    for i in vertices:
        for j in list(g.neighbors(i)):
            if all(k in closed_neighborhood(g, j) for k in g.neighbors(i)):
                return i
    return False


# This function determines whether or not a graph g is dismantlable. It first runs find_corner; if that returns False,
# the while loop breaks. If it does return a vertex, the vertex and its incident edges are removed from g, and the loop
# continues. Once there are no corners left in g, if g is K_1, then it is dismantlable; otherwise, it is not.
def is_dismantlable(g):
    while True:
        corner = find_corner(g)
        if str(corner) == "False":
            break
        else:
            g.remove_node(corner)
    if len(list(g.nodes)) == 1:
        return True
    else:
        return False


def main():
    # The first eight graphs in this list are those with dmg_1(G)>1, whereas the remaining thirteen have dmg_1(G)=1.
    graphs_to_check = ["F?ov?", "F?q`o", "FCQb_", "FCRV?", "FCZb_", "FCpV?", "FCpbO", "FCpb_",
                       "F?`f_", "F?ov_", "F?q_w", "F?qdo", "F?re_", "F?reg", "FCQf?", "FCQf_",
                       "FCRbg", "FCXf?", "FCXfO", "FCZbg", "FCpbo"]
    for graph in graphs_to_check:
        graph_nx = nx.from_graph6_bytes(bytes(graph, encoding='utf-8'))  # convert from g6 to nx format
        print(str(graph) + " - " + str(is_dismantlable(graph_nx)))


if __name__ == "__main__":
    main()
