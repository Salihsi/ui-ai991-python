#we are at the result and the goal,so we want to get back to the root so we use the solution function
from base import Action
def solution(node):
    sequence = list()
    return recursive_sol(node.parent,sequence) 

def recursive_sol(node,sequence):
    if node.parent:
        sequence.append(node.action)
        return recursive_sol(node.parent,sequence)
    else:
        return sequence