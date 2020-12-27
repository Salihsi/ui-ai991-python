from state_graph import StateSpace
from solution import solution
from aStarNode import a_Node
class ASearch:
    def __init__(self, problem):
        self.frontier =[]
        self.explored =[]
        self.problem = problem

    def start_search(self):
        root_node = a_Node(self.problem.initial_state , goal=self.problem.goal)
        return self.recursive_search(root_node)

    def recursive_search(self, node):
        self.explored.append(node)
        if self.problem.goal_test(node):
            rs = (solution(node) , node)
            return rs
        else:    
            children = self.problem.expand_node_a(node.name ,node)
            for child in children:
                if not child in self.explored:
                    self.frontier.append(child)
            if not self.frontier:
                return "failure"
            self.frontier.sort(reverse=True)
            return self.recursive_search(self.frontier.pop())