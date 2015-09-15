"""
Algorithm to build a quadratically expanding hierarchical graph
and examine the in-degree distribution
"""

import copy
import project1
import matplotlib.pyplot as pyplot

BASE_GRAPH = {0: set([1, 2, 3, 4]),
              1: set([0, 2, 4]),
              2: set([0, 1, 3]),
              3: set([0, 2, 4]),
              4: set([0, 1, 3])}
BASE_OUTER_LIST = [1, 2, 3, 4]


def build_graph(iterations):
    """
    Builds a hierarchical graph with a base of 5 nodes, with number of
    levels provided by iterations parameter
    """
    graph = BASE_GRAPH
    outer_list = BASE_OUTER_LIST
    next_node_number = len(graph)
    for i in range(iterations):
        graph_copy = copy.deepcopy(graph)
        outer_list_copy = list(outer_list)
        outer_list = []
        for j in range(4):
            new_graph = copy_graph(graph_copy, outer_list_copy, next_node_number)
            # add edges to and from 0 node
            for node in new_graph[1]:
                new_graph[0][node].add(0)
                graph[0].add(node)
            next_node_number += len(new_graph[0])
            graph.update(new_graph[0])
            outer_list.extend(new_graph[1])
    return graph


def copy_graph(graph, outer_nodes, nnn):
    """
    Creates a copy of an existing graph, with new node numbers
    :param graph (as a dictionary: node number: set):
    :param outer_nodes (list of outer nodes in graph):
    :param nnn (next node number):
    :return graph copy & list of outer nodes in copy:
    """
    new_graph = {}
    for node in graph:
        new_edges = set([edge + nnn for edge in graph[node]])
        new_graph[node + nnn] = new_edges
    new_outer_list = [node + nnn for node in outer_nodes]
    return new_graph, new_outer_list


def plot_graph(graph):
    """Creates log/log plot of degree distribution for a graph"""
    dist = project1.in_degree_distribution(graph)
    print(dist)
    pyplot.loglog(dist.keys(), dist.values(), color='blue', linestyle='none',
                  marker='.', markersize=10)
    pyplot.grid(True)
    pyplot.show()


if __name__ == '__main__':
    iterated = build_graph(6)
    plot_graph(iterated)

