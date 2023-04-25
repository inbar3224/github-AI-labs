# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


import random


class Word:
    target = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']
    lengthT = 13
    binaryT = ['1', '0', '0', '1', '0', '0', '0',
               '1', '1', '0', '0', '1', '0', '1',
               '1', '1', '0', '1', '1', '0', '0',
               '1', '1', '0', '1', '1', '0', '0',
               '1', '1', '0', '1', '1', '1', '1',
               '0', '1', '0', '1', '1', '0', '0',
               '0', '1', '0', '0', '0', '0', '0',
               '1', '1', '1', '0', '1', '1', '1',
               '1', '1', '0', '1', '1', '1', '1',
               '1', '1', '1', '0', '0', '1', '0',
               '1', '1', '0', '1', '1', '0', '0',
               '1', '1', '0', '0', '1', '0', '0',
               '0', '1', '0', '0', '0', '0', '1']
    lengthB = 91
    translateB = [49, 48, 48, 49, 48, 48, 48,
                  49, 49, 48, 48, 49, 48, 49,
                  49, 49, 48, 49, 49, 48, 48,
                  49, 49, 48, 49, 49, 48, 48,
                  49, 49, 48, 49, 49, 49, 49,
                  48, 49, 48, 49, 49, 48, 48,
                  48, 49, 48, 48, 48, 48, 48,
                  49, 49, 49, 48, 49, 49, 49,
                  49, 49, 48, 49, 49, 49, 49,
                  49, 49, 49, 48, 48, 49, 48,
                  49, 49, 48, 49, 49, 48, 48,
                  49, 49, 48, 48, 49, 48, 48,
                  48, 49, 48, 48, 48, 48, 49]

    # initialize gene
    def __init__(self, args):
        if type(args) != int:
            self.gene = args
        else:
            self.gene = [chr(random.randint(32, 122)) for j in range(self.lengthT)]

        number = [ord(self.gene[i]) for i in range(self.lengthT)]
        binary = [format(number[i], 'b') for i in range(self.lengthT)]
        for i in range(13):
            while len(binary[i]) < 7:
                binary[i] = '0' + binary[i]
        united = list(''.join(binary))
        self.unitedT = [ord(united[i]) for i in range(len(united))]

        self.age = 0

    # measure fitness
    def fitness(self):
        score = 0
        for i in range(self.lengthT):
            if self.gene[i] == self.target[i]:
                score += 1
        return score

    # fitness binary
    def fitnessBinary(self):
        score = 0
        for i in range(self.lengthB):
            if self.unitedT[i] == self.translateB[i]:
                score += 1
        return score / 7

    # hamming distance
    def hammingD(self, other):
        rightPlace = [self.unitedT[i] - other.unitedT[i] for i in range(self.lengthB)]
        count = rightPlace.count(0)
        return self.lengthB - count

    # edit distance
    def editD(self, other):
        a = self.gene.copy()
        b = other.gene.copy()
        return sum(i != j for i, j in zip(a, b))

    # update age for every generation you survive
    def updateAge(self):
        self.age += 1

    # crossover according to type: single point, two point, uniform
    def crossover(self, type, p2):
        point1 = random.randint(1, self.lengthT - 2)
        point2 = random.randint(point1 + 1, self.lengthT - 1)
        child = None

        if type == 1:
            # 1 point for separating parent 1 and 2
            child = self.gene[0: point1] + p2.gene[point1:]
        elif type == 2:
            # 2 points separating: parent 1 until point1, then parent 2, than parent 1 again
            child = self.gene[0: point1] + p2.gene[point1: point2] + self.gene[point2:]
        elif type == 3:
            # at each point, we choose randomly between parent1 and parent2
            child = [self.gene[i] if random.random() < 0.5 else p2.gene[i] for i in range(self.lengthT)]

        return Word(args=child)

    # mutation
    def mutation(self, mutationT):
        point = random.randint(0, self.lengthB - 1)
        newB = random.randint(48, 49)
        self.unitedT[point] = newB

        c = [chr(self.unitedT[i]) for i in range(self.lengthB)]
        c = ''.join(c)
        s = ""
        for i in range(0, len(c), 7):
            temp_data = c[i : i + 7]
            decimal_data = int(temp_data, 2)
            s += chr(decimal_data)
        self.gene = list(s)

    # print details
    def printD(self):
        print(self.gene)
        print(self.unitedT)
        print(self.age)
