# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


import random
import copy


class BinPacking:
    # initialize gene
    def __init__(self, best):
        copyL = best.copy()
        self.numberOfItems = 120
        self.gene = []

        for i in range(self.numberOfItems):
            number = random.choice(copyL)
            self.gene.append(number)
            copyL.remove(number)

        self.age = 0
        self.capacity = 150
        self.maxFF = 0

    # measure fitness
    def fitnessD(self, best):
        score = 0
        for i in range(self.numberOfItems):
            if self.gene[i] == best[i]:
                score += 1
        return score

    # first fit
    def firstFit(self):
        remain = [self.capacity]
        sol = [[]]
        s = self.gene.copy()

        for item in s:
            for j, free in enumerate(remain):
                if free >= item:
                    remain[j] -= item
                    sol[j].append(item)
                    break
            else:
                sol.append([item])
                remain.append(self.capacity - item)

        self.maxFF = sum(max(sol))
        return len(sol)

    # update age for every generation you survive
    def updateAge(self):
        self.age += 1

    # mutation
    def mutation(self, mutationT):
        if mutationT == 0:
            self.inversion()
        elif mutationT == 1:
            self.scramble()

    # inversion
    def inversion(self):
        point = 60
        temp = [self.gene[i] for i in range(point, 120)]
        temp.reverse()
        self.orderOfInsertion = temp + self.gene[0: point]

    # scramble
    def scramble(self):
        random.shuffle(self.gene)

    # print details
    def printD(self):
        print(self.gene)
        print(self.age)

    def distance(self, other):
        return self.maxFF - other.maxFF

best = [[98, 50, 98, 49, 98, 49, 96, 49, 96, 47, 94, 55, 93, 57, 93, 57, 92, 58, 91, 59, 91, 58, 90, 60,
         87, 62, 86, 64, 85, 62, 85, 60, 84, 66, 84, 58, 84, 57, 84, 57, 84, 55, 83, 67, 83, 55, 82, 46,
         20, 82, 45, 23, 81, 69, 80, 70, 80, 70, 80, 70, 79, 71, 79, 69, 78, 72, 78, 69, 78, 46, 26, 78,
         45, 27, 76, 74, 74, 73, 73, 44, 33, 73, 44, 33, 73, 43, 33, 43, 43, 41, 23, 43, 42, 41, 24, 42,
         42, 41, 25, 42, 42, 39, 27, 39, 38, 38, 35, 38, 37, 36, 36, 36, 32, 32, 30, 30, 30, 29, 28, 25],
        [100, 50, 100, 49, 99, 49, 99, 48, 98, 52, 98, 52, 98, 48, 98, 47, 98, 47, 97, 53, 97, 53, 97, 53,
         95, 55, 95, 55, 95, 53, 94, 53, 92, 58, 90, 60, 90, 60, 88, 62, 88, 61, 85, 65, 82, 68, 81, 67,
         81, 67, 81, 67, 80, 70, 80, 70, 80, 70, 79, 71, 79, 67, 78, 72, 78, 72, 76, 74, 75, 75, 66, 66,
         65, 64, 20, 61, 60, 29, 59, 57, 33, 57, 57, 36, 53, 47, 46, 46, 45, 45, 45, 44, 43, 43, 43, 41,
         23, 39, 39, 39, 32, 38, 38, 37, 36, 36, 35, 30, 30, 29, 27, 27, 27, 25, 24, 23, 22, 22, 22, 20],
        [100, 50, 100, 50, 98, 51, 97, 53, 97, 53, 96, 51, 94, 48, 92, 57, 92, 48, 91, 59, 91, 59, 90, 60,
         90, 48, 90, 47, 88, 62, 85, 65, 84, 66, 84, 66, 84, 66, 83, 67, 81, 69, 81, 69, 80, 70, 80, 68,
         80, 68, 80, 67, 79, 67, 79, 67, 79, 64, 76, 73, 76, 74, 75, 75, 64, 46, 38, 64, 46, 38, 64, 46,
         38, 64, 45, 41, 62, 45, 42, 61, 44, 42, 61, 41, 28, 20, 37, 37, 37, 37, 40, 21, 21, 22, 23, 23,
         36, 36, 24, 24, 30, 35, 25, 34, 26, 29, 34, 26, 33, 27, 29, 32, 28, 31, 29, 29, 35, 32, 32, 31],
        [100, 47, 100, 46, 99, 46, 97, 53, 97, 52, 97, 46, 96, 54, 96, 54, 95, 54, 95, 27, 26, 95, 27, 26,
         95, 42, 94, 56, 92, 58, 92, 58, 91, 59, 91, 20, 39, 90, 60, 90, 60, 90, 42, 89, 61, 88, 62, 87,
         63, 87, 63, 86, 63, 86, 24, 37, 85, 65, 84, 66, 84, 34, 32, 84, 37, 28, 83, 67, 82, 68, 82, 33,
         35, 81, 43, 25, 80, 70, 80, 44, 26, 80, 45, 25, 79, 45, 25, 78, 42, 30, 76, 45, 29, 75, 35, 40,
         74, 35, 40, 74, 35, 40, 73, 43, 34, 73, 48, 29, 73, 56, 21, 71, 57, 22, 71, 47, 32, 70, 49, 31],
        [99, 50, 99, 50, 98, 52, 98, 52, 97, 53, 97, 49, 96, 48, 95, 55, 92, 57, 92, 57, 92, 57, 92, 57,
         91, 59, 91, 57, 91, 56, 90, 60, 89, 61, 89, 60, 88, 45, 87, 45, 87, 43, 20, 87, 43, 20, 86, 42,
         21, 85, 65, 84, 66, 84, 65, 84, 42, 24, 84, 42, 24, 82, 68, 82, 68, 81, 69, 79, 71, 78, 72, 78,
         71, 77, 73, 77, 73, 76, 74, 76, 73, 75, 75, 75, 73, 71, 71, 70, 69, 69, 69, 69, 67, 42, 42, 41,
         25, 40, 40, 39, 31, 39, 37, 37, 37, 36, 35, 34, 32, 32, 31, 30, 28, 27, 23, 21, 21, 21, 21, 20]]


class BinPi(BinPacking):
    # initialize gene
    def __init__(self, index):
        BinPacking.__init__(self, best[index])
        self.index = index

    # measure fitness
    def fitness(self):
        return BinPacking.fitnessD(self, best[self.index])

    # choose crossover
    def choose(self, crossoverType):
        if crossoverType == 0:
            return self.PMX()
        elif crossoverType == 1:
            return self.CX()

    # PMX for crossover
    def PMX(self):
        child = copy.copy(self)
        child.gene = self.gene.copy()

        temp = self.gene.copy()
        i1 = random.choice(temp)
        temp.remove(i1)
        i2 = random.choice(temp)

        index1 = child.gene.index(i1)
        index2 = child.gene.index(i2)
        a = child.gene[index1]
        child.gene[index1] = child.gene[index2]
        child.gene[index2] = a

        return child

    # CX for crossover
    def CX(self):
        child = copy.copy(self)
        child.gene = self.gene.copy()
        child.gene.reverse()
        return child
