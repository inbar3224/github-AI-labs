# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


class City:
    # constructor
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.cityDemand = 0

    # we only get the city demand later
    def setDemand(self, demand):
        self.cityDemand = demand

    # print details
    def printD(self):
        print(self.number, self.x, self.y, self.cityDemand)