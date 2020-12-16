import networkx as nx
import matplotlib.pyplot as plt
import copy
class Problem:
    initial_state = tuple
    actions = []
    G = nx.DiGraph()

    def __init__(self ,map, position):
        self.recursive_problem(map, True, position)
        nx.draw(self.G, with_labels=True)
        plt.savefig('problem.png')



    def recursive_problem(self, map, gemOrBase, position): 
        if gemOrBase :
            for i in range(len(map)):
                for j in range(len(map)):
                    if map[i][j].isdigit():
                        x , y = position
                        self.G.add_edge(f'{x},{y}' , f'{i},{j}')
                        self.actions.append([f'{x},{y}' , f'{i},{j}'])
                        newMap = copy.deepcopy(map)
                        newMap[i][j] = '.'
                        self.recursive_problem(newMap, False, tuple((i , j)))
            
        else :
            for i in range(len(map)):
                for j in range(len(map)):
                    x , y = position
                    if map[i][j] == 'a' :
                        self.G.add_edge(f'{x},{y}' , f'{i},{j}')
                        self.actions.append([f'{x},{y}' , f'{i},{j}'])
                        self.recursive_problem(map, True, tuple((i , j)))
            print(self.actions)
            self.actions = []

                


                    






