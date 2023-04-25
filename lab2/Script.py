# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from Parameters import *
from Niching import *
from Island import *


def first():
    m = "Hello!\n" \
        "This section is dedicated to testing the effects of binary bulls' eye heuristic, similarity metrics and " \
        "different types of mutation probability.\n" \
        "We would run the algorithm for each of the 7 problems: strings, queens and 5 sets of bin packing\n"
    print(m)

    print("strings")
    popSize, numOfGen, mutationR, mutationP, parentS, crossoverType = getParameters(1)
    print("the algorithm is currently running. please wait for results")
    results1 = geneticA(popSize, numOfGen, mutationR, mutationP, 1, parentS, crossoverType, 0, 0)
    printGeneration1(numOfGen, results1)

    print("queens")
    popSize, numOfGen, mutationR, mutationP, parentS, crossoverType, mutationT, numOfQueens = getParameters(2)
    print("the algorithm is currently running. please wait for results")
    results2 = geneticA(popSize, numOfGen, mutationR, mutationP, 2, parentS, crossoverType, mutationT, numOfQueens)
    printGeneration2(numOfGen, results2)

    print("bin packing")
    popSize, numOfGen, mutationR, mutationP, parentS, crossoverType, mutationT = getParameters(3)
    print("the algorithm is currently running. please wait for results")
    # set 1
    results3 = geneticA(popSize, numOfGen, mutationR, mutationP, 3, parentS, crossoverType, mutationT, 0)
    # set 2
    results4 = geneticA(popSize, numOfGen, mutationR, mutationP, 4, parentS, crossoverType, mutationT, 0)
    # set 3
    results5 = geneticA(popSize, numOfGen, mutationR, mutationP, 5, parentS, crossoverType, mutationT, 0)
    # set 4
    results6 = geneticA(popSize, numOfGen, mutationR, mutationP, 6, parentS, crossoverType, mutationT, 0)
    # set 5
    results7 = geneticA(popSize, numOfGen, mutationR, mutationP, 7, parentS, crossoverType, mutationT, 0)
    printGeneration3(numOfGen, results3)
    printGeneration3(numOfGen, results4)
    printGeneration3(numOfGen, results5)
    printGeneration3(numOfGen, results6)
    printGeneration3(numOfGen, results7)


def second():
    m = "This section is dedicated to testing the effects of niching, crowding and clustering.\n" \
        "We would run the algorithms for the bin packing problem\n"
    print(m)

    popSize, numOfGen, mutationR, mutationP, parentS, crossoverType, mutationT = getParameters(3)
    print("press 1 for niching, 2 for crowding, 3 for clustering")
    temp = input()
    try:
        nType = int(temp)
        if nType < 1 or nType > 3:
            print("the value received is not within range. putting default value: 1")
    except ValueError:
        print("the value received was not a number. putting default value: 1")
    print("the algorithm is currently running. please wait for results")
    results3 = nichingA(popSize, numOfGen, mutationR, mutationP, 3, parentS, crossoverType, mutationT, 0)
    printGeneration4(numOfGen, results3)


def third():
    m = "This section deals with the island problem. It has a fixed number of 100 generations, 100 genes per generation"
    print(m)
    ii = islandA(100, 100, 4, 0, 3, 3, 3, 3, 3)


if __name__ == "__main__":
    first()
    second()
    third()