"""
Code to create graphs for application 2
"""
import random
import upa_trial
import project1


def undirected_er(nodes, probability):
    """
    Implemention of ER algorithm to generate random undirected graphs
    Takes as input number of nodes
    and probability that an edge exists between two nodes
    outputs graph
    """
    er_graph = {}
    for node_no in range(nodes):
        er_graph[node_no] = set([])
    random.seed(123)
    for tail in range(nodes):
        for head in range(nodes):
            if tail != head:
                edge_prob = random.random()
                if edge_prob < probability:
                    er_graph[tail].add(head)
                    er_graph[head].add(tail)
    return er_graph


def upa(num_nodes, in_degree):
    """
    creates a random undirected graph with n nodes and average in-degree of m
    input: no_nodes (m) and in_degree(m) - both integers
    output: directed graph (dictionary, with edges as sets)
    """
    upa_graph = project1.make_complete_graph(in_degree)
    node_counter = upa_trial.UPATrial(in_degree)
    for new_node in range(in_degree, num_nodes):
        new_node_set = node_counter.run_trial(in_degree)
        upa_graph[new_node] = new_node_set
        for vertex in new_node_set:
            upa_graph[vertex].add(new_node)

    return upa_graph

