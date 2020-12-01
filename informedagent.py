import random
from base import BaseAgent, TurnData, Action
from state_graph import StateSpace
from a_search import Search
import time
class Agent(BaseAgent):

    def __init__(self):
        BaseAgent.__init__(self)
        self.sequence = []
        self.conclusion = []

    def do_turn(self, turn_data: TurnData) -> Action:
        now = time.time()
        agent = turn_data.agent_data[0]
        if not self.conclusion:
            if agent.carrying == None:
                if not self.sequence :
                   problem = StateSpace(turn_data.map)
                   agentx, agenty = turn_data.agent_data[0].position
                   problem.initial_state = f'{agentx},{agenty}'
                   print("problem , agent to gem" ,  time.time() - now)
                   seqTime = time.time()
                   self.sequence = Search(problem).start_search()
                   print("agent  to gem : " , time.time() - now)
                   print("just seq : " , time.time() - seqTime)
                if self.sequence:
                    return self.sequence.pop()
            else:
                problem = StateSpace(turn_data.map , True)
                agentx, agenty = turn_data.agent_data[0].position
                problem.initial_state = f'{agentx},{agenty}'
                print("problem , gem to base" ,  time.time() - now)  
                seqTime = time.time()
                self.conclusion = Search(problem).start_search()
                print("gem to base" ,  time.time() - now)
                print("just seq : " , time.time() - seqTime)
        if self.conclusion:
            return self.conclusion.pop()
        
        # return random.choice(list(Action))

if __name__ == '__main__':
    now = time.time()
    winner = Agent().play()
    print("WINNER: " + winner)
    print(time.time() - now)

