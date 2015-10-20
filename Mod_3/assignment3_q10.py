"""
code to answer question 10
"""

import closest_pair
import alg_project3_viz as viz

def answer_q10():
    """
    generates clusters, figure out distoration and plots results
    """
    data_sources = [viz.DATA_111_URL, viz.DATA_290_URL, viz.DATA_896_URL]
    x_vals = range(6,21)
    for url in data_sources:
        # 0. Generate data_field & cluster_list
        clust_list, data_table = closest_pair.create_cluster_list(url)
        # 1. calculate values for hierarchical - decreasing order
        for clust_size in reversed(x_vals):
            clust_list = closest_pair.hierarchical_clustering(clust_list,clust_size)
