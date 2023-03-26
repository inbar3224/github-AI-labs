# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0

import random

class BinPacking:
    def __init__(self, arr, i):
        self.age = 0
        self.orderOfInsertion = arr[i]
        self.capacity = 150
        self.numberOfItems = 120

    # print to check permutations
    def printD(self):
        print(self.age, self.orderOfInsertion)

    # count minimal number of bins required
    def fitness(self):
        remain = [self.capacity]
        sol = [[]]
        s = [self.orderOfInsertion[i] for i in range(self.numberOfItems)]

        for item in sorted(s, reverse=True):
            for j, free in enumerate(remain):
                if free >= item:
                    remain[j] -= item
                    sol[j].append(item)
                    break
            else:
                sol.append([item])
                remain.append(self.capacity - item)
        return len(sol)

    # first fit
    def firstFit(self):
        remain = [self.capacity]
        sol = [[]]
        s = [self.orderOfInsertion[i] for i in range(self.numberOfItems)]

        for item in s:
            for j, free in enumerate(remain):
                if free >= item:
                    remain[j] -= item
                    sol[j].append(item)
                    break
            else:
                sol.append([item])
                remain.append(self.capacity - item)
        return len(sol)

    # update age for every generation you survive
    def updateAge(self):
        self.age += 1

    # inversion mutation
    def inversion(self):
        point = 60
        temp = [self.orderOfInsertion[i] for i in range(point, 120)]
        temp.reverse()
        self.orderOfInsertion = temp + self.orderOfInsertion[0: point]

    # scramble mutation
    def scramble(self):
        temp = [self.orderOfInsertion[i] for i in range(120)]
        for i in range(120):
            val = random.choice(temp)
            self.orderOfInsertion[i] = val
            temp.remove(val)
