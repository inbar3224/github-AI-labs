# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0
import itertools
import random
import time
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy

from Nqueens import *
from BinPacking import *

target = list("Hello, world!")

# get initial parameters
def getParameters(type):
    # population size
    print("what is the population size - please enter a number between 1 and 1000:")
    temp = input()
    try:
        populationSize = int(temp)
        if populationSize < 1 or populationSize > 1000:
            print("the value received is not within range. putting default value: 100")
            populationSize = 100
    except ValueError:
        print("the value received was not a number. putting default value: 100")
        populationSize = 100

    # number of generations
    print("what is the number of generations - please enter a number between 1 and 1000:")
    temp = input()
    try:
        numberOfGenerations = int(temp)
        if numberOfGenerations < 1 or numberOfGenerations > 1000:
            print("the value received is not within range. putting default value: 100")
            numberOfGenerations = 100
    except ValueError:
        print("the value received was not a number. putting default value: 100")
        numberOfGenerations = 100

    # only for strings
    if type == 1:
        # type of crossover
        print("enter 0 for no crossover, 1 for single point crossover, 2 for two points crossover, 3 for uniform crossover:")
        temp = input()
        try:
            crossoverType = int(temp)
            if crossoverType < 0 or crossoverType > 3:
                print("the value received is not within range. putting default value: 1")
                crossoverType = 1
        except ValueError:
            print("the value received was not a number. putting default value: 1")
            crossoverType = 1

        # mutation type
        print("enter 0 for no mutation, 1 for mutation:")
        temp = input()
        try:
            mutationType = int(temp)
            if mutationType < 0 or mutationType > 1:
                print("the value received is not within range. putting default value: 1")
                mutationType = 1
        except ValueError:
            print("the value received was not a number. putting default value: 1")
            mutationType = 1

        return populationSize, numberOfGenerations, crossoverType, mutationType

    # only for n queens
    elif type >= 2:
        if type == 3:
            # number of queens
            print("what is the number of queens - please enter a number between 1 and 10:")
            temp = input()
            try:
                numberOfQueens = int(temp)
                if numberOfQueens < 1 or numberOfQueens > 10:
                    print("the value received is not within range. putting default value: 5")
                    numberOfQueens = 5
            except ValueError:
                print("the value received was not a number. putting default value: 5")
                numberOfQueens = 5

        # type of parent selection
        print("enter 0 for RWS, 1 for SUS, 2 for tournament:")
        temp = input()
        try:
            parentS = int(temp)
            if parentS < 0 or parentS > 2:
                print("the value received is not within range. putting default value: 2")
                parentS = 2
        except ValueError:
            print("the value received was not a number. putting default value: 2")
            parentS = 2

        # type of parent selection
        print("enter 0 for PMX, 1 for CX:")
        temp = input()
        try:
            crossoverType = int(temp)
            if crossoverType < 0 or crossoverType > 1:
                print("the value received is not within range. putting default value: 0")
                crossoverType = 0
        except ValueError:
            print("the value received was not a number. putting default value: 0")
            crossoverType = 0

        # mutation type
        print("enter 0 for inversion, 1 for scramble:")
        temp = input()
        try:
            mutationType = int(temp)
            if mutationType < 0 or mutationType > 1:
                print("the value received is not within range. putting default value: 1")
                mutationType = 1
        except ValueError:
            print("the value received was not a number. putting default value: 1")
            mutationType = 1

        if type == 2:
            return populationSize, numberOfGenerations, parentS, crossoverType, mutationType
        elif type == 3:
            return populationSize, numberOfGenerations, numberOfQueens, parentS, crossoverType, mutationType

# initialize # generations with # population
def createGenePool(populationSize, numberOfGenerations, crossoverType, mutationType):
    population = []
    generation = []
    clockTicksTimes = []
    fitnessArray = []
    meanArray = []
    varianceArray = []
    stdArray = []
    bullsEyeArray = []
    length = len(target)

    # generation 0
    elapsedBegin = timer()
    clockTicksBegin1 = time.time()
    for i in range(populationSize):
        gene = [chr(random.randint(32, 126)) for j in range(length)]
        generation.append(gene)
    fitnessesI1 = [fitness(individual) for individual in generation]
    fitnessArray.append(fitnessesI1)
    mean1, variance1, std1 = meanVarianceStd(fitnessesI1)
    meanArray.append(mean1)
    varianceArray.append(variance1)
    stdArray.append(std1)
    bullsEyeI1 = [bullsEye(individual) for individual in generation]
    bullsEyeArray.append(bullsEyeI1)
    population.append(generation)
    clockTicksEnd1 = time.time()
    clockTicksTimes.append(clockTicksEnd1 - clockTicksBegin1)

    # create all the other generations
    for i in range(numberOfGenerations - 1):
        clockTicksBegin = time.time()

        # fitness heuristic
        fitnessesI = [fitness(individual) for individual in generation]
        fitnessArray.append(fitnessesI)

        # mean, variance, std
        mean, variance, std = meanVarianceStd(fitnessesI)
        meanArray.append(mean)
        varianceArray.append(variance)
        stdArray.append(std)

        # bulls eye heuristic
        bullsEyeI = [bullsEye(individual) for individual in generation]
        bullsEyeArray.append(bullsEyeI)

        # reproduction according to crossover type and mutation
        # no crossover
        if crossoverType == 0:
            eliteSize = int(populationSize * 1)
            eliteIndices = sorted(range(populationSize), key=lambda i: fitnessesI[i], reverse=True)[:eliteSize]
            elites = [generation[i] for i in eliteIndices]
            # yes to mutation
            if mutationType == 1:
                elites1 = [mutation(individual, length) for individual in elites]
                generation = elites1
                population.append(generation)
            else:
                generation = elites
                population.append(generation)
        # crossover
        else:
            # take only the 10%
            eliteSize = int(populationSize * 0.1)
            eliteIndices = sorted(range(populationSize), key=lambda i: fitnessesI[i], reverse=True)[:eliteSize]
            elites = [generation[i] for i in eliteIndices]
            # creates the 90% of new children - crossover and mutation operators
            offspring = []
            while len(offspring) < populationSize - eliteSize:
                parent1 = random.choice(generation)
                parent2 = random.choice(generation)
                child = crossover(crossoverType, parent1, parent2, length)
                offspring.append(child)
            generation = elites + offspring
            if mutationType == 1:
                generation1 = [mutation(individual, length) for individual in generation]
                generation = generation1
                population.append(generation)
            else:
                population.append(generation)

        # times
        clockTicksEnd = time.time()
        clockTicksTimes.append(clockTicksEnd - clockTicksBegin)

    elapsedEnd = timer()
    elapsedTime = elapsedEnd - elapsedBegin

    return population, clockTicksTimes, fitnessArray, meanArray, varianceArray, stdArray, bullsEyeArray, elapsedTime

# returns a fitness score for a single person
def fitness(individual):
    score = 0
    for i in range(len(individual)):
        if individual[i] == target[i]:
            score += 1
    return score

# return mean, variance and std of fitness
def meanVarianceStd(fitness):
    length = len(fitness)
    mean = sum(fitness) / length
    variance = sum(pow(i - mean, 2) for i in fitness) / length
    std = pow(variance, 0.5)
    return mean, variance, std

# gives a point if the word has the letter, and an extra point if the letter is in the right place
def bullsEye(individual):
    score = 0
    for i in range(len(individual)):
        if target[i] in individual:
             score += 1
        if individual[i] == target[i]:
            score += 1
    return score

# mutation
def mutation(individual, length):
    point = random.randint(0, length - 1)
    newC = chr(random.randint(32, 126))
    individual[point] = newC
    return individual

# crossover according to type: single point, two point, uniform
def crossover(type, p1, p2, numberOfG):
    if type == 1:
        # 1 point for separating parent 1 and 2
        point = random.randint(1, numberOfG - 1)
        child = p1[0: point] + p2[point:]
    elif type == 2:
        # 2 points separating: parent 1 until point1, then parent 2, than parent 1 again
        point1 = random.randint(1, numberOfG - 2)
        point2 = random.randint(point1 + 1, numberOfG - 1)
        child = p1[0: point1] + p2[point1: point2] + p1[point2:]
    elif type == 3:
        # at each point, we choose randomly between parent1 and parent2
        child = [p1[i] if random.random() < 0.5 else p2[i] for i in range(numberOfG)]

    return child

# print mean, std, clock ticks time, elapsed time
def printDetails(numberOfGenerations, mean, std, clockTicks, elapsed):
    for i in range(numberOfGenerations):
        print(f"generations {i}:")
        print(f"mean {mean[i]}")
        print(f"std {std[i]}")
        print(f"clock ticks {clockTicks[i]} seconds")
        print()
    print(f"elapsed time {elapsed} seconds")

# histogram function
def fitnessHis(numberOfGenerations, fitness):
    if numberOfGenerations == 1:
        indices = [0]
    elif numberOfGenerations == 2:
        indices = [0, 1]
    else:
        indices = [0, int(numberOfGenerations / 2), numberOfGenerations - 1]
    length = len(fitness[0])

    for j in range(len(indices)):
        x = [0] * length
        y = [0] * length

        for i in range(length):
            x[i] = i
        for i in range(length):
            y[i] = fitness[indices[j]][i]
        plt.scatter(x, y)
        for i in range(0, int(length / 10) + 1):
            plt.axvline(x = i * 10)

        plt.title(f'generation {indices[j]}')
        plt.xlabel('gene number (from 1 to population size)')
        plt.ylabel('score')
        plt.show()

# run for N queens
def runNQueens(populationSize, numberOfGenerations, numberOfQueens, parentS, crossoverType, mutationType):
    population = []
    generation = []
    fitnessArray = []
    meanArray = []
    stdArray = []
    varianceArray = []
    topAverage = []
    geneDistanceArray = []
    permutationsNumber = []
    clockTicksTimes = []

    arr = permutations(numberOfQueens)

    # generation 0
    elapsedBegin = timer()
    clockTicksBegin1 = time.time()
    j = 0
    for i in range(populationSize):
        if numberOfQueens == 1:
            gene = Nqueens(arr, 0, 0)
        else:
            gene = Nqueens(arr, j, j + 1)
        generation.append(gene)
        j += 2
        if j >= len(arr):
            j = 0
    fitnessesI1 = [individual.fitness() for individual in generation]
    fitnessArray.append(fitnessesI1)
    mean1, variance1, std1 = meanVarianceStd(fitnessesI1)
    meanArray.append(mean1)
    varianceArray.append(variance1)
    stdArray.append(std1)
    topA1 = topAverageF(fitnessesI1, mean1)
    topAverage.append(topA1)
    geneD1 = geneDistance(generation)
    geneDistanceArray.append(geneD1)
    per1 = countD(generation)
    permutationsNumber.append(per1)
    population.append(generation)
    clockTicksEnd1 = time.time()
    clockTicksTimes.append(clockTicksEnd1 - clockTicksBegin1)

    # create all the other generations
    for i in range(numberOfGenerations - 1):
        # update age of genes from previews generations
        for generationX in population:
            for individual in generationX:
                individual.updateAge()

        # begin timer
        clockTicksBegin = time.time()

        # fitness heuristic
        fitnessesI = [individual.fitness() for individual in generation]
        fitnessArray.append(fitnessesI)

        # mean, variance, std
        mean, variance, std = meanVarianceStd(fitnessesI)
        meanArray.append(mean)
        varianceArray.append(variance)
        stdArray.append(std)

        # top average ration
        topA = topAverageF(fitnessesI, mean)
        topAverage.append(topA)

        # gene distance and number of permutations
        geneD = geneDistance(generation)
        geneDistanceArray.append(geneD)
        per = countD(generation)
        permutationsNumber.append(per)

        # reproduction according to parenting selection, crossover type and mutation
        # take only the 10% that fit the aging criteria
        elites = elitismAndAging(populationSize, fitnessesI, generation, numberOfGenerations)
        eliteSize = len(elites)

        # scaling and creation of roulette
        if parentS == 0 or parentS == 1:
            # scaling
            newFitness = scalingFitness(fitnessesI, mean)
            # create roulette for RWS, SUS
            values, roulette = createRoulette(newFitness)
        # getting k competitors in tournament
        elif parentS == 2:
            if len(elites) != 0:
                kPool = elites
            else:
                kPool = generation

        # creates the 90% of new children, crossover and mutation operators
        offspring = []
        while len(offspring) < populationSize - eliteSize:
            # parent selection
            if parentS == 0:
                parent1 = RWS(roulette, newFitness, generation)
                parent2 = RWS(roulette, newFitness, generation)
            elif parentS == 1:
                parent1, parent2 = SUS(roulette, newFitness, generation)
            elif parentS == 2:
                parent1 = random.choice(kPool)
                parent2 = random.choice(kPool)
            # crossover
            if crossoverType == 0:
                child = PMX(parent1, parent2, arr)
            elif crossoverType == 1:
                child = CX(parent1, parent2, arr)
            # mutation
            if mutationType == 0:
                child.inversion()
            elif mutationType == 1:
                child.scramble()
            #child.printD()
            offspring.append(child)
        generation = elites + offspring
        population.append(generation)

        # times
        clockTicksEnd = time.time()
        clockTicksTimes.append(clockTicksEnd - clockTicksBegin)

    elapsedEnd = timer()
    elapsedTime = elapsedEnd - elapsedBegin

    return meanArray, stdArray, varianceArray, topAverage, geneDistanceArray, permutationsNumber, clockTicksTimes, elapsedTime

# create permutations of rows and columns for n queens
def permutations(number):
    numberOfQueens = []
    for i in range(0, number):
        temp = i + 1
        numberOfQueens.append(temp)

    resultPerms = [[]]
    for n in numberOfQueens:
        newPerms = []
        for perm in resultPerms:
            for i in range(len(perm) + 1):
                newPerms.append(perm[:i] + [n] + perm[i:])
                resultPerms = newPerms
    return resultPerms

# elitism (choosing elite team) while fitting the aging criteria
def elitismAndAging(populationSize, fitnessesI, generation, numberOfGenerations):
    newFitness = [0.5 * fitnessesI[i] + 0.5 * (1 - (generation[i].age / numberOfGenerations)) for i in range(len(fitnessesI))]
    eliteSize = int(populationSize * 0.1)
    eliteIndices = sorted(range(populationSize), key=lambda i: newFitness[i], reverse=True)[:eliteSize]
    elites = [generation[i] for i in eliteIndices]
    return elites

# scaling existing fitness
def scalingFitness(fitnessI, mean):
    lower = numpy.percentile(fitnessI, 5)
    upper = numpy.percentile(fitnessI, 95)
    for i in range(len(fitnessI)):
        if fitnessI[i] < lower:
            fitnessI[i] = lower
        if fitnessI[i] > upper:
            fitnessI[i] = upper

    newFitness = [fitnessI[i] - mean for i in range(len(fitnessI))]
    return newFitness

# create roulette for RWS, SUS parent selecting
def createRoulette(fitnessI):
    fitnessI.sort()
    roulette = []
    cell = fitnessI[0]
    counter = 1
    length = len(fitnessI)
    values = []

    for i in range(1, length):
        if int(fitnessI[i]) == int(cell):
            counter += 1
        else:
            values.append(cell)
            roulette.append(counter / length)
            cell = fitnessI[i]
            counter = 1
    values.append(cell)
    roulette.append(counter / length)

    return roulette, values

# RWS parent selection
def RWS(roulette, newFitness, generation):
    probability = random.choice(roulette)
    item = newFitness.index(probability)
    return generation[item]

# SUS parent selection
def SUS(roulette, newFitness, generation):
    r1 = roulette
    probability1 = random.choice(r1)
    if len(r1) != 1:
        r1.remove(probability1)
    probability2 = random.choice(r1)

    item1 = newFitness.index(probability1)
    item2 = newFitness.index(probability2)

    return generation[item1], generation[item2]

# PMX crossover operator
def PMX(parent1, parent2, permutation):
    child = Nqueens(permutation, 0, 0)
    child.rows = parent1.rows
    child.cols = parent2.cols

    if len(parent1.rows) == 1:
        return child
    else:
        i1 = random.choice(child.rows)
        i2 = random.choice(child.rows)
        index1 = child.rows.index(i1)
        index2 = child.rows.index(i2)
        a = child.rows[index1]
        child.rows[index1] = child.rows[index2]
        child.rows[index2] = a
        index1 = child.cols.index(i1)
        index2 = child.cols.index(i2)
        a = child.cols[index1]
        child.cols[index1] = child.cols[index2]
        child.cols[index2] = a

        return child

# CX crossover operator
def CX(parent1, parent2, permutation):
    child = Nqueens(permutation, 0, 0)
    if len(parent1.rows) == 1:
        return child
    else:
        temp = random.choice(permutation[0])
        if temp % 2 == 0:
            child.rows = parent1.rows
            child.cols = parent2.cols
        else:
            child.rows = parent2.rows
            child.cols = parent1.cols

        return child

# top average ratio
def topAverageF(fitnessI, mean):
    counter = 0
    for i in fitnessI:
        if i > mean:
            counter += 1

    return counter / len(fitnessI)

# gene distance - measure the number of changes required to get from one permutation to another
def geneDistance(generation):
    length = len(generation)
    counter = 0

    for i in range(length):
        for j in range(i + 1, length):
            counter += differences(generation[i].rows, generation[j].rows)
            counter += differences(generation[i].cols, generation[j].cols)

    return counter

def differences(a, b):
    return sum(i != j for i, j in zip(a, b))

# number of different permutations in each generation
def countD(generation):
    list = []
    counter = 0

    for i in range(len(generation)):
        if generation[i].rows in list:
            continue
        else:
            list.append(generation[i].rows)
            counter += 1
        if generation[i].cols in list:
            continue
        else:
            list.append(generation[i].cols)
            counter += 1

    return counter

def printForQueen(numberOfGenerations, mean, std, variance, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime):
    for i in range(numberOfGenerations):
        print(f"generations {i}:")
        print(f"mean {mean[i]}")
        print(f"std {std[i]}")
        print(f"selection pressure - variance {variance[i]}")
        print(f"selection pressure - top average ratio {topAverage[i]}")
        print(f"genetic diversity - distance between genes {geneDistance[i]}")
        print(f"genetic diversity - number of permutations {permutationsNumber[i]}")
        print(f"clock ticks {clockTicksTimes[i]} seconds")
        print()
    print(f"elapsed time {elapsedTime} seconds")

# rearrange the order of insertion
def options(permutations):
    return list(itertools.permutations(permutations))

def adding(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    counter = 0
    list = []
    x = 0

    while counter < 1000:
        per = a[x] + b[x] + c[x] + d[x] + e[x] + f[x] + g[x] + h[x] + i[x] + j[x] + k[x] + l[x] + m[x] + n[x] + o[x]
        list.append(per)
        x += 1
        counter += 1

    return list

# run for Binpacking
def runBinPacking(populationSize, numberOfGenerations, perN, parentS, crossoverType, mutationType):
    population = []
    generation = []
    fitnessArray = []
    firstFitArray = []
    meanArray = []
    stdArray = []
    varianceArray = []
    firstFitMeanArray = []
    topAverage = []
    geneDistanceArray = []
    permutationsNumber = []
    clockTicksTimes = []

    # generation 0
    elapsedBegin = timer()
    clockTicksBegin1 = time.time()
    j = 0
    for i in range(populationSize):
        gene = BinPacking(perN, j)
        generation.append(gene)
        j += 1
        if j >= len(perN):
            j = 0
    fitnessesI1 = [individual.fitness() for individual in generation]
    fitnessArray.append(fitnessesI1)
    firstFitI1 = [individual.firstFit() for individual in generation]
    firstFitArray.append(firstFitI1)

    mean1, variance1, std1 = meanVarianceStd(fitnessesI1)
    meanArray.append(mean1)
    varianceArray.append(variance1)
    stdArray.append(std1)
    mean2, variance1, std1 = meanVarianceStd(firstFitI1)
    firstFitMeanArray.append(mean2)

    topA1 = topAverageF(fitnessesI1, mean1)
    topAverage.append(topA1)

    geneD1 = geneDistanceD(generation)
    geneDistanceArray.append(geneD1)
    per1 = countDL(generation)
    permutationsNumber.append(per1)

    population.append(generation)
    clockTicksEnd1 = time.time()
    clockTicksTimes.append(clockTicksEnd1 - clockTicksBegin1)

    # create all the other generations
    for i in range(numberOfGenerations - 1):
        # update age of genes from previews generations
        for generationX in population:
            for individual in generationX:
                individual.updateAge()

        # begin timer
        clockTicksBegin = time.time()

        # fitness heuristic
        fitnessesI = [individual.fitness() for individual in generation]
        fitnessArray.append(fitnessesI)
        firstFitI = [individual.firstFit() for individual in generation]
        firstFitArray.append(firstFitI)

        # mean, variance, std
        mean, variance, std = meanVarianceStd(fitnessesI)
        meanArray.append(mean)
        varianceArray.append(variance)
        stdArray.append(std)
        mean3, variance1, std1 = meanVarianceStd(firstFitI)
        firstFitMeanArray.append(mean3)

        # top average ration
        topA = topAverageF(fitnessesI, mean)
        topAverage.append(topA)

        # gene distance and number of permutations
        geneD = geneDistanceD(generation)
        geneDistanceArray.append(geneD)
        per = countDL(generation)
        permutationsNumber.append(per)

        # reproduction according to parenting selection, crossover type and mutation
        # take only the 10% that fit the aging criteria
        elites = elitismAndAging(populationSize, fitnessesI, generation, numberOfGenerations)
        eliteSize = len(elites)

        # scaling and creation of roulette
        if parentS == 0 or parentS == 1:
            # scaling
            newFitness = scalingFitness(fitnessesI, mean)
            # create roulette for RWS, SUS
            values, roulette = createRoulette(newFitness)
        # getting k competitors in tournament
        elif parentS == 2:
            if len(elites) != 0:
                kPool = elites
            else:
                kPool = generation

        # creates the 90% of new children, crossover and mutation operators
        offspring = []
        while len(offspring) < populationSize - eliteSize:
            # parent selection
            if parentS == 0:
                parent1 = RWS(roulette, newFitness, generation)
                parent2 = RWS(roulette, newFitness, generation)
            elif parentS == 1:
                parent1, parent2 = SUS(roulette, newFitness, generation)
            elif parentS == 2:
                parent1 = random.choice(kPool)
                parent2 = random.choice(kPool)
            # crossover
            if crossoverType == 0:
                child = PMXD(parent1, parent2)
            elif crossoverType == 1:
                child = CXD(parent1, parent2)
            # mutation
            if mutationType == 0:
                child.inversion()
            elif mutationType == 1:
                child.scramble()
            #child.printD()
            offspring.append(child)
        generation = elites + offspring
        population.append(generation)

        # times
        clockTicksEnd = time.time()
        clockTicksTimes.append(clockTicksEnd - clockTicksBegin)

    elapsedEnd = timer()
    elapsedTime = elapsedEnd - elapsedBegin

    return meanArray, stdArray, varianceArray, firstFitMeanArray, topAverage, geneDistanceArray, permutationsNumber, clockTicksTimes, elapsedTime

def geneDistanceD(generation):
    length = len(generation)
    counter = 0
    for i in range(length):
        for j in range(i + 1, length):
            counter += differences(generation[i].orderOfInsertion, generation[j].orderOfInsertion)
    return counter

def countDL(generation):
    list = []
    counter = 0
    for i in range(len(generation)):
        if generation[i].orderOfInsertion in list:
            continue
        else:
            list.append(generation[i].orderOfInsertion)
            counter += 1
    return counter

def PMXD(parent1, parent2):
    if parent1.fitness() >= parent2.fitness():
        child = BinPacking([parent1.orderOfInsertion], 0)
    else:
        child = BinPacking([parent2.orderOfInsertion], 0)

    i1 = random.choice(child.orderOfInsertion)
    i2 = random.choice(child.orderOfInsertion)
    index1 = child.orderOfInsertion.index(i1)
    index2 = child.orderOfInsertion.index(i2)

    a = child.orderOfInsertion[index1]
    child.orderOfInsertion[index1] = child.orderOfInsertion[index2]
    child.orderOfInsertion[index2] = a

    return child

def CXD(parent1, parent2):
    temp = random.choice([0, 1])
    if temp % 2 == 0:
        child = BinPacking([parent1.orderOfInsertion], 0)
    else:
        child = BinPacking([parent2.orderOfInsertion], 0)
    return child

def printForBin(numberOfGenerations, mean, std, variance, firstFit, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime):
    for i in range(numberOfGenerations):
        print(f"generations {i}:")
        print(f"mean {mean[i]}")
        print(f"std {std[i]}")
        print(f"first fit {firstFit[i]}")
        print(f"selection pressure - variance {variance[i]}")
        print(f"selection pressure - top average ratio {topAverage[i]}")
        print(f"genetic diversity - distance between genes {geneDistance[i]}")
        print(f"genetic diversity - number of permutations {permutationsNumber[i]}")
        print(f"clock ticks {clockTicksTimes[i]} seconds")
        print()
    print(f"elapsed time {elapsedTime} seconds")
