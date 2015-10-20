"""
Closest pair and clustering functions

Owltest Page: http://codeskulptor.appspot.com/owltest?urlTests=alg.module3_tests.py&urlPylintConfig=alg.pylint_config.py&imports={alg:%28alg_cluster%29}&

Instructions: https://class.coursera.org/algorithmicthink2-003/wiki/Project_3
"""

import alg_cluster


def slow_closest_pair(cluster_list):
    """
    Takes a list of Cluster objects and returns a closest pair where the pair
    is represented by the tuple (dist, idx1, idx2) with idx1 < idx2 where dist
    is the distance between the closest pair cluster_list[idx1] and
    cluster_list[idx2]. This function should implement the brute-force closest
    pair method described in SlowClosestPair from Homework 3.
    """
    closest_pair = (float('inf'), -1, -1)
    list_len = len(cluster_list)
    for idx1 in range(list_len):
        for idx2 in range(list_len):
            if idx1 != idx2:
                cluster1, cluster2 = cluster_list[idx1], cluster_list[idx2]
                cluster_dist = cluster1.distance(cluster2)
                if cluster_dist < closest_pair[0]:
                    closest_pair = (cluster_dist, idx1, idx2)
    return closest_pair


def fast_closest_pair(cluster_list):
    """
    Takes a list of Cluster objects and returns a closest pair where the pair
    is represented by the tuple (dist, idx1, idx2) with idx1 < idx2 where dist
    is the distance between the closest pair cluster_list[idx1] and
    cluster_list[idx2]. This function should implement the divide-and-conquer
    closest pair method described FastClosestPair from Homework 3.
    """
    list_len = len(cluster_list)
    if list_len <= 3:
        closest_pair = slow_closest_pair(cluster_list)
    else:
        split = list_len / 2
        left_list = cluster_list[:split]
        right_list = cluster_list[split:]
        closest_left = fast_closest_pair(left_list)
        closest_right = fast_closest_pair(right_list)
        min_halves = min(closest_left,
                         (closest_right[0],
                          closest_right[1] + split,
                          closest_right[2] + split))
        mid = 0.5 * (cluster_list[split - 1].horiz_center() +
                     cluster_list[split].horiz_center())
        min_cross = closest_pair_strip(cluster_list, mid, min_halves[0])
        closest_pair = min(min_halves, min_cross)
    return closest_pair


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Takes a list of Cluster objects and two floats horiz_center and half_width.
    horiz_center specifies the horizontal position of the center line for a
    vertical strip. half_width specifies the maximal distance of any point in
    the strip from the center line. This function should implement the helper
    function described in ClosestPairStrip from Homework 3 and return a tuple
    corresponding to the closest pair of clusters that lie in the specified
    strip. (Again the return pair of indices should be in ascending order.)

    As one important coding note, you will need to sort a list of clusters by
    the horizontal (as well as vertical) positions of the cluster centers. This
    operation can be done in a single line of Python using the sort method for
    lists by providing a key argument of the form:

    cluster_list.sort(key = lambda cluster: cluster.horiz_center())
    """
    index_list = [idx for idx in range(len(cluster_list))
                  if abs(cluster_list[idx].horiz_center() - horiz_center) <
                  half_width]
    index_list.sort(key=lambda idx0: cluster_list[idx0].vert_center())
    strip_len = len(index_list)
    closest_pair = (float('inf'), -1, -1)
    for idx1 in range(strip_len - 1):
        for idx2 in range(idx1 + 1, min(idx1 + 4, strip_len)):
            point1 = index_list[idx1]
            point2 = index_list[idx2]
            current_dist = (cluster_list[point1].distance(cluster_list[point2]),
                            min(point1, point2), max(point1, point2))
            closest_pair = min(closest_pair, current_dist)
    return closest_pair


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Takes a list of Cluster objects and applies hierarchical clustering as
    described in the pseudo-code HierarchicalClustering from Homework 3 to this
    list of clusters. This clustering process should proceed until num_clusters
    clusters remain. The function then returns this list of clusters.
    """
    list_len = len(cluster_list)
    while list_len > num_clusters:
        cluster_list.sort(key=lambda cluster: cluster.horiz_center())
        closest_pair = fast_closest_pair(cluster_list)
        cluster_list[closest_pair[1]].merge_clusters(
            cluster_list[closest_pair[2]])
        cluster_list.pop(closest_pair[2])
        list_len -= 1
    return cluster_list


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Takes a list of Cluster objects and applies k-means clustering as described
    in the pseudo-code KMeansClustering from Homework 3 to this list of
    clusters. This function should compute an initial list of clusters (line 2
    in the pseudo-code) with the property that each cluster consists of a
    single county chosen from the set of the num_cluster counties with the
    largest populations. The function should then compute num_iterations of
    k-means clustering and return this resulting list of clusters.

    As you implement KMeansClustering, here are a several items to keep in mind.
    In line 4, you should represent an empty cluster as a Cluster object whose
    set of counties is empty and whose total population is zero. The cluster
    centers muf, computed by lines 2 and 8-9, should stay fixed as lines 5-7 are
    executed during one iteration of the outer loop. To avoid modifying these
    values during execution of lines 5-7, you should consider storing these
    cluster centers in a separate data structure. Line 7 should be implemented
    using the merge_clusters method from the Cluster class. merge_clusters will
    automatically update the cluster centers to their correct locations based
    on the relative populations of the merged clusters.
    """
    list_len = len(cluster_list)
    # initialize cluster centres to largest population counties
    index_by_pop = list(range(list_len))
    index_by_pop.sort(reverse=True,
                      key=lambda idx: cluster_list[idx].total_population())
    clust_ctrs = []
    for idx in range(num_clusters):
        clust_ctrs.append(cluster_list[index_by_pop[idx]])

    # Main loop in algorithm
    for dummy_idx0 in range(num_iterations):
        # 4. initialize k empty sets C1 ... Ck
        new_clusters = [alg_cluster.Cluster(set([]), 0, 0, 0, 0)
                        for dummy_idx in range(num_clusters)]
        # 5. for every element in original list
        for pt_idx in range(list_len):
            # 6. find the centre it's closest to
            min_dist, closest_ctr = float('inf'), 0
            for clust_idx in range(num_clusters):
                dist = clust_ctrs[clust_idx].distance(cluster_list[pt_idx])
                if dist < min_dist:
                    min_dist, closest_ctr = dist, clust_idx
            # 7. Add element to the closest cluster
            new_clusters[closest_ctr].merge_clusters(cluster_list[pt_idx])
        # 8. Update clust_ctrs based on centre of new_clusters
        for idx in range(num_clusters):
            new_pos = (new_clusters[idx].horiz_center(),
                       new_clusters[idx].vert_center())
            clust_ctrs[idx] = alg_cluster.Cluster(set([]), new_pos[0],
                                                  new_pos[1],0,0)
        # clust_ctrs = new_clusters[:]

    # 10. return {C1 .. Ck}
    return new_clusters
