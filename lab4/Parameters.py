# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


# get initial parameters
def getParameters():
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

    # vector size
    print("enter vector size: press 6 or 16")
    temp = input()
    try:
        vectorS = int(temp)
        if vectorS != 6 and vectorS != 16:
            print("the value received is not within range. putting default value: 6")
            vectorS = 6
    except ValueError:
        print("the value received was not a number. putting default value: 1")
        vectorS = 6

    return popSize, numOfGen, vectorS
