# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from Vehicle import *


class CooperativePSO:
    def __init__(self, problemData):
        print("cooperative pso")
        self.problemData = problemData

    def algorithm(self):
        vehicleList = [Vehicle(i + 1, self.problemData.vehicleC, []) for i in range(self.problemData.numOfC - 1)]

        cityList = self.problemData.cityList.copy()
        cityList.remove(cityList[0])
        cityList.sort(key=lambda i: i.x, reverse = True)
        counter = 0
        i = 0
        route = [self.problemData.cityList[0]]
        solution = []

        while counter < len(cityList):
            if vehicleList[i].capacity >= cityList[counter].cityDemand:
                vehicleList[i].capacity -= cityList[counter].cityDemand
                route.append(cityList[counter])
                counter += 1
            else:
                route.append(self.problemData.cityList[0])
                vehicleList[i].setRoute(route)
                solution.append(vehicleList[i])
                i += 1
                route = [self.problemData.cityList[0]]

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
