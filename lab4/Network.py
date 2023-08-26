# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


import numpy as np
from matplotlib import pyplot as plt
import networkx as nx


class Network:
    def __init__(self, vectorS):
        self.numOfElements = vectorS
        self.numOfComparators = vectorS * (vectorS - 1) // 2
        self.comparators = np.random.randint(0, self.numOfElements - 1, size = (self.numOfComparators, 2))
        self.fitness = 0

    def sortVector(self, vector, vectorS):
        toSort = np.copy(vector)
        sorted = np.sort(toSort)

        for i in range(self.numOfComparators):
            first, second = self.comparators[i]
            if toSort[first] > toSort[second]:
                toSort[first], toSort[second] = toSort[second], toSort[first]
            if np.array_equal(toSort, sorted):
                self.numOfComparators = i + 1

        return toSort

    def mutation(self):
        n1 = np.random.randint(0, self.numOfElements)
        n2 = np.random.randint(0, self.numOfComparators - n1)
        self.comparators[n1], self.comparators[n2] = self.comparators[n2], self.comparators[n1]

    def draw(self):
        graph = nx.DiGraph()

        for i in range(self.numOfElements):
            graph.add_node(i)

        for i in range(len(self.comparators)):
            a, b = self.comparators[i]
            graph.add_edge(a, b)

        pos = {}
        for i in range(self.numOfElements):
            pos[i] = (0, i)

        for i in range(self.numOfElements):
            plt.plot([0, 1000 ], [i, i], 'k-', linewidth = 2)

        x_offset = 1
        y_offset = 0.5
        for i in range(len(self.comparators)):
            a, b = self.comparators[i]
            nx.draw_networkx_edges(
                graph,
                pos,
                edgelist = [(a, b)],
                edge_color = 'black',
                width = 2.0,
                arrows = False,
                connectionstyle = f"arc3, rad={0.2 + y_offset / 6}"
            )
            plt.plot([x_offset, x_offset], [a, b], 'k-', linewidth = 2)
            x_offset += 1

        plt.title("Sorting Network")
        plt.xlim(0, x_offset)
        plt.ylim(-1, self.numOfElements)
        plt.axis('off')

        plt.show()
