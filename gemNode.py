import anytree as at
import networkx as nx

class Node(at.Node):

    init = tuple
    gem = tuple
    base = tuple
    score = int
    turns_left = int
    last_score = int
    gem_left = int


    def __init__(self, init :'str' , parent=None , problem = None):
        super().__init__( init, parent=parent)
        self.problem = problem
        if parent :
            initList = eval(init)
            lastStep = tuple(initList[len(initList)-1])
            x , y , s = lastStep
            self.score = parent.get_score() +  s
            self.init = parent.get_init()
            self.gem = (x , y)
            self.turns_left = parent.get_turns_left() - (self.init_to_gem() + self.gem_to_base())
            self.last_score = parent.get_score()
            self.gem_left = parent.get_gem_left() - 1
        else:
            self.score = 0
            self.turns_left = problem.maxTurn
            self.base = problem.initial_state
            self.gem_left = problem.gemNum
        

    def get_init(self):
        return self.base
    
    def get_score(self):
        return self.score
    
    def get_turns_left(self):
        return self.turns_left

    def get_gem_left(self):
        return self.gem_left

    def init_to_gem(self):
        initx , inity = self.init
        gemx , gemy = self.gem
        return len(nx.shortest_path(self.problem.mapProblem.graph , source = f'{initx},{inity}' , target = f'{gemx},{gemy}')) - 1

    def gem_to_base(self):
        dlist = list()
        gemx , gemy = self.gem
        for i in range(len(self.problem.baseList)) :
            basex , basey = self.problem.baseList[i]
            d = len(nx.shortest_path(self.problem.mapProblem.graph , source =f'{gemx},{gemy}' , target= f'{basex},{basey}')) - 1
            dlist.append((d , i))
        dlist.sort(key=lambda x:x[0] , reverse=True)
        bestbase = dlist.pop()
        d , i = bestbase
        self.base = self.problem.baseList[i]
        return d

    def __lt__(self, other):
        if self.turns_left > 0 and other.turns_left > 0:
            if self.score > other.score:
                return True
            else:
                return False
        elif self.turns_left > 0 and other.turns_left < 0 :
            if self.score > other.last_score:
                return True
            else:
                return False
        elif self.turns_left < 0 and other.turns_left > 0:
            if self.last_score > other.score:
                return False
            else:
                return True
        else:
            if self.last_score > other.last_score:
                return True
            else:
                return False
