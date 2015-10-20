"""
Routines for assignment 3
"""

import alg_cluster
import closest_pair
import random
import matplotlib.pyplot as pyplot
import time


def gen_random_clusters(num_clusters):
    """
    creates a list of clusters where each cluster in this list corresponds to
    one randomly generated point in the square with corners (+/-1, +/-1)
    """
    cluster_list = []
    for idx in range(num_clusters):
        cluster_list.append(alg_cluster.Cluster(set([]),
                                                random.random() * 2 - 1,
                                                random.random() * 2 - 1,
                                                0, 0))
    cluster_list.sort(key=lambda cluster: cluster.horiz_center())
    return cluster_list

def question1():
    """
    plot graph for question 1
    """
    slow = []
    fast = []
    for idx in range(2, 201):
        pair_list_slow = gen_random_clusters(idx)
        pair_list_fast = pair_list_slow[:]
        start_time = time.time()
        closest_pair.slow_closest_pair(pair_list_slow)
        slow.append(time.time() - start_time)
        start_time = time.time()
        closest_pair.fast_closest_pair(pair_list_fast)
        fast.append(time.time() - start_time)
    pyplot.plot(range(2, 201), slow, color='red', linestyle='-',
                marker='None', label='slow_closest_pair')
    pyplot.plot(range(2, 201), fast, color='blue', linestyle='-',
                marker='None', label='fast_closest_pair')
    pyplot.xlabel('Number of clusters')
    pyplot.ylabel('Algorithm Running Time in secs')
    pyplot.title('Comparison of fast & slow closest pair algorithms'
                 '\nDesktop Python')
    pyplot.legend(loc='upper right')
    pyplot.grid(True)
    pyplot.show()


question1()
