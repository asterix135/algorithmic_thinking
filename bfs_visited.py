"""
Implementation of BFS_Visited and CC_Visited for week2 homework
"""

# Instructions: https://class.coursera.org/algorithmicthink1-003/wiki/Programming_assignment_3
# OwlTest: http://codeskulptor.appspot.com/owltest?urlTests=alg.module2_tests.py&urlPylintConfig=alg.pylint_config.py&imports=%7Balg:(alg_module2_graphs),poc:(poc_queue)%7D&
from collections import deque


def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and returns the
    set consisting of all nodes that are visited by a breadth-first search that
    starts at start_node.
    """
    visit_queue = deque()
    visited = set([start_node])
    visit_queue.append(start_node)
    while len(visit_queue) > 0:
        curr_node = visit_queue.popleft()
        for neighbor in ugraph[curr_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                visit_queue.append(neighbor)
    return visited


def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, where each
    set consists of all the nodes (and nothing else) in a connected component,
    and there is exactly one set in the list for each connected component in
    ugraph and nothing else.
    """
    remaining_nodes = []
    for node in ugraph.keys():
        remaining_nodes.append(node)
    conn_comps = []
    while len(remaining_nodes) > 0:
        node = remaining_nodes[0]
        current_cc = bfs_visited(ugraph, node)
        conn_comps.append(current_cc)
        for item in current_cc:
            remaining_nodes.remove(item)
    return conn_comps


def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer) of the
    largest connected component in ugraph.
    """
    max_size = 0
    cc_list = cc_visited(ugraph)
    for group in cc_list:
        if len(group) > max_size:
            max_size = len(group)
    return max_size


def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and
    iterates through the nodes in attack_order. For each node in the list,
    the function removes the given node and its edges from the graph and then
    computes the size of the largest connected component
    for the resulting graph.

    The function returns a list whose k+1th entry is the size of the largest
    connected component in the graph after the removal of the first k nodes in
    attack_order. The first entry (indexed by zero) is the size of the largest
    connected component in the original graph.
    """
    res_results = [largest_cc_size(ugraph)]
    for node in attack_order:
        del ugraph[node]
        for vertex in ugraph:
            ugraph[vertex].discard(node)
        res_results.append(largest_cc_size(ugraph))
    return res_results
