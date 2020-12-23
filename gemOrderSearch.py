from solution import solution
from gemNode import Node
class Search:
    def __init__(self, problem):
        self.frontier =[]
        self.problem = problem


    def start_search(self):
        root_node = Node('[]' , parent = None , problem = self.problem)
        self.frontier.append(root_node)
        self.recursive_search()
        self.frontier.sort()
        # for n in self.frontier:
        #     print(n.name)
        return self.frontier[0].name


    def recursive_search(self):
        # children = self.problem.expand_node(node.name ,node , self.problem)
        # for child in children:
        #     self.frontier.append(child)
        # self.frontier.sort(reverse=True)
        # if self.frontier[0].turns_left < 0 :
        # # tabdil if be for
        #     return self.frontier
        # else:
        #     return self.recursive_search(self.frontier.pop(0))


        for i in range(len(self.frontier)):
            if self.frontier[i].turns_left > 0 and self.frontier[i].gem_left > 0 :
                n = self.frontier.pop(i)
                children = self.problem.expand_node(n.name ,n , self.problem)
                for child in children:
                    self.frontier.append(child)
                self.recursive_search()
        
                
        

