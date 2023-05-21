# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from Vehicle import *


class MaximumD:
    def __init__(self, problemData):
        m = "multi stage heuristic:\n" \
            "we would sort our neighborhood based on maximum demand, " \
            "and than create a journey for each vehicle under the constraint of vehicle capacity"
        print(m)

        solution = self.findingRoute(problemData)
        cost = self.calculatingCost(solution, problemData)

        self.printResults(solution, cost)

    def findingRoute(self, problemData):
        vehicleList = [Vehicle(i + 1, problemData.vehicleC, []) for i in range(problemData.numOfC - 1)]

        cityList = problemData.cityList.copy()
        cityList.remove(cityList[0])
        cityList.sort(key = lambda i : i.cityDemand, reverse = True)
        counter = 0
        i = 0
        route = [problemData.cityList[0]]
        solution = []

        while counter < len(cityList):
            if vehicleList[i].capacity >= cityList[counter].cityDemand:
                vehicleList[i].capacity -= cityList[counter].cityDemand
                route.append(cityList[counter])
                counter += 1
            else:
                route.append(problemData.cityList[0])
                vehicleList[i].setRoute(route)
                solution.append(vehicleList[i])
                i += 1
                route = [problemData.cityList[0]]

        # dealing with last iteration of loop
        route.append(problemData.cityList[0])
        vehicleList[i].setRoute(route)
        solution.append(vehicleList[i])

        return solution

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
