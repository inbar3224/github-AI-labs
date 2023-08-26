# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


import numpy as np


class Vector:
    def __init__(self, temp, popS):
        np.random.shuffle(temp)
        self.vector = temp.copy()
        self.fitness = popS

    def mutation(self):
        np.random.shuffle(self.vector)