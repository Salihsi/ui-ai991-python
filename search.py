from state_graph import StateSpace
from base import TurnData,AgentData,Action

def search(problem,limit):
    for i in range(len(limit)):
        result = depth_limited_search(problem, limit)
		if result != "cutoff":
			return result

def depth_limited_search(problem, limit):
	return recursive_dls(problem.initial_state, problem, limit)


def rucersive_dls(node,problem,limit):
    if problem.goal_test(node):
        return Solution(node)

    elif limit == 0 :
        return "Cutoff"

    else :
        children = problem.expand_node(node.name,node)
        for child in children :    
    
            result = recursive_dls(child,problem,limit-1) 
            if result != "failure" :
                return result
        return "failure"