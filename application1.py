"""
Code for Questions in Application 1
https://class.coursera.org/algorithmicthink1-003/human_grading/view/courses/975649/assessments/31/submissions
"""
import project1
import matplotlib.pyplot as pyplot
import random
import dpa_algorithm


GRAPH_FILE = 'alg_phys-cite.txt'


def load_graph(filename):
    """
    loads a text file representation of a graph
    returns graph as a dictionary
    """
    new_graph = {}
    with open(filename) as file_in:
        for line in file_in:
            val = line.strip().split()
            node = int(val[0])
            edge_list = val[1:]
            edge_set = set([])
            for edge in edge_list:
                edge_set.add(int(edge))
            new_graph[node] = edge_set
    return new_graph


def normalise_in_degree_dist(dist_graph):
    """Normalises in-degree distriution and returns normalised dictionary"""
    normalised_dic = {}
    degree_total = float(sum(dist_graph.values()))
    for val in dist_graph:
        normalised_dic[val] = dist_graph[val] / degree_total
    return normalised_dic


def question1(dir_graph, show_value=True):
    """Generates plot required for question 1"""
    citation_dist = project1.in_degree_distribution(dir_graph)
    normalised_dist = normalise_in_degree_dist(citation_dist)
    if show_value:
        pyplot.plot(normalised_dist.keys(), normalised_dist.values(),
                    color='green', linestyle='None', marker='.', markersize=5)
        pyplot.xscale('log')
        pyplot.yscale('log')
        pyplot.xlabel('Number of Citations (scale = log10)')
        pyplot.ylabel('Frequency (scale = log10)')
        pyplot.title("Question 1\n"
                     "Citation Distribution for High-Energy Physics Papers")
        pyplot.grid(True)
        pyplot.show()
    return normalised_dist


def directed_er(nodes, probability):
    """
    Implemention of ER algorithm to generate random directed graphs
    Takes as input number of nodes
    and probability that an edge exists between two nodes
    outputs graph
    """
    er_graph = {}
    for node_no in range(nodes):
        er_graph[node_no] = set([])
    for tail in range(nodes):
        for head in range(nodes):
            if tail != head:
                edge_prob = random.random()
                if edge_prob < probability:
                    er_graph[tail].add(head)
    return er_graph


def question2():
    """generates random graphs of directed_er to explore patterns"""
    er_20_percent = normalise_in_degree_dist(project1.in_degree_distribution(
        directed_er(10000, 0.2)))
    er_50_percent = normalise_in_degree_dist(project1.in_degree_distribution(
        directed_er(10000, 0.5)))
    er_80_percent = normalise_in_degree_dist(project1.in_degree_distribution(
        directed_er(10000, 0.9)))
    pyplot.plot(er_20_percent.keys(), er_20_percent.values(), color='red',
                linestyle='None', marker='.', markersize=5)
    pyplot.plot(er_50_percent.keys(), er_50_percent.values(), color='blue',
                linestyle='None', marker='.', markersize=5)
    pyplot.plot(er_80_percent.keys(), er_80_percent.values(), color='green',
                linestyle='None', marker='.', markersize=5)
    pyplot.text(1500, 0.04, 'n=10000\np=0.2', color='red')
    pyplot.text(3500, 0.04, 'n=10000\np=0.5', color='blue')
    pyplot.text(6500, 0.04, 'n=10000\np=0.8', color='green')
    pyplot.xscale('log')
    pyplot.yscale('log')
    pyplot.xlabel('in_degree of node (scale = log10)')
    pyplot.ylabel('Frequency (scale = log10)')
    pyplot.title("Question 2\n"
                 "Sample results of ER Algorithm")
    pyplot.grid(True)
    pyplot.show()


def question3(graph):
    """Prints number of nodes and edges in citation graph"""
    print('nodes = ' + str(len(graph)))
    edges = 0
    for node in graph:
        edges += len(graph[node])
    print('edges = ' + str(edges))
    print('average out-degree: ' + str(edges/len(graph)))


def question4(nodes, degree, show_value=True):
    q4_graph = dpa_algorithm.dpa(nodes, degree)
    q4_normalised = normalise_in_degree_dist(project1.in_degree_distribution(
        q4_graph))
    if show_value:
        pyplot.loglog(q4_normalised.keys(), q4_normalised.values(),
                      color='magenta', linestyle='none', marker='.',
                      markersize=6)
        pyplot.title('Question 4\nIn-Degree Distribution of DPA(27770, 12)')
        pyplot.xlabel('In-Degrees (scale = log10)')
        pyplot.ylabel('Distribution (scale = log10)')
        pyplot.show()
    return q4_normalised


def question5(graph1, graph2):
    pyplot.loglog(graph2.keys(), graph2.values(), color='magenta',
                  linestyle='none', marker='+', markersize=5,
                  label='DPA Graph')
    pyplot.loglog(graph1.keys(), graph1.values(), color='green',
                  linestyle='none', marker='.', markersize=5,
                  label="Citation Graph")
    pyplot.title('Question5\nComparison of Citation Graph & DPA Graph')
    pyplot.xlabel('In-Degrees (scale = log10')
    pyplot.ylabel('Distribution (scale = log10')
    pyplot.legend(loc='upper right')
    pyplot.grid(True)
    pyplot.show()

if __name__ == '__main__':
    citation_graph = load_graph(GRAPH_FILE)
    q1_dist = question1(citation_graph, False)
    # question2()
    # question3(citation_graph)
    q4_dist = question4(27770, 12, False)
    question5(q1_dist, q4_dist)