# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


import itertools
import time
from timeit import default_timer as timer

import numpy

from Word import *
from Nqueens import *
from BinPacking import *
from Results import *


counterQ = 0
evolution = 0
per75 = 0.75
per25 = 0.25
notImproved = 5


# 1 = string, 2 = queens, 3 = bin packing
def geneticA(popSize, numOfGen, mutationR, mutationP, PTYPE, parentS, crossoverType, mutationT, numOfQueens):
    # lists
    clockTicksTimesP = []
    population = []; generation = []
    fitnessP = []
    binaryFitnessP = []
    firstFitP = []
    meanP = []; varianceP = []; stdP = []
    topAverageRP = []
    hammingP = []; editP = []; kendallTP = []; ffDP = []
    uniqueP = []
    newFitness = None; values = None; roulette = None; kPool = None

    # times
    elapsedBegin = timer()
    clockTicksBegin = time.time()

    # initialize generation 0
    if PTYPE != 2:
        for i in range(popSize):
            gene = createGene(PTYPE)
            generation.append(gene)
    else:
        options = permutations(numOfQueens)
        for i in range(popSize):
            gene = createQueen(options)
            generation.append(gene)
    population.append(generation)

    # fitness, bull's eye and binary bull's eye for strings, first fit for bin packing
    fitnessG = [gene.fitness() for gene in generation]
    fitnessP.append(fitnessG)
    if PTYPE == 1:
        binaryFitnessG = [gene.fitnessBinary() for gene in generation]
        binaryFitnessP.append(binaryFitnessG)
    if PTYPE >= 3:
        firstFitG = [gene.firstFit() for gene in generation]
        firstFitP.append(firstFitG)

    # mean, variance, std
    meanG, varianceG, stdG = meanVarianceStd(fitnessG)
    meanP.append(meanG)
    varianceP.append(varianceG)
    stdP.append(stdG)

    # variance (already calculated), top average
    topAverageRG = topAverage(fitnessG, meanG)
    topAverageRP.append(topAverageRG)

    # gene distance
    if PTYPE == 1:
        hammingG = stringDistance(generation, 1)
        hammingP.append(hammingG)
        editG = stringDistance(generation, 2)
        editP.append(editG)
    elif PTYPE == 2:
        kendallTG = queensDistance(generation)
        kendallTP.append(kendallTG)
    elif PTYPE >= 3:
        ffDG = binDistance(generation)
        ffDP.append(ffDG)

    # unique alleles
    uniqueG = unique(generation, PTYPE)
    uniqueP.append(uniqueG)

    # times
    clockTicksEnd = time.time()
    clockTicksTimesP.append(clockTicksEnd - clockTicksBegin)

    # create all the other generations
    for i in range(numOfGen - 1):
        clockTicksBegin = time.time()

        # update age of genes from previews generations
        for j in generation:
            j.updateAge()

        # take only the 10% that fit the aging criteria
        elites = elitismAndAging(popSize, fitnessG, generation, numOfGen, 0.1)
        eliteSize = len(elites)

        # scaling and creation of roulette / getting k competitors in tournament
        newFitness = scalingFitness(fitnessG, meanG)
        values, roulette = createRoulette(newFitness)
        kPool = elitismAndAging(popSize, fitnessG, generation, numOfGen, 0.5)

        # update parameters for mutation
        global evolution
        evolution = 1 - (i / numOfGen)

        # parent selection, crossover and mutation operators
        offspring = []
        while len(offspring) < popSize - eliteSize:
            parent1, parent2 = psFunction(parentS, roulette, newFitness, generation, kPool)
            child = crossoverF(crossoverType, PTYPE, parent1, parent2)
            mutationF(mutationR, mutationP, mutationT, child, meanG, max(fitnessG))
            offspring.append(child)
        generation = elites + offspring
        population.append(generation)

        # fitness, bull's eye and binary bull's eye for strings, first fit for bin packing
        fitnessG = [gene.fitness() for gene in generation]
        fitnessP.append(fitnessG)
        if PTYPE == 1:
            binaryFitnessG = [gene.fitnessBinary() for gene in generation]
            binaryFitnessP.append(binaryFitnessG)
        if PTYPE >= 3:
            firstFitG = [gene.firstFit() for gene in generation]
            firstFitP.append(firstFitG)

        # mean, variance, std
        meanG, varianceG, stdG = meanVarianceStd(fitnessG)
        meanP.append(meanG)
        varianceP.append(varianceG)
        stdP.append(stdG)

        # variance (already calculated), top average
        topAverageRG = topAverage(fitnessG, meanG)
        topAverageRP.append(topAverageRG)

        # gene distance
        if PTYPE == 1:
            hammingG = stringDistance(generation, 1)
            hammingP.append(hammingG)
            editG = stringDistance(generation, 2)
            editP.append(editG)
        elif PTYPE == 2:
            kendallTG = queensDistance(generation)
            kendallTP.append(kendallTG)
        elif PTYPE >= 3:
            ffDG = binDistance(generation)
            ffDP.append(ffDG)

        # unique alleles
        uniqueG = unique(generation, PTYPE)
        uniqueP.append(uniqueG)

        clockTicksEnd = time.time()
        clockTicksTimesP.append(clockTicksEnd - clockTicksBegin)

    # elapsed time
    elapsedEnd = timer()
    elapsedTime = elapsedEnd - elapsedBegin

    if PTYPE == 1:
        return WordR(clockTicksTimesP, elapsedTime, fitnessP, binaryFitnessP, meanP, stdP, varianceP,
                     topAverageRP, hammingP, editP, uniqueP)
    elif PTYPE == 2:
        return QueensR(clockTicksTimesP, elapsedTime, fitnessP, meanP, stdP, varianceP, topAverageRP, kendallTP, uniqueP)
    elif PTYPE >= 3:
        return BinR(clockTicksTimesP, elapsedTime, fitnessP, firstFitP, meanP, stdP, varianceP, topAverageRP, ffDP, uniqueP)


# create gene
def createGene(PTYPE):
    gene = None

    if PTYPE == 1:
        gene = Word(args=1)
    elif PTYPE == 3:
        gene = BinPi(index=0)
    elif PTYPE == 4:
        gene = BinPi(index=1)
    elif PTYPE == 5:
        gene = BinPi(index=2)
    elif PTYPE == 6:
        gene = BinPi(index=3)
    elif PTYPE == 7:
        gene = BinPi(index=4)

    return gene


# permutations
def permutations(numOfQueens):
    original = [i + 1 for i in range(numOfQueens)]
    return list(itertools.permutations(original))


# create queen
def createQueen(permutations):
    gene = None
    global counterQ

    if len(permutations) == 1:
        gene = Nqueens(permutations, 0, 0)
    else:
        gene = Nqueens(permutations, counterQ, counterQ + 1)
        counterQ += 2
        if counterQ >= len(permutations):
            counterQ = 0

    return gene


# return mean, variance and std of fitness
def meanVarianceStd(fitness):
    length = len(fitness)

    mean = sum(fitness) / length
    variance = sum(pow(i - mean, 2) for i in fitness) / length
    std = pow(variance, 0.5)

    return mean, variance, std


# top average ratio
def topAverage(fitness, mean):
    counter = 0

    for i in fitness:
        if i > mean:
            counter += 1

    return counter / len(fitness)


# gene distance - string
def stringDistance(generation, num):
    length = len(generation)
    counter = 0

    for i in range(length):
        for j in range(i + 1, length):
            if num == 1:
                counter += generation[i].hammingD(generation[j])
            elif num == 2:
                counter += generation[i].editD(generation[j])

    return round(counter / pow(length, 2))


# gene distance - queens
def queensDistance(generation):
    length = len(generation)
    counter = 0

    for i in range(length):
        for j in range(i + 1, length):
            counter += generation[i].kendallT(generation[i].rows, generation[j].rows)
            counter += generation[i].kendallT(generation[i].cols, generation[j].cols)

    return round(counter / (2 * pow(length, 2)))


# gene distance - bin packing
def binDistance(generation):
    n = [gene.maxFF for gene in generation]
    return sum(n) / len(generation)


# unique alleles / permutations number
def unique(generation, PTYPE):
    options = []
    chars = []
    counter = 0
    length = len(generation)

    for i in range(length):
        if PTYPE == 1:
            for j in range(generation[i].lengthT):
                if generation[i].gene[j] in chars:
                    pass
                else:
                    chars.append(generation[i].gene[j])
                    counter += 1
        elif PTYPE == 2:
            if generation[i].rows in options:
                pass
            else:
                options.append(generation[i].rows)
                counter += 1
            if generation[i].cols in options:
                pass
            else:
                options.append(generation[i].cols)
                counter += 1
        elif PTYPE >= 3:
            if generation[i].gene in options:
                pass
            else:
                options.append(generation[i].gene)
                counter += 1

    if PTYPE != 2:
        return counter
    else:
        return counter / 2


# elitism (choosing elite team) while fitting the aging criteria
def elitismAndAging(popSize, fitness, generation, numOfGen, per):
    newFitness = [0.5 * fitness[i] + 0.5 * (1 - (generation[i].age / numOfGen)) for i in range(popSize)]
    eliteSize = int(popSize * per)
    eliteIndices = sorted(range(popSize), key=lambda i: newFitness[i], reverse=True)[:eliteSize]
    elites = [generation[i] for i in eliteIndices]
    return elites


# scaling existing fitness
def scalingFitness(fitness, mean):
    temp = fitness.copy()
    length = len(temp)

    lower = numpy.percentile(temp, 5)
    upper = numpy.percentile(temp, 95)

    for i in range(length):
        if temp[i] < lower:
            temp[i] = lower
        if temp[i] > upper:
            temp[i] = upper

    newFitness = [temp[i] - mean for i in range(length)]
    return newFitness


# create roulette for RWS, SUS parent selecting
def createRoulette(Fitness):
    newFitness = Fitness.copy()
    newFitness.sort()
    roulette = []; values = []
    cell = newFitness[0]
    counter = 1
    length = len(newFitness)

    for i in range(1, length):
        if newFitness[i] == cell:
            counter += 1
        else:
            values.append(cell)
            roulette.append(counter / length)
            cell = newFitness[i]
            counter = 1

    values.append(cell)
    roulette.append(counter / length)

    return roulette, values


# go to parent selection function
def psFunction(parentS, roulette, newFitness, generation, kPool):
    if parentS == 0:
        parent1 = RWS(roulette, newFitness, generation)
        parent2 = RWS(roulette, newFitness, generation)
        return parent1, parent2
    elif parentS == 1:
        return SUS(roulette, newFitness, generation)
    elif parentS == 2:
        parent1 = random.choice(kPool)
        parent2 = random.choice(kPool)
        return parent1, parent2


# RWS parent selection
def RWS(roulette, newFitness, generation):
    probability = random.choice(roulette)
    item = newFitness.index(probability)
    return generation[item]


# SUS parent selection
def SUS(roulette, newFitness, generation):
    r1 = roulette.copy()

    probability1 = random.choice(r1)
    if len(r1) != 1:
        r1.remove(probability1)
    probability2 = random.choice(r1)
    item1 = newFitness.index(probability1)
    item2 = newFitness.index(probability2)

    return generation[item1], generation[item2]


# go to crossover function
def crossoverF(crossoverType, PTYPE, parent1, parent2):
    child = None

    if PTYPE == 1:
        child = parent1.crossover(crossoverType, parent2)
    elif PTYPE >= 2:
        if parent1.fitness() > parent2.fitness():
            child = parent1.choose(crossoverType)
        else:
            child = parent2.choose(crossoverType)

    return child


# go to mutation function
def mutationF(mutationR, mutationP, mutationT, child, mean, maxF):
    fitness = child.fitness()
    rand = random.random()
    if (fitness + 1) != 0:
        newP = (0.99 * (1 / (fitness + 1)))
    else:
        newP = (0.99 * (1 / fitness))

    if mutationR == 1:
        if rand < mutationP:
            child.mutation(mutationT)
    elif mutationR == 2:
        if rand < evolution:
            child.mutation(mutationT)
    elif mutationR == 3:
        if fitness > mean:
            temp = per25
        else:
            temp = per75
        if rand < temp:
            child.mutation(mutationT)
    elif mutationR == 4:
        if fitness > maxF:
            temp = per25
        else:
            temp = per75
        if notImproved != 5:
            temp += 0.5
        if rand < temp:
            child.mutation(mutationT)
    elif mutationR == 5:
        if rand < newP:
            child.mutation(mutationT)


# details of every generation
def printGeneration1(numOfGen, WordR):
    for i in range(numOfGen):
        print(f"generations {i}:")

        print(f"max fitness {max(WordR.fitnessP[i])}")
        print(f"max binary fitness {max(WordR.binaryFitnessP[i])}")

        print(f"mean of fitness {WordR.meanP[i]}")
        print(f"std of fitness {WordR.stdP[i]}")

        print(f"selection pressure - variance {WordR.varianceP[i]}")
        print(f"selection pressure - top average ratio {WordR.topAverageRP[i]}")

        print(f"genetic diversity - average hamming distance {WordR.hammingP[i]}")
        print(f"genetic diversity - average edit distance {WordR.editP[i]}")
        print(f"genetic diversity - unique alleles amount {WordR.uniqueP[i]}")

        print(f"clock ticks {WordR.clockTicksTimesP[i]} seconds")
        print()
    print(f"elapsed time {WordR.elapsedTime} seconds")
    print()


# details of every generation
def printGeneration2(numOfGen, QueensR):
    for i in range(numOfGen):
        print(f"generations {i}:")

        print(f"max fitness {max(QueensR.fitnessP[i])}")

        print(f"mean of fitness {QueensR.meanP[i]}")
        print(f"std of fitness {QueensR.stdP[i]}")

        print(f"selection pressure - variance {QueensR.varianceP[i]}")
        print(f"selection pressure - top average ratio {QueensR.topAverageRP[i]}")

        print(f"genetic diversity - average kendall tau distance {QueensR.kendallTP[i]}")
        print(f"genetic diversity - unique permutations amount {QueensR.uniqueP[i]}")

        print(f"clock ticks {QueensR.clockTicksTimesP[i]} seconds")
        print()
    print(f"elapsed time {QueensR.elapsedTime} seconds")
    print()


# details of every generation
def printGeneration3(numOfGen, BinR):
    for i in range(numOfGen):
        print(f"generations {i}:")

        print(f"max fitness {max(BinR.fitnessP[i])}")
        print(f"max first fit {max(BinR.firstFitP[i])}")

        print(f"mean of fitness {BinR.meanP[i]}")
        print(f"std of fitness {BinR.stdP[i]}")

        print(f"selection pressure - variance {BinR.varianceP[i]}")
        print(f"selection pressure - top average ratio {BinR.topAverageRP[i]}")

        print(f"genetic diversity - average max bin distance {BinR.ffDP[i]}")
        print(f"genetic diversity - unique permutations amount {BinR.uniqueP[i]}")

        print(f"clock ticks {BinR.clockTicksTimesP[i]} seconds")
        print()
    print(f"elapsed time {BinR.elapsedTime} seconds")
    print()
