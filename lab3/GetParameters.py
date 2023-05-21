# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


def getParameters():
    print("we have 3 sets of problems and the option to get an ackley check:")
    print("press 1 for set 1, 2 for set 2, 3 for set 3:")
    temp = input()
    try:
        problemType = int(temp)
        if problemType < 1 or problemType > 3:
            print("the value received is not within range. putting default value: 1")
            problemType = 1
    except ValueError:
        print("the value received was not a number. putting default value: 1")
        problemType = 1

    print("press 1 for tabu search, 2 for ant colony, 3 for simulated annealing, 4 for island model, 5 for PSO, 6 for all of them")
    temp = input()
    try:
        searchType = int(temp)
        if searchType < 1 or searchType > 6:
            print("the value received is not within range. putting default value: 1")
            searchType = 1
    except ValueError:
        print("the value received was not a number. putting default value: 1")
        searchType = 1

    return problemType, searchType