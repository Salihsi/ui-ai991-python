import networkx as nx
import matplotlib.pyplot as plt
from node import Node
from aStarNode import a_Node
class StateSpace(object):

    def __init__(self, matrix, final=False):
        self.matrix = matrix
        self.graph = nx.Graph()
        self.initial_state = ''
        self.goal = []

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == '*':
                    continue
                else:
                    if matrix[i][j] == 'A':
                        if not final:
                            self.initial_state = f'{i},{j}'
                    elif matrix[i][j] == "a":
                        if final:
                            self.goal.append(f'{i},{j}')
                    elif matrix[i][j].isdigit():
                        if final:
                            self.initial_state = f'{i},{j}'
                        else:
                            self.goal.append(f'{i},{j}')

                    self._make_relations(matrix, i, j)

    def _indices_to_string(self, indices: list):
        a = indices[0]
        b = indices[1]
        return f'{a},{b}'

    def _string_to_indices(self, indices_string: str):
        indices = indices_string.split(',')
        first = int(indices[0])
        second = int(indices[1])
        return first, second

    def _make_relations(self, matrix, i, j):

        if j+1 < len(matrix) and matrix[i][j+1] != '*':
            self.graph.add_edge(f'{i},{j}', self._indices_to_string([i, j+1]))
        if i+1 < len(matrix) and matrix[i+1][j] != '*':
            self.graph.add_edge(f'{i},{j}', self._indices_to_string([i+1, j]))

    def show_image(self):
        nx.draw(self.graph, with_labels=True)
        plt.savefig('test_image.png')
        plt.show()

    
    def goal_test(self , node):
        if  node.name in self.goal :
            return True
        return False

    def expand_node(self, node_label, parentNode):
        neighbors = list(nx.neighbors(self.graph, node_label))
        result = []
        for neighbor in neighbors:
            result.append(Node(neighbor, parent=parentNode , goal=self.goal))
        return result

    def expand_node_a(self, node_label, parentNode):
        neighbors = list(nx.neighbors(self.graph, node_label))
        result = []
        for neighbor in neighbors:
            result.append(a_Node(neighbor, parent=parentNode , goal=self.goal))
        return result