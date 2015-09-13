"""
Implementation of DPA Algorithm to build a synthetic directed graph
"""

import project1
import dpa_trial


def dpa(num_nodes, in_degree):
    """
    creates a random directed graph with n nodes and average in-degree of m
    input: no_nodes (m) and in_degree(m) - both integers
    output: directed graph (dictionary, with edges as sets)
    """
    dpa_graph = project1.make_complete_graph(in_degree)
    node_counter = dpa_trial.DPATrial(in_degree)
    for new_node in range(in_degree, num_nodes):
        dpa_graph[new_node] = node_counter.run_trial(in_degree)
    return dpa_graph


if __name__ == '__main__':
    print(dpa(10, 5))
