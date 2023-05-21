# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from GetParameters import *
from ReadSet import *
from MaximumD import *
from TabuSearch import *
from AntColony import *
from SimulatedAnnealing import *
from Islands import *
from CooperativePSO import *


def printMatrix(problemData):
    for i in range(len(problemData.distanceM)):
        for j in range(len(problemData.distanceM[i])):
            problemData.distanceM[i][j] = int(problemData.distanceM[i][j])

    print(problemData.distanceM)


def main():
    problemType, searchType = getParameters()
    problemData = readSet(problemType)
    print()

    # multi stage heuristic
    msh = MaximumD(problemData)

    # meta heuristic + sanity check:
    if searchType == 1:
        temp = TabuSearch(problemData)
        temp.algorithm()
    elif searchType == 2:
        temp = AntColony(problemData)
        temp.algorithm()
    elif searchType == 3:
        temp = SimulatedAnnealing(problemData)
        temp.algorithm()
    elif searchType == 4:
        temp = Islands(problemData)
        temp.algorithm()
    elif searchType == 5:
        temp = CooperativePSO(problemData)
        temp.algorithm()
    elif searchType == 6:
        temp1 = TabuSearch(problemData)
        temp1.algorithm()
        temp2 = AntColony(problemData)
        temp2.algorithm()
        temp3 = SimulatedAnnealing(problemData)
        temp3.algorithm()
        temp4 = Islands(problemData)
        temp4.algorithm()
        temp = CooperativePSO(problemData)
        temp.algorithm()


if __name__ == "__main__":
    main()