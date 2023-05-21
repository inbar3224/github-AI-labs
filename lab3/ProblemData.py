# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


class ProblemData:
    def __init__(self, numberOfCities, vehicleCapacity, cityList, distanceM):
        self.numOfC = numberOfCities
        self.vehicleC = vehicleCapacity
        self.cityList = cityList
        self.distanceM = distanceM
        self.wareHouse = cityList[0]
        self.vehicles = 0
        self.bestTour = []
        self.bestCost = 0
        self.solution = []
