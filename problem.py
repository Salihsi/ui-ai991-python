import networkx as nx
import matplotlib.pyplot as plt
import copy
from gemNode import Node
class Problem:
    initial_state = tuple
    actions = []
    G = nx.DiGraph()
    baseList = list()
    maxTurn = int
    gemNum = 0

    def __init__(self ,map, position , mapProblem , max_turns):
        self.mapProblem = mapProblem
        self.initial_state = position
        self.positionSeq = []
        self.maxTurn = max_turns
        self.recursive_problem(map, True, self.positionSeq)
        #nx.draw(self.G, with_labels=True)
        #plt.savefig('problem.png')
        self.get_baseList(map)
        self.get_gemNum(map)

    def recursive_problem(self, map, gemOrBase, position): 
        if gemOrBase :
            for i in range(len(map)):
                for j in range(len(map)):
                    if map[i][j].isdigit():
                        positionCopy = position.copy()
                        positionCopy.append((i , j , self.get_score(int(map[i][j]))))
                        self.G.add_edge(str(position) , str(positionCopy))
                        newMap = copy.deepcopy(map)
                        newMap[i][j] = '.'
                        self.recursive_problem(newMap, True, positionCopy)     
        else :
            pass
            # for i in range(len(map)):
            #     for j in range(len(map)):
            #         if map[i][j] == 'a' :
            #             positionCopy = position.copy()
            #             positionCopy.append((i , j))
            #             self.G.add_edge(str(position) , str(positionCopy))
            #             self.recursive_problem(map, True, positionCopy)
                        
    def get_baseList(self , map):
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == 'a':
                    self.baseList.append((i , j))

    def get_gemNum(self, map):
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j].isdigit():
                    self.gemNum = self.gemNum + 1


    def get_score(self,gem):
        if gem == 0 :
            return 2
        elif gem == 1 :
            return 5
        elif gem == 2 :
            return 3
        elif gem == 3 :
            return 1
        else :
            return 10


    def expand_node(self, node_label, parentNode , p):
        neighbors = list(nx.neighbors(self.G, node_label))
        result = []
        for neighbor in neighbors:
            result.append(Node(neighbor, parent=parentNode , problem = p))
        return result
    
    # def expand_node_base(self, node_label, parentNode):
    #     neighbors = list(nx.neighbors(self.G, node_label))
    #     result = []
    #     for neighbor in neighbors:
    #         result.append(Node(neighbor, parent=parentNode))
    #     return result

                    






