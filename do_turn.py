from base import BaseAgent
from state_graph import StateSpace
from search import search

class uninformedagent (BaseAgent):
    sequence = []
    def do_turn(self, turn_data: TurnData) -> Action: nbv
    state = TurnData
    if sequence is empty:
        problem = StateSpace(map)
        sequence = search(problem)
        if sequence is "failure" :
            return None
    return sequence.pop()