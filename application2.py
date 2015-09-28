"""
Code to deal with application 2
https://class.coursera.org/algorithmicthink1-003/human_grading/view/courses/975649/assessments/32/submissions
"""

import app2_provided
import app2_create_graphs
import random
import bfs_visited
import matplotlib.pyplot as pyplot


# supplied graph has 1239 nodes and 3047 edges
# for upa, use m = 5
# for er use p = 0.002


def count_edges(ugraph):
    """
    counts number of edges in an undirected graph
    NOTE: this is 1/2 the actual number because each edge is represented 2x
    """
    edges = 0
    for node in ugraph:
        for dummy_edge in ugraph[node]:
            edges += 1
    return edges/2


def random_order(ugraph):
    """
    takes a graph and returns a list of the nodes of that graph in
    random order
    graph can be directed or undirected
    """
    new_order = ugraph.keys()
    random.seed(123)
    random.shuffle(new_order)
    return new_order


def question1():
    """
    create 3 graphs - subject each to the same random attack order
    plot the resulting largest cc for each
    """
    network_graph = app2_provided.load_graph(app2_provided.NETWORK_URL)
    attack_order = random_order(network_graph)
    network_resil = bfs_visited.compute_resilience(network_graph, attack_order)
    er_graph = app2_create_graphs.undirected_er(1239, 0.002)
    attack_order = random_order(er_graph)
    while count_edges(er_graph) < 2900 or count_edges(er_graph) > 3190:
        er_graph = app2_create_graphs.undirected_er(1239, 0.002)
    er_resil = bfs_visited.compute_resilience(er_graph, attack_order)
    upa_graph = app2_create_graphs.upa(1239, 3)
    attack_order = random_order(upa_graph)
    upa_resil = bfs_visited.compute_resilience(upa_graph, attack_order)

    pyplot.plot(range(1240), network_resil, color='red', linestyle='-',
                marker=None, label='Network Graph')
    pyplot.plot(range(1240), er_resil, color='blue', linestyle='-',
                marker=None, label='ER Graph, p=0.002')
    pyplot.plot(range(1240), upa_resil, color='green', linestyle='-',
                marker=None, label='UPA Graph, m=3')

    pyplot.title('Question 1\nComparison of Random Attack Graph Degradation')
    pyplot.xlabel('Number of Nodes Removed')
    pyplot.ylabel('Largest Connected Component')
    pyplot.legend(loc='upper right')
    pyplot.grid(True)
    pyplot.show()
    return network_resil, er_resil, upa_resil


def question2(resil1, resil2, resil3):
    """
    Calculates resiliency of three networks at 20% nodes removed
    """
    check_pt = int(len(resil1) * 0.2)
    resil_20_pct = 0.75 * max(resil1) * 0.8
    print('resilience check value = ' + str(resil_20_pct))
    print('network graph @20% = ' + str(resil1[check_pt]))
    print('er graph @20% = ' + str(resil2[check_pt]))
    print('upa graph @20% = ' + str(resil3[check_pt]))




if __name__ == '__main__':
    resil_lists = question1()
    question2(resil_lists[0], resil_lists[1], resil_lists[2])
