# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0

import random

class Nqueens:
    def __init__(self, arr, i, j):
        self.age = 0
        self.rows = arr[i]
        self.cols = arr[j]

    # print to check permutations
    def printD(self):
        print(self.age, self.rows, self.cols)

    # for every collision between queens, you lose a point
    def fitness(self):
        score = 0

        for i in range(len(self.rows)):
            if i != len(self.rows) - 1:
                for j in range(i + 1, len(self.rows)):
                    if self.rows[i] == self.rows[j]:
                        score += 1
                    if self.cols[i] == self.cols[j]:
                        score += 1
                    if abs(self.rows[i] - self.rows[j]) == abs(self.cols[i] - self.cols[j]):
                        score += 1

        score *= (-1)
        return score

    # update age for every generation you survive
    def updateAge(self):
        self.age += 1

    # inversion mutation
    def inversion(self):
        if len(self.rows) == 1:
            return
        else:
            length = len(self.rows)
            point = int(length / 2)

            temp = [self.rows[i] for i in range(point, length)]
            temp.reverse()
            self.rows = temp + self.rows[0: point]
            temp = [self.cols[i] for i in range(point, length)]
            temp.reverse()
            self.cols = temp + self.cols[0: point]

    # scramble mutation
    def scramble(self):
        if len(self.rows) == 1:
            return
        else:
            length = len(self.rows)
            temp = [self.rows[i] for i in range(length)]
            for i in range(length):
                val = random.choice(temp)
                self.rows[i] = val
                self.cols[length - i - 1] = val
                temp.remove(val)
