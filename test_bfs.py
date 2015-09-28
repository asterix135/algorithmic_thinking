import bfs_visited
import test_graphs_mod2a


def test1():
    print(bfs_visited.cc_visited(test_graphs_mod2a.GRAPH0))


def test2():
    print(bfs_visited.compute_resilience(test_graphs_mod2.GRAPH0, [1,2]))


if __name__ == '__main__':
    test2()
