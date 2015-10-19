"""
Closest pair functions

For this part of the Project, your task is to implement the two algorithms for
computing closest pairs discussed in Homework 3. For the fast method, you will
also implement its helper function separately to make debugging/testing your
code easier. Your implementations should work on lists of Cluster objects and
compute distances between clusters using the distance method.
"""

import cluster_class as cluster


def slow_closest_pair(cluster_list):
    """
     Takes a list of Cluster objects and returns a closest pair where the pair
     is represented by the tuple (dist, idx1, idx2) with idx1 < idx2 where dist
     is the distance between the closest pair cluster_list[idx1] and
     cluster_list[idx2]. This function should implement the brute-force closest
     pair method described in SlowClosestPair from Homework 3.
    """
    pass


def fast_closest_pair(cluster_list):
    """
    Takes a list of Cluster objects and returns a closest pair where the pair
    is represented by the tuple (dist, idx1, idx2) with idx1 < idx2 where dist
    is the distance between the closest pair cluster_list[idx1] and
    cluster_list[idx2]. This function should implement the divide-and-conquer
    closest pair method described FastClosestPair from Homework 3.
    """
    pass


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
    pass
