"""
The Python Code in this file implements the various functions described as
part of Project 1.
"""

__author__ = 'Bala Sridhar'
__version__ = 'June 10, 2015'


EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]),
             4: set([1]), 5: set([2]), 6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]),
             4: set([1]), 5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """
    Return a dictionary that represents a complete Digraph for the given
    number of nodes.

    :param num_nodes: nodes in the graph.
    :return: the dictionary representing a complete directed graph.
    """
    graph_representation = {}
    for node in range(0, num_nodes):
        graph_representation[node] = set([])
        for node_entry in range(0, num_nodes):
            if node_entry is not node:
                graph_representation[node].add(node_entry)

    return graph_representation


def compute_in_degrees(digraph):
    """
    Compute In-Degree Dictionary for the given directed Graph.

    :param digraph: dictionary representation of a directed graph.
    :return: the dictionary representing the in-degree count for each node in
             the graph.
    """

    in_degrees_representation = dict.fromkeys(digraph.keys(), 0)
    for connected_nodes in digraph.itervalues():
        for entry in connected_nodes:
            in_degrees_representation[entry] += 1

    return in_degrees_representation


def in_degree_distribution(digraph):
    """
    Computes the un normalized distribution of the in-degrees of a
    directed graph.

    :param digraph: dictionary representation of a directed graph.
    :return: the dictionary representing the un normalized in-degree
             distribution for each in-degree count available in the
             directed graph.
    """

    in_degrees_rep = compute_in_degrees(digraph)
    in_degrees_distribution = dict.fromkeys(in_degrees_rep.values(), 0)
    for in_degree in in_degrees_rep.itervalues():
        in_degrees_distribution[in_degree] += 1

    return in_degrees_distribution


if __name__ == "__main__":
    print "\n\n"
    print "Graph: ", make_complete_graph(5)
    print "\n\n"
    print "In Degree Representation: ", compute_in_degrees(EX_GRAPH1)
    print "\n\n"
    print "In Degree Distribution: ", in_degree_distribution(EX_GRAPH1)