"""
code to answer question 7
"""

import closest_pair
import alg_project3_viz

URL = alg_project3_viz.DATA_111_URL

clust_list, data_table = closest_pair.create_cluster_list(URL)
test1 = closest_pair.hierarchical_clustering(clust_list,9)
print(closest_pair.compute_distortions(test1, data_table))
clust_list, data_table = closest_pair.create_cluster_list(URL)
test2 = closest_pair.kmeans_clustering(clust_list,9,5)
print(closest_pair.compute_distortions(test2, data_table))


