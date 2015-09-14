"""
Algorithm to build a quadratically expanding hierarchical graph
and examine the in-degree distribution
"""

BASE_GRAPH = {0: set([1, 2, 3, 4]),
              1: set([0, 2, 4]),
              2: set([0, 1, 3]),
              3: set([0, 2, 4]),
              4: set([0, 1, 3])}
BASE_OUTER_LIST = [1, 2, 3, 4]

def build_graph(iterations):
    # TODO: This is a mess of iterations and copies the way its going: FIX IT!
    graph = BASE_GRAPH
    outer_list = BASE_OUTER_LIST
    next_node_number = len(graph) + 1
    for i in range(iterations):
        graph_copy = graph.copy()
        for j in range(4):
            new_graph = copy(graph, outer_nodes, next_node_number)
            new_outer_list = list(outer_list)
            graph_copy.update(new_graph[0])



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


if __name__ == '__main__':
    copy = copy_graph(BASE_GRAPH, BASE_OUTER_LIST, 5)
    print(BASE_GRAPH)
    print(copy[0])
    print(copy[1])

