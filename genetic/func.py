import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt , networkx as nx

class Fitness:
    def __init__(self, route , turns_left , position , problem):
        self.problem = problem
        self.route = route
        self.turns_left = turns_left
        self.position = position
        self.currentScore = 0
        self.score = 0
        self.fitness= 0.0
    
    def routeScore(self):
        if self.score ==0:
            i = 0
            while self.turns_left >= 0 and  self.route:
                nextPosition = self.route[i]
                if i % 2 == 0 :
                    x , y , s  = nextPosition
                    self.currentScore = s
                    positionx , positiony = self.position
                    self.position = (x,y)
                    lenght = nx.shortest_path_length(self.problem, f'{positionx},{positiony}' , f'{x},{y}')
                    self.turns_left -= lenght
                    i += 1
                else:
                    self.score += self.currentScore
                    x , y = nextPosition
                    positionx , positiony = self.position 
                    self.position = nextPosition
                    lenght = nx.shortest_path_length(self.problem, f'{positionx},{positiony}' , f'{x},{y}')
                    self.turns_left -= lenght
                    i += 1
        return self.score
        
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = float(self.routeScore())
        return self.fitness

def parsMap(map , pop):
    gemList =[]
    baseList =[]
    initialPopulation = []
    route = []
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j].isdigit():
                gemList.append((i , j , getScore(int(map[i][j]))))
            if map[i][j] == 'a':
                baseList.append((i , j))

    for i in range(pop):
        gemSample = random.sample(gemList , len(gemList))
        for j in range(len(gemList)):
            route.append(gemSample[j])
            route.append(random.sample(baseList , 1)[0])
        initialPopulation.append(route)
        route = []

    return initialPopulation

def getScore(gemPoint):
    if gemPoint == 0:
        return 2
    elif gemPoint == 1:
        return 5
    elif gemPoint == 2:
        return 3
    elif gemPoint == 3:
        return 1
    else:
        return 10

def problem(map):
    graph = nx.Graph()
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] != '*' :
                if j+1 < len(map) and map[i][j+1] != '*':
                    graph.add_edge(f'{i},{j}', f'{i},{j+1}')
                if i+1 < len(map) and map[i+1][j] != '*':
                    graph.add_edge(f'{i},{j}', f'{i+1},{j}')
    return graph

def rankRoutes(population , turns_left , position , problem):
    fitnessResults = {}
    for i in range(0,len(population)):
        fitnessResults[i] = Fitness(population[i] , turns_left , position , problem).routeFitness()
        sortedList = sorted(fitnessResults.items(), key = operator.itemgetter(1) ,reverse=True)
    return sortedList

def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,eliteSize):
        children.append(matingpool[i])
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []
    
    #geneA = int(random.random() * len(parent1))
    #geneB = int(random.random() * len(parent1))
    geneA = random.randrange(0 , len(parent1) - 1 , 2)
    geneB = random.randrange(0 , len(parent1) - 1 , 2)
    
    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    gemP1 = []
    gemP2 = []
    baseP2 = []

    p2L = parent2[:startGene]
    p2H = parent2[endGene:]
    newP2 = p2H + p2L

    for i in range(len(newP2)):
        if i%2 != 0 :
            baseP2.append(newP2[i])

    for i in range(startGene, endGene):
        childP1.append(parent1[i])
        if i%2 == 0 :
            gemP1.append(parent1[i])

    for i in range(len(parent2)):
        if i%2 == 0 and parent2[i] not in gemP1:
            gemP2.append(parent2[i])

    for i in range(len(gemP2)):
        childP2.append(gemP2[i])
        childP2.append(baseP2[i])

    child = childP1 + childP2
    return child

def mutatePopulation(population, mutationRate):
    mutatedPop = []
    
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            if swapped % 2 == 0 :
                swapWith = int(random.randrange(0 , len(individual) - 1 , 2))
            else:
                swapWith = int(random.randrange(1 , len(individual) - 1 , 2))
            
            
            city1 = individual[swapped]
            city2 = individual[swapWith]
            
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

def nextGeneration(currentGen, eliteSize, mutationRate , turns_left , position , problem):
    popRanked = rankRoutes(currentGen , turns_left , position , problem)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration