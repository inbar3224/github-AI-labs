# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


import random


class Nqueens:
    # initialize gene
    def __init__(self, arr, i, j):
        self.rows = list(arr[i])
        self.cols = list(arr[j])
        self.age = 0

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

    # kendall tau distance
    def kendallT(self, x, y):
        n = len(y)
        good = 0
        bad = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (x[i] < x[j] and y[i] < y[j]) or (x[i] > x[j] and y[i] > y[j]):
                    good += 1
                else:
                    bad += 1

        result = (1 - ((good - bad) / (0.5 * n * (n - 1)))) * n
        return result

    # update age for every generation you survive
    def updateAge(self):
        self.age += 1

    # choose crossover
    def choose(self, crossoverType):
        if crossoverType == 0:
            return self.PMX()
        elif crossoverType == 1:
            return self.CX()

    # PMX for crossover
    def PMX(self):
        child = Nqueens([[]], 0, 0)
        child.rows = self.rows.copy()
        child.cols = self.cols.copy()

        if len(child.rows) == 1:
            return child
        else:
            temp = self.rows.copy()
            i1 = random.choice(temp)
            temp.remove(i1)
            i2 = random.choice(temp)

            index1 = child.rows.index(i1)
            index2 = child.rows.index(i2)
            a = child.rows[index1]
            child.rows[index1] = child.rows[index2]
            child.rows[index2] = a

            index1 = child.cols.index(i1)
            index2 = child.cols.index(i2)
            a = child.cols[index1]
            child.cols[index1] = child.cols[index2]
            child.cols[index2] = a

            return child

    # CX for crossover
    def CX(self):
        child = Nqueens([[]], 0, 0)
        child.rows = self.rows.copy()
        child.cols = self.cols.copy()

        if len(child.rows) == 1:
            return child
        else:
            child.rows.reverse()
            child.cols.reverse()
            return child

    # mutation
    def mutation(self, mutationT):
        if mutationT == 0:
            self.inversion()
        elif mutationT == 1:
            self.scramble()

    # inversion
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

    # scramble
    def scramble(self):
        random.shuffle(self.rows)
        random.shuffle(self.cols)

    # print details
    def printD(self):
        print(self.rows)
        print(self.cols)
        print(self.age)
