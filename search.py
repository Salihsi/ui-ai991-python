from state_graph import StateSpace
from base import TurnData,AgentData,Action
import itertools
from solution import solution
from node import Node
from counter import Counter

def search(problem):
    for depth in itertools.count(start=0):
        result = depth_limited_search(problem.initial_state , problem, depth)
        if result:
            return result

def depth_limited_search(node,problem,limit):
    root_node = Node(node)
    return recursive_dls(root_node,problem,limit)



def recursive_dls(node, problem, limit): 
    
    if problem.goal_test(node):
        print('expands : ' , Counter.get_counter())
        Counter.set_counter()
        return solution(node)
    elif limit == 0:
        return
    else:
        children = problem.expand_node(node.name, node)
        Counter.addcounter()   
        for child in children:
            result= recursive_dls(child, problem, limit-1)
            if result:
                return result
        return None

