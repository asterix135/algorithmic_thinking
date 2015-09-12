"""
Code required to implement Project 1
https://class.coursera.org/algorithmicthink1-003/wiki/graph_degree
Owltest page: http://codeskulptor.appspot.com/owltest?urlTests=alg.module1_tests.py&urlPylintConfig=alg.pylint_config.py&imports=%7Balg:(alg_module1_graphs)%7D&
"""

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {8: set([1, 2]),
             0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             9: set([0, 4, 5, 6, 7, 3])}
