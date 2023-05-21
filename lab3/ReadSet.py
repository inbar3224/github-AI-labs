# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


import math


from City import *
from ProblemData import *


# read and parse set from text file
def readSet(problemType):
    file = None

    if problemType == 1:
        file = open("E-n22-k4.txt", "r")
    elif problemType == 2:
        file = open("E-n33-k4.txt", "r")
    elif problemType == 3:
        file = open("E-n51-k5.txt", "r")

    for i in range(3):
        file.readline()

    # number of cities - line 4
    temp = file.readline()
    separate = [word for word in temp.split(' ')]
    numberOfCities = (int(separate[2]) - 1)

    file.readline()

    # capacity for vehicle - line 6
    temp = file.readline()
    separate = [word for word in temp.split(' ')]
    vehicleCapacity = int(separate[2])

    file.readline()

    # list of cities coordination's - line 8
    # first line is center, the rest is cities
    cityList = []
    for i in range(numberOfCities + 1):
        temp = file.readline()
        separate = [word for word in temp.split(' ')]
        city = City(i, int(separate[1]), int(separate[2]))
        cityList.append(city)

    file.readline()

    # list of cities demand - line 31
    # first line is center, the rest is cities
    for i in range(numberOfCities + 1):
        temp = file.readline()
        separate = [word for word in temp.split(' ')]
        cityList[i].setDemand(int(separate[1]))

    file.close()

    # calculate distance between cities
    distanceM = distanceMatrix(cityList, numberOfCities + 1)

    # full problem
    problemData = ProblemData(numberOfCities + 1, vehicleCapacity, cityList, distanceM)
    '''for i in cityList:
        i.printD()'''
    return problemData


# calculate distance between every 2 cities
def distanceMatrix(cityList, numOfC):
    rows = []

    # distance by the formula: sqrt((x1 - x2)^2 + (y1 - y2)^2)
    for i in range(numOfC):
        cols = []
        for j in range(numOfC):
            distance = math.sqrt(pow(cityList[j].x - cityList[i].x, 2) + pow(cityList[j].y - cityList[i].y, 2))
            cols.append(distance)
        rows.append(cols)

    return rows



