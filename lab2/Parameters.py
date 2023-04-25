# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


# get initial parameters
def getParameters(type):
    m = "enter mutation rate: " \
        "1 for basic, " \
        "2 for non uniform, " \
        "3 for adaptive, " \
        "4 for THM, and 5 for self adaptive"

    # population size
    print("enter population size - number between 1 and 1000:")
    temp = input()
    try:
        popSize = int(temp)
        if popSize < 1 or popSize > 1000:
            print("the value received is not within range. putting default value: 100")
            popSize = 100
    except ValueError:
        print("the value received was not a number. putting default value: 100")
        popSize = 100

    # number of generations
    print("enter number of generations - number between 1 and 1000:")
    temp = input()
    try:
        numOfGen = int(temp)
        if numOfGen < 1 or numOfGen > 1000:
            print("the value received is not within range. putting default value: 100")
            numOfGen = 100
    except ValueError:
        print("the value received was not a number. putting default value: 100")
        numOfGen = 100

    # mutation rate
    print(m)
    temp = input()
    try:
        mutationR = int(temp)
        if mutationR < 1 or mutationR > 5:
            print("the value received is not within range. putting default value: 1")
            mutationR = 1
    except ValueError:
        print("the value received was not a number. putting default value: 1")
        mutationR = 1

    # percentage of mutation
    mutationP = 0
    if mutationR == 1:
        print("enter percentage of mutation - number between 0 and 1:")
        temp = input()
        try:
            mutationP = float(temp)
            if mutationP < 0 or mutationP > 1:
                print("the value received is not within range. putting default value: 0.5")
                mutationP = 0.5
        except ValueError:
            print("the value received was not a number. putting default value: 0.5")
            mutationP = 0.5
    else:
        mutationP = 0

    # parent selection
    print("enter parent selection: 0 for RWS, 1 for SUS, 2 for ranking and tournament:")
    temp = input()
    try:
        parentS = int(temp)
        if parentS < 0 or parentS > 2:
            print("the value received is not within range. putting default value: 2")
            parentS = 2
    except ValueError:
        print("the value received was not a number. putting default value: 2")
        parentS = 2

    # crossover
    crossoverType = 0
    if type == 1:
        print("enter crossover type: 1 for single point, 2 for two points, and 3 for uniform")
        temp = input()
        try:
            crossoverType = int(temp)
            if crossoverType < 0 or crossoverType > 3:
                print("the value received is not within range. putting default value: 1")
                crossoverType = 1
        except ValueError:
            print("the value received was not a number. putting default value: 1")
            crossoverType = 1
    elif type >= 2:
        print("enter crossover type: 0 for PMX, 1 for CX:")
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
    mutationT = 0
    if type >= 2:
        print("enter mutation type: 0 for inversion, 1 for scramble:")
        temp = input()
        try:
            mutationT = int(temp)
            if mutationT < 0 or mutationT > 1:
                print("the value received is not within range. putting default value: 1")
                mutationT = 1
        except ValueError:
            print("the value received was not a number. putting default value: 1")
            mutationT = 1

    # for queens only
    numOfQueens = 0
    if type == 2:
        # number of queens
        print("enter number of queens - number between 1 and 10:")
        temp = input()
        try:
            numOfQueens = int(temp)
            if numOfQueens < 1 or numOfQueens > 10:
                print("the value received is not within range. putting default value: 5")
                numOfQueens = 5
        except ValueError:
            print("the value received was not a number. putting default value: 5")
            numOfQueens = 5

    if type == 1:
        return popSize, numOfGen, mutationR, mutationP, parentS, crossoverType
    elif type == 2:
        return popSize, numOfGen, mutationR, mutationP, parentS, crossoverType, mutationT, numOfQueens
    elif type >= 3:
        return popSize, numOfGen, mutationR, mutationP, parentS, crossoverType, mutationT
