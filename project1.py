"""
Code required to implement Project 1
https://class.coursera.org/algorithmicthink1-003/wiki/graph_degree
"""

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {8: set([1, 2]),
             0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             9: set([0, 4, 5, 6, 7, 3])}


def make_complete_graph(num_nodes):
    """
    Takes num_nodes as input and returns a dictionary corresponding to a
    complete graph with that number of nodes
    """
    graph = {}
    for tail in range(num_nodes):
        for head in range(num_nodes):
            if tail == head:
                if tail not in graph:
                    graph[tail] = set([])
            elif tail in graph:
                graph[tail].add(head)
            else:
                graph[tail] = set([head])
    return graph


def compute_in_degrees(digraph):
    """
    Takes a directed graph (dictionary) as input and calculates the
    in-degree for each node
    returns a dictionary with each node and its in-degree
    """
    in_degree_dic = {}
    for node in digraph:
        in_degree_dic[node] = 0
    for node in digraph:
        for edge in digraph[node]:
                in_degree_dic[edge] += 1
    return in_degree_dic


def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes
    the unnormalized distribution of the in-degrees of the graph. The function
    returns a dictionary whose keys correspond to in-degrees of nodes
    """
    in_degree_dic = compute_in_degrees(digraph)
    distribution_dic = {}
    for node in in_degree_dic:
        if in_degree_dic[node] in distribution_dic:
            distribution_dic[in_degree_dic[node]] += 1
        else:
            distribution_dic[in_degree_dic[node]] = 1
    return distribution_dic
