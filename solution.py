#we are at the result and the goal,so we want to get back to the root so we use the solution function
from base import Action
def solution(node,seq):
    seq.append(node.Action)
    if is not node.parent :
        return seq
    else :
        return solution(node.parent,seq) 
