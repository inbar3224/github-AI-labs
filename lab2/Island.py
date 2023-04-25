# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from GeneticA import *


def isF(x, y):
    return (x - 6, y - 6)


def isG(x, y):
    return (x + 4, y + 4)


def viability(x, y, range):
    if x > range or y > range:
        return False
    elif x < range or y < range:
        return False
    else:
        return True


# 1 = string, 2 = queens, 3 = bin packing
def islandA(popSize, numOfGen, mutationR, mutationP, PTYPE, parentS, crossoverType, mutationT, numOfQueens):
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


