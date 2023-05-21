# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from Vehicle import *
from Functions import *


class AntColony:
    def __init__(self, problemData):
        print("ant colony")
        self.problemData = problemData

    def algorithm(self):
        vehicleList = [Vehicle(i + 1, self.problemData.vehicleC, []) for i in range(self.problemData.numOfC - 1)]

        # the list that saves visited cities - not to remove anything from 0-20 = 1-21
        cityList = self.problemData.cityList.copy()
        cityList.remove(cityList[0])

        # the list of marked cities - true or false 1-21
        marked = {key + 1: False for key in range(len(cityList))}

        counter = 0
        i = 0
        route = [self.problemData.cityList[0]]
        solution = []

        while counter < len(cityList):
            # find random city:
            index = getRandom(self.problemData.numOfC, marked)

            if index != -1:
                # check if we can answer demand
                if vehicleList[i].capacity >= cityList[index - 1].cityDemand:
                    vehicleList[i].capacity -= cityList[index - 1].cityDemand
                    route.append(cityList[index - 1])
                    counter += 1
                else:
                    route.append(self.problemData.cityList[0])
                    vehicleList[i].setRoute(route)
                    solution.append(vehicleList[i])
                    i += 1
                    route = [self.problemData.cityList[0]]
                    marked[index] = False
            else:
                break

        # dealing with last iteration of loop
        route.append(self.problemData.cityList[0])
        vehicleList[i].setRoute(route)
        solution.append(vehicleList[i])

        cost = self.calculatingCost(solution, self.problemData)
        self.printResults(solution, cost)

    def calculatingCost(self, solution, problemData):
        sum = 0

        for vehicle in solution:
            for i in range(len(vehicle.route) - 1):
                sum += problemData.distanceM[i][i + 1]

        return sum

    def printResults(self, solution, cost):
        for i in solution:
            i.printD()
        print(f"cost: {cost}")
        print()
