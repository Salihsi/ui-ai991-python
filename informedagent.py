import random
from base import BaseAgent, TurnData, Action
from state_graph import StateSpace
from a_search import Search

class Agent(BaseAgent):

    def __init__(self):
        BaseAgent.__init__(self)
        self.sequence = []
        self.conclusion = []
        print(f"MY NAME: {self.name}")
        print(f"PLAYER COUNT: {self.agent_count}")
        print(f"GRID SIZE: {self.grid_size}")
        print(f"MAX TURNS: {self.max_turns}")
        print(f"DECISION TIME LIMIT: {self.decision_time_limit}")

    def do_turn(self, turn_data: TurnData) -> Action:
        print(f"TURN {self.max_turns - turn_data.turns_left}/{self.max_turns}")
        for agent in turn_data.agent_data:
            print(f"AGENT {agent.name}")
            print(f"POSITION: {agent.position}")
            print(f"CARRYING: {agent.carrying}")
            print(f"COLLECTED: {agent.collected}")
        for row in turn_data.map:
            print(''.join(row))

        if not self.conclusion:
            if agent.carrying == None:
                if not self.sequence :
                   problem = StateSpace(turn_data.map)
                   agentx, agenty = turn_data.agent_data[0].position
                   problem.initial_state = f'{agentx},{agenty}'
                   self.sequence = Search(problem).start_search()
                if self.sequence:
                    return self.sequence.pop()
            else:
                problem = StateSpace(turn_data.map , True)
                agentx, agenty = turn_data.agent_data[0].position
                problem.initial_state = f'{agentx},{agenty}'  
                self.conclusion = Search(problem).start_search()
        if self.conclusion:
            return self.conclusion.pop()
        
        # return random.choice(list(Action))

if __name__ == '__main__':
    winner = Agent().play()
    print("WINNER: " + winner)

