# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


class Vehicle:
    def __init__(self, ID, capacity, route):
        self.ID = ID
        self.capacity = capacity
        self.route = route

    def setRoute(self, route):
        self.route = route

    def printD(self):
        g = [i.number for i in self.route]
        print(f"route #{self.ID}: {g}")