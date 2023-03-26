# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0

from functions import *
from problem1 import *
from problem2 import *
from problem3 import *
from problem4 import *
from problem5 import *

def main():
    # get parameters for string
    print("welcome")
    print("this is the first iteration of the genetic algorithm program. please insert parameters:")
    populationSize, numberOfGenerations, crossoverType, mutationType = getParameters(1)
    print("the algorithm is currently running. please wait for results")
    # initialize population
    population, clockTicks, fitness, mean, variance, std, bullsEye, elapsedTime = createGenePool(populationSize, numberOfGenerations, crossoverType, mutationType)
    # printing
    printDetails(numberOfGenerations, mean, std, clockTicks, elapsedTime)
    # histogram of fitness
    print("press A (capslock) to show the fitness histograms of 3 generations: the first, the middle and the last generation")
    temp = input()
    while temp != 'A':
        print("press A (capslock)")
        temp = input()
    fitnessHis(numberOfGenerations, fitness)
    print("press B (capslock) to show the bulls eye histograms of 3 generations: the first, the middle and the last generation")
    temp = input()
    while temp != 'B':
        print("press B (capslock)")
        temp = input()
    fitnessHis(numberOfGenerations, bullsEye)
    print()

    # n queens
    print("second iteration - n queens. please insert parameters:")
    populationSize, numberOfGenerations, numberOfQueens, parentS, crossoverType, mutationType = getParameters(3)
    print("the algorithm is currently running. please wait for results")
    mean, std, variance, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime = runNQueens(populationSize, numberOfGenerations, numberOfQueens, parentS, crossoverType, mutationType)
    # printing
    printForQueen(numberOfGenerations, mean, std, variance, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime)
    print()

    print("third iteration - bin packing:")
    # bin packing problem 1
    print("problem number 1. please insert parameters:")
    populationSize, numberOfGenerations, parentS, crossoverType, mutationType = getParameters(2)
    print("the algorithm is currently running. please wait for results")
    mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime = runBinPacking(populationSize, numberOfGenerations, per1, parentS, crossoverType, mutationType)
    printForBin(numberOfGenerations, mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime)
    print()

    # bin packing problem 2
    print("problem number 2. please insert parameters:")
    populationSize, numberOfGenerations, parentS, crossoverType, mutationType = getParameters(2)
    print("the algorithm is currently running. please wait for results")
    mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime = runBinPacking(populationSize, numberOfGenerations, per2, parentS, crossoverType, mutationType)
    printForBin(numberOfGenerations, mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime)
    print()

    # bin packing problem 3
    print("problem number 3. please insert parameters:")
    populationSize, numberOfGenerations, parentS, crossoverType, mutationType = getParameters(2)
    print("the algorithm is currently running. please wait for results")
    mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime = runBinPacking(populationSize, numberOfGenerations, per3, parentS, crossoverType, mutationType)
    printForBin(numberOfGenerations, mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime)
    print()

    # bin packing problem 4
    print("problem number 4. please insert parameters:")
    populationSize, numberOfGenerations, parentS, crossoverType, mutationType = getParameters(2)
    print("the algorithm is currently running. please wait for results")
    mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime = runBinPacking(populationSize, numberOfGenerations, per4, parentS, crossoverType, mutationType)
    printForBin(numberOfGenerations, mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime)
    print()

    # bin packing problem 5
    print("problem number 5. please insert parameters:")
    populationSize, numberOfGenerations, parentS, crossoverType, mutationType = getParameters(2)
    print("the algorithm is currently running. please wait for results")
    mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime = runBinPacking(populationSize, numberOfGenerations, per5, parentS, crossoverType, mutationType)
    printForBin(numberOfGenerations, mean, std, variance, firstFitMean, topAverage, geneDistance, permutationsNumber, clockTicksTimes, elapsedTime)
    print()

    print("press A (capslock) to finish the program")
    temp = input()
    while temp != 'A':
        print("press A (capslock)")
        temp = input()

    numberOfBins = [48, 49, 46, 49, 50]

if __name__ == "__main__":
    main()
