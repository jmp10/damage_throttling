import networkx as nx
import itertools


# This function finds all placements of k cops such that the robber can never place a distance d away from all cops. It
# takes in as inputs a graph g, the number of cops k, and the desired distance d, and outputs all "bad" cop placements
# where the robber cannot place d away from all cops at once.
def k_cops_at_dist_d(g, k, d):
    vertices = list(g.nodes)
    all_cop_placements = itertools.combinations_with_replacement(vertices, k)
    bad_cop_placements = []
    for cop_placement in all_cop_placements:
        num_bad_vertices = 0
        for robber_location in vertices:
            robber_is_far = True
            for cop_location in cop_placement:
                r_to_c_distance = nx.shortest_path_length(g, source=robber_location, target=cop_location)
                if r_to_c_distance < d:  # if the robber is closer than d to any cop, record a bad vertex
                    robber_is_far = False
            if not robber_is_far:
                num_bad_vertices += 1
        # if for every possible placement the robber is too close to each cop, then the cop placement is marked as bad
        if num_bad_vertices == len(vertices):
            bad_cop_placements += [cop_placement]
    return bad_cop_placements


def main():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4),
                      (4, 5), (5, 7), (7, 9), (9, 11), (11, 10), (10, 8), (8, 6), (6, 4),
                      (11, 12), (11, 13), (12, 14), (13, 14)
                      ])

    print(k_cops_at_dist_d(G, 2, 4))  # prints all placements of 2 cops s.t. R is always less than 4 away from a cop
    print(k_cops_at_dist_d(G, 3, 3))  # prints all placements of 3 cops s.t. R is always less than 3 away from a cop


if __name__ == "__main__":
    main()
