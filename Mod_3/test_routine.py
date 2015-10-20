"""
Testing stuff
"""

import closest_pair
import alg_cluster
import alg_project3_viz as viz


def create_cluster_list(url):
    data_table = viz.load_data_table(url)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    return singleton_list, data_table


def test_q7():
    clust_list, data_table = create_cluster_list(URL)
    print(closest_pair.compute_distortions(clust_list, data_table))
    test1 = closest_pair.hierarchical_clustering(clust_list,16)
    print(closest_pair.compute_distortions(test1, data_table))
    clust_list, data_table = create_cluster_list(URL)
    test2 = closest_pair.kmeans_clustering(clust_list,16,5)
    print(closest_pair.compute_distortions(test2, data_table))


# hier_clust = closest_pair.hierarchical_clustering(test_list, 16)

# print(closest_pair.compute_distortions(hier_clust, test_list))

URL = viz.DATA_290_URL

test_q7()
