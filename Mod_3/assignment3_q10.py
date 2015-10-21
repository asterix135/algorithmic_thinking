"""
code to answer question 10
"""

import closest_pair
import alg_project3_viz as viz
import matplotlib.pyplot as pyplot


def answer_q10():
    """
    generates clusters, figure out distoration and return x & y values
    """
    data_sources = [viz.DATA_111_URL, viz.DATA_290_URL, viz.DATA_896_URL]
    x_vals = range(6, 21)
    y_vals_hier = {}
    y_vals_kmean = {}
    for idx in range(len(data_sources)):
        # 0. Generate data_field & cluster_list
        clust_list, data_table = closest_pair.create_cluster_list(
            data_sources[idx])
        y_vals_hier[idx] = []
        # 1. calculate values for hierarchical - decreasing order
        for clust_size in reversed(x_vals):
            clust_list = closest_pair.hierarchical_clustering(clust_list,
                                                              clust_size)
            clust_error = closest_pair.compute_distortions(clust_list,
                                                           data_table)
            y_vals_hier[idx].insert(0, clust_error)
        # 2. calculate values for kmeans - decreasing order
        y_vals_kmean[idx] = []
        for clust_size in x_vals:
            clust_list, data_table = closest_pair.create_cluster_list(
                data_sources[idx])
            clust_list = closest_pair.kmeans_clustering(clust_list,
                                                        clust_size, 5)
            clust_error = closest_pair.compute_distortions(clust_list,
                                                           data_table)
            y_vals_kmean[idx].append(clust_error)
    return x_vals, y_vals_hier, y_vals_kmean


def plot_q10(x_val, y_val1, y_val2):
    """
    Generates plot for answer
    """
    num_counties = [111, 290, 896]
    for idx in range(3):
        pyplot.plot(x_val, y_val1[idx], color='red', linestyle='-',
                    marker=None, label='Hierarchical Clustering')
        pyplot.plot(x_val, y_val2[idx], color='blue', linestyle='-',
                    marker=None, label='k-Means Clustering (5 iterations)')
        pyplot.xlabel('Number of Clusters')
        pyplot.ylabel('Distortion Value (note scale at top of axis)')
        pyplot.title('Comparative Distortion Results for {ctynum}-County Data\nDesktop Python'.format(ctynum=num_counties[idx]))
        pyplot.legend(loc='upper right')
        pyplot.grid(True)
        pyplot.show()


if __name__ == '__main__':
    x_range, y_val_h, y_val_k = answer_q10()
    plot_q10(x_range, y_val_h, y_val_k)
