import random
from base import BaseAgent, TurnData, Action
from state_graph import StateSpace
from search import search

class uninformedagent(BaseAgent):

    def __init__(self):
        BaseAgent.__init__(self)
        self.sequence = []
        print(f"MY NAME: {self.name}")
        print(f"PLAYER COUNT: {self.agent_count}")
        print(f"GRID SIZE: {self.grid_size}")
        print(f"MAX TURNS: {self.max_turns}")
        print(f"DECISION TIME LIMIT: {self.decision_time_limit}")

    def do_turn(self, turn_data: TurnData) -> Action:
       
        print(turn_data.map)
        if not sequence :
            print(turn_data.map)
            problem = StateSpace(map)
            sequence = search(problem)
            if sequence == "failure" :
                return None
        return sequence.pop()

if __name__ == '__main__':
    winner = uninformedagent().play()
    print("WINNER: " + winner)


