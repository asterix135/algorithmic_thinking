"""
Supporting function for Application 3
"""
import test_graphs_mod2


def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph


def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)



def fast_targeted_order(ugraph):
    """
    Compute a targeted attack order consisting of nodes of maximal degree
    returns a list of nodes
    """
    # Copy graph so as not to mutate original
    newgraph = copy_graph(ugraph)
    # Initialize degree_sets - list of all nodes whose degree is k
    degree_sets = [set([]) for dummy_ctr in range(len(newgraph))]
    for node in newgraph:
        node_degree = len(newgraph[node])
        degree_sets[node_degree].add(node)
    attack_order = []
    for degree in range(len(newgraph)-1, -1, -1):
        while len(degree_sets[degree]) > 0:
            active_node = degree_sets[degree].pop()
            for neighbor in newgraph[active_node]:
                neighbor_degree = len(newgraph[neighbor])
                degree_sets[neighbor_degree].discard(neighbor)
                degree_sets[neighbor_degree-1].add(neighbor)
            attack_order.append(active_node)
            delete_node(newgraph, active_node)
    return attack_order

if __name__ == '__main__':
    graph0 = test_graphs_mod2.GRAPH10
    print(fast_targeted_order(graph0))