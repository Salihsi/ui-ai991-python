import numpy as np , random , copy

class Game():
    wall_score = -0.5
    outOfRange_score = -0.8
    base_score = +0.2
    step_score = -0.1

    carrying = False

    def __init__(self ,map , position):
        self.map = map
        self.x , self.y = position

    def play(self ,action):
        newx , newy  = 0,0
        if action == 0:
            newx = self.x - 1
            newy = self.y
        elif action == 1:
            newx = self.x + 1
            newy = self.y
        elif action == 2:
            newx = self.x 
            newy = self.y - 1
        else:
            newx = self.x 
            newy = self.y + 1

        if self.carrying :
            if (newx < 0) or (newx >= len(self.map)) or (newy < 0) or (newy >= len(self.map)):
                return ((len(self.map) * self.x) + self.y , self.outOfRange_score , False , 0)
            elif self.map[newx][newy] == '*':
                return ((len(self.map) * self.x) + self.y , self.wall_score , False , 0)
            elif self.map[newx][newy] == 'a':
                self.carrying = False
                self.x = newx
                self.y = newy
                return ((len(self.map) * self.x) + self.y , self.base_score , self.goal() , 0)
            else:
                self.x = newx
                self.y = newy
                return ((len(self.map) * self.x) + self.y , self.step_score , False , 0) 
            
        else :
            if (newx < 0) or (newx >= len(self.map)) or (newy < 0) or (newy >= len(self.map)):
                return ((len(self.map) * self.x) + self.y , self.outOfRange_score , False , 0)
            elif self.map[newx][newy] == '*':
                return ((len(self.map) * self.x) + self.y , self.wall_score , False , 0)
            elif self.map[newx][newy].isdigit():
                n = int(self.map[newx][newy])
                self.map[newx][newy] = '.'
                self.carrying = True
                self.x = newx
                self.y = newy
                return ((len(self.map) * self.x) + self.y , self.getScore(n) , False , self.getScore(n))
            else:
                self.x = newx
                self.y = newy
                return ((len(self.map) * self.x) + self.y , self.step_score , False , 0) 

    def goal(self):
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if self.map[i][j].isdigit():
                    return False
        return True

    def getScore(self , ind):
        if ind == 0:
            return 2
        elif ind == 1:
            return 5
        elif ind == 2:
            return 3
        elif ind == 3:
            return 1
        else :
            return 10

class Qtable():
    total_episodes = 1000      # Total episodes
    learning_rate = 0.8           # Learning rate
    gamma = 0.95                  # Discounting rate
    epsilon = 1.0                 # Exploration rate
    max_epsilon = 1.0             # Exploration probability at start
    min_epsilon = 0.01            # Minimum exploration probability 
    decay_rate = 0.01             # Exponential decay rate for exploration prob

    rewards = []
    gem_rewards = []

    def __init__(self , map, max_turns , position):
        self.max_steps = max_turns
        self.map = map
        self.position = position 
        state_size = len(map) * len(map)
        action_size = 4
        self.qtable = np.zeros((state_size, action_size))

    def train(self):
        for episode in range(self.total_episodes):
            x , y = self.position
            state = (len(self.map) * x) + y
            step = 0
            done = False
            total_rewards = 0
            game = Game(copy.deepcopy(self.map) , self.position)
            total_gem_score = 0
            for step in range(self.max_steps):

                exp_exp_tradeoff = random.uniform(0, 1)
        
                if exp_exp_tradeoff > self.epsilon:
                    action = np.argmax(self.qtable[state,:])

                else:
                    action = random.randint(0 , 3)

                new_state, reward, done  , gem = game.play(action)


                self.qtable[state, action] = self.qtable[state, action] + self.learning_rate * (reward + self.gamma * np.max(self.qtable[new_state, :]) - self.qtable[state, action])
        
                total_rewards += reward

                total_gem_score += gem
        
                state = new_state
        
                if done == True: 
                    break
        
            #episode += 1
            self.gem_rewards.append(total_gem_score)
            self.epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon)*np.exp(-self.decay_rate*episode) 
            self.rewards.append(total_rewards)
