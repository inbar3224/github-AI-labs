# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from GeneticA import *
from Results import *
from bisect import bisect_left


radius = 0.5


def nichingA(popSize, numOfGen, mutationR, mutationP, PTYPE, parentS, crossoverType, mutationT, numOfQueens):
    # lists
    clockTicksTimesP = []
    population = []; generation = []
    fitnessG = []; fitnessP = []; firstFitG = []; firstFitP = []
    meanG = []; varianceG = []; stdG = []; meanP = []; varianceP = []; stdP = []
    topAverageRG = []; topAverageRP = []
    ffDG = []; ffDP = []
    uniqueG = []; uniqueP = []
    newFitness = None; values = None; roulette = None; kPool = None

    # times
    elapsedBegin = timer()
    clockTicksBegin = time.time()

    # initialize generation 0
    group = round(popSize / 20)
    for i in range(20):
        groupR = []
        for j in range(group):
            gene = createGene(PTYPE)
            groupR.append(gene)
        generation.append(groupR)
    population.append(generation)

    # fitness & first fit
    for i in generation:
        fitnessR = [gene.fitness() for gene in i]
        fitnessG.append(fitnessR)
        firstFitR = [gene.firstFit() for gene in i]
        firstFitG.append(firstFitR)
    fitnessP.append(fitnessG)
    firstFitP.append(firstFitG)

    # mean, variance, std
    for i in fitnessG:
        meanR, varianceR, stdR = meanVarianceStd(i)
        meanG.append(meanR)
        varianceG.append(varianceR)
        stdG.append(stdR)
    meanP.append(meanG)
    varianceP.append(varianceG)
    stdP.append(stdG)

    # variance (already calculated), top average, gene distance & unique alleles
    for i in range(20):
        topAverageRR = topAverage(fitnessG[i], meanG[i])
        topAverageRG.append(topAverageRR)
        ffDR = binDistance(generation[i])
        ffDG.append(ffDR)
        uniqueR = unique(generation[i], PTYPE)
        uniqueG.append(uniqueR)
    topAverageRP.append(topAverageRG)
    ffDP.append(ffDG)
    uniqueP.append(uniqueG)

    # times
    clockTicksEnd = time.time()
    clockTicksTimesP.append(clockTicksEnd - clockTicksBegin)

    # create all the other generations
    for i in range(numOfGen - 1):
        clockTicksBegin = time.time()

        for j in range(20):
            # update age of genes from previews generations
            for k in generation[j]:
                k.updateAge()

            # take only the 10% that fit the aging criteria
            elites = elitismAndAging(group, fitnessG[j], generation[j], numOfGen, 0.1)
            eliteSize = len(elites)

            # scaling and creation of roulette / getting k competitors in tournament
            newFitness = scalingFitness(fitnessG[j], meanG[j])
            values, roulette = createRoulette(newFitness)
            kPool = elitismAndAging(group, fitnessG[j], generation[j], numOfGen, 0.5)

            # update parameters for mutation
            global evolution
            evolution = 1 - (i / numOfGen)

            # parent selection, crossover and mutation operators
            matrix = distanceMatrix(generation[j])
            newG = [shared(generation[j], matrix)]

            offspring = []
            while len(offspring) < group - eliteSize:
                parent1, parent2 = psFunction(parentS, roulette, newFitness, generation[j], kPool)
                answer = radius(parent1, parent2)
                child = crossoverF(crossoverType, PTYPE, parent1, parent2)
                if PTYPE == 2:
                    child2 = crossoverF(crossoverType, PTYPE, parent2, parent1)
                    probability(parent1, parent2, child, child2)
                    c1, c2 = select(parent1, parent2, child, child2)
                mutationF(mutationR, mutationP, mutationT, child, meanG[j], max(fitnessG[j]))
                offspring.append(child)
            generation[j] = elites + offspring

        population.append(generation)

        # fitness & first fit
        for i in generation:
            fitnessR = [gene.fitness() for gene in i]
            fitnessG.append(fitnessR)
            firstFitR = [gene.firstFit() for gene in i]
            firstFitG.append(firstFitR)
        fitnessP.append(fitnessG)
        firstFitP.append(firstFitG)

        # mean, variance, std
        for i in fitnessG:
            meanR, varianceR, stdR = meanVarianceStd(i)
            meanG.append(meanR)
            varianceG.append(varianceR)
            stdG.append(stdR)
        meanP.append(meanG)
        varianceP.append(varianceG)
        stdP.append(stdG)

        # variance (already calculated), top average, gene distance & unique alleles
        for i in range(20):
            topAverageRR = topAverage(fitnessG[i], meanG[i])
            topAverageRG.append(topAverageRR)
            ffDR = binDistance(generation[i])
            ffDG.append(ffDR)
            uniqueR = unique(generation[i], PTYPE)
            uniqueG.append(uniqueR)
        topAverageRP.append(topAverageRG)
        ffDP.append(ffDG)
        uniqueP.append(uniqueG)

        clockTicksEnd = time.time()
        clockTicksTimesP.append(clockTicksEnd - clockTicksBegin)

    # elapsed time
    elapsedEnd = timer()
    elapsedTime = elapsedEnd - elapsedBegin

    return BinR(clockTicksTimesP, elapsedTime, fitnessP, firstFitP, meanP, stdP, varianceP, topAverageRP, ffDP, uniqueP)


# details of every generation
def printGeneration4(numOfGen, BinR):
    for i in range(numOfGen):
        print(f"generations {i}:")

        fitness = [max(BinR.fitnessP[i][j]) for j in range(20)]
        print(BinR.fitnessP[i])
        firstFit = [max(BinR.firstFitP[i][j]) for j in range(20)]
        mean = [BinR.meanP[i][j] for j in range(20)]
        std = [BinR.stdP[i][j] for j in range(20)]
        variance = [BinR.varianceP[i][j] for j in range(20)]
        topA = [BinR.topAverageRP[i][j] for j in range(20)]
        maxBin = [BinR.ffDP[i][j] for j in range(20)]
        unique = [BinR.uniqueP[i][j] for j in range(20)]

        print(f"max fitness {fitness}")
        print(f"max first fit {firstFit}")

        print(f"mean of fitness {mean}")
        print(f"std of fitness {std}")

        print(f"selection pressure - variance {variance}")
        print(f"selection pressure - top average ratio {topA}")

        print(f"genetic diversity - average max bin distance {maxBin}")
        print(f"genetic diversity - unique permutations amount {unique}")

        print(f"clock ticks {BinR.clockTicksTimesP[i]} seconds")
        print()
    print(f"elapsed time {BinR.elapsedTime} seconds")
    print()


# distance matrix
def distanceMatrix(group):
    size = len(group)
    matrix = numpy.zeros((size, size))

    for i in size:
        for j in size:
            matrix[i][j] = group[i].distance(group[j])

    return matrix


# shared fitness
def shared(gene, matrix):
    return gene.fitness / sum(matrix[0])


# radius
def radius(parent1, parent2):
    if parent1 + parent2 < radius:
        return True
    else:
        return False


# give probability
def probability(parent1, parent2, child1, child2):
    arr = [parent1.fitness(), parent2.fitness(), child1.fitness(), child2.fitness()]
    arr2 = [arr[i] / sum(arr) for i in range(4)]
    return arr2


# choose between parents and children
def select(parent1, parent2, child1, child2):
    arr = [parent1.fitness(), parent2.fitness(), child1.fitness(), child2.fitness()]
    arr2 = [parent1, parent2, child1, child2]

    index1 = max(arr)
    arr.remove(index1)
    index2 = max(arr)

    return arr2[index1], arr2[index2]


# creates clusters
def clusters(generation):
    k = random.randint(1, 20)
    gen = generation.copy()
    values = []

    for i in range(k):
        choice = random.choice(gen)
        values.append([choice])
        gen.remove(choice)

    for i in range(len(gen)):
        index = BinarySearch(values, gen[i])
        values[index].append(gen[i])

    return values


# binary search
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return (i-1)
    else:
        return -1
