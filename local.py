import random
from base import BaseAgent, TurnData, Action
from genetic import func
import matplotlib.pyplot as plt
import networkx as nx
class Agent(BaseAgent):

    def __init__(self):
        self.result = []
        BaseAgent.__init__(self)
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
        # for row in turn_data.map:
        #     print(''.join(row))
        # action_name = input("> ").upper()
        # if action_name == "U":
        #     return Action.UP
        # if action_name == "D":
        #     return Action.DOWN
        # if action_name == "L":
        #     return Action.LEFT
        # if action_name == "R":
        #     return Action.RIGHT
        # return random.choice(list(Action))
        if not self.result : 
            problem = func.problem(turn_data.map)
            initialPopulation = func.parsMap(turn_data.map , 50)
            progress = []
            
            progress.append(func.rankRoutes(initialPopulation, turn_data.turns_left , turn_data.agent_data[0].position , problem)[0][1])
            for i in range(0, 500):
                initialPopulation = func.nextGeneration(initialPopulation, 20, 0.05 , turn_data.turns_left , turn_data.agent_data[0].position , problem)
                generationScoreList = func.rankRoutes(initialPopulation, turn_data.turns_left , turn_data.agent_data[0].position , problem)
                generationScore = generationScoreList[0][1]
                progress.append(generationScore)

            routeIndex = func.rankRoutes(initialPopulation, turn_data.turns_left , turn_data.agent_data[0].position , problem)[0][0]
            route = initialPopulation[routeIndex]
            #print(route)
            self.result = self.get_seq(route , turn_data.agent_data[0].position , problem) 
            #print(rs)
            plt.plot(progress)
            plt.ylabel('Score')
            plt.xlabel('Generation')
            #plt.show()
            plt.savefig('test_image.png')

        return self.result.pop(0) 


    def get_seq(self , route , location , problem):
        xstart , ystart = location
        res = []
        seq = []
        for i in range(len(route)):
            xend , yend = 0,0
            if i % 2 ==0:
                xend , yend , s = route[i]
            else:
                xend , yend  = route[i]
            p = nx.shortest_path(problem , f'{xstart},{ystart}' , f'{xend},{yend}')
            for item in p :
                res.append(item)
            xstart = xend
            ystart = yend
        for node in range(len(res) - 1):
            x1 , y1 = eval(res[node])
            x2 , y2 = eval(res[node + 1])
            if x1 - x2 == 1 and y1 - y2 == 0:
                seq.append(Action.UP)
            if x1 - x2 == 0 and y1 - y2 == 1:
                seq.append(Action.LEFT)
            if x1 - x2 == -1 and y1 - y2 == 0:
                seq.append(Action.DOWN)
            if x1 - x2 == 0 and y1 - y2 == -1:
                seq.append(Action.RIGHT)
        return seq



            




if __name__ == '__main__':
    winner = Agent().play()
    print("WINNER: " + winner)
