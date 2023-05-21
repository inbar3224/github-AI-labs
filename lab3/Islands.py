# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from Vehicle import *
from Functions import *


class Islands:
    def __init__(self, problemData):
        print("islands model")
        self.problemData = problemData

    def algorithm(self):
        # the list that saves visited cities - not to remove anything from 0-20 = 1-21
        cityList = self.problemData.cityList.copy()
        cityList.remove(cityList[0])

        finalSolution = []
        finalCost = []

        for j in range(len(cityList)):
            if cityList[j].number >= 23 and len(cityList) == 50:
                continue
            else:
                vehicleList = [Vehicle(i + 1, self.problemData.vehicleC, []) for i in range(self.problemData.numOfC - 1)]
                marked = {key + 1: False for key in range(len(cityList))}
                counter = 0
                i = 0
                route = [self.problemData.cityList[0]]
                solution = []

                route.append(cityList[j])
                marked[j + 1] = True
                counter += 1
                while counter < len(cityList):
                    # find city with minimum distance:
                    index = getMinimum(route[len(route) - 1].number, self.problemData.distanceM, marked)

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

                finalSolution.append(solution)
                finalCost.append(cost)

        temp = finalCost.copy()
        temp.sort()
        min = temp[0]
        index = finalCost.index(min)
        self.printResults(finalSolution[index], finalCost[index])

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

