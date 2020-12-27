import random
from base import BaseAgent, TurnData, Action
from problem import Problem
from gemOrderSearch import Search
from state_graph import StateSpace
from aStarSearch import ASearch
class Agent(BaseAgent):
    
    def __init__(self):
        BaseAgent.__init__(self)
        self.gemSeq = []
        self.seq = []
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
        location = tuple()
        if not self.seq :
            mapProblem = StateSpace(turn_data.map , True)
            problem = Problem(turn_data.map , agent.position , mapProblem ,self.max_turns)
            gemSeq = eval(Search(problem).start_search())
            for gem in gemSeq:
                if not location:
                    location = turn_data.agent_data[0].position
                x , y , s = gem
                i , j = location
                mapProblem.initial_state = f'{i},{j}'
                problemGoal = mapProblem.goal
                mapProblem.goal = [f'{x},{y}']
                seq , node = ASearch(mapProblem).start_search()
                for a in seq[::-1]:
                    self.seq.append(a)
                mapProblem.goal = problemGoal
                mapProblem.initial_state = f'{x},{y}'
                seq , node = ASearch(mapProblem).start_search()
                location = eval(node.name)
                for a in seq[::-1]:
                    self.seq.append(a)

        if self.seq :
            return self.seq.pop(0)
                




if __name__ == '__main__':
    winner = Agent().play()
    print("WINNER: " + winner)
