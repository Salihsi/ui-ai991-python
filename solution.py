from base import Action
def solution(node):
    sequence = list()
    return recursive_sol(node,sequence) 

def recursive_sol(node,sequence):
    if node.parent:
        sequence.append(node.action)
        return recursive_sol(node.parent,sequence)
    else:
        return sequence