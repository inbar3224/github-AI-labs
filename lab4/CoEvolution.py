# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


from Vector import *
from Network import *
import random


class CoEvolution:
    def __init__(self, popS, genS, vectorS):
        self.popS = popS
        self.genS = genS
        self.vectorS = vectorS

        self.networkP = []
        self.vectorP = []

        # create generation 0
        temp = np.random.randint(1, 100, size = vectorS)
        for i in range(self.popS):
            self.networkP.append(Network(vectorS))
            self.vectorP.append(Vector(temp, popS))

    def evolution(self):
        maxNetworkFitness = []; maxVectorFitness = []; numOfComparators = []

        # for each generation
        for i in range(self.genS):
            # evaluate fitness
            networkF, vectorF, comparatorN = self.fitnessEvaluation()
            maxNetworkFitness.append(max(networkF))
            maxVectorFitness.append(max(vectorF))
            numOfComparators.append(min(comparatorN))

            # elite team
            eliteVector, eliteNetwork = self.elite()
            eliteSize = len(eliteVector)

            # parent selection, crossover, mutation
            offspringVector = []
            offspringNetwork = []
            self.parentVector = self.vectorP.copy()
            self.parentNetwork = self.networkP.copy()
            while len(offspringVector) < self.popS - eliteSize:
                pv1, pv2, pn1, pn2 = self.parentSelection()
                childVector, childNetwork = self.crossover(pv1, pv2, pn1, pn2)
                childVector.mutation()
                childNetwork.mutation()
                offspringVector.append(childVector)
                offspringNetwork.append(childNetwork)

            generationV = eliteVector + offspringVector
            generationN = eliteNetwork + offspringNetwork

            self.networkP = generationN.copy()
            self.vectorP = generationV.copy()

        return maxNetworkFitness, maxVectorFitness, numOfComparators

    def fitnessEvaluation(self):
        networkF = []; vectorF = []; comparatorN = []

        # for each vector and its respective network in our population
        for i in range(self.popS):
            sortedV = np.copy(self.vectorP[i].vector)
            sortedV = np.sort(sortedV)
            networkSortedV = self.networkP[i].sortVector(self.vectorP[i].vector, self.vectorS)

            networkFitness = sum(networkSortedV == sortedV)
            self.networkP[i].fitness = networkFitness
            if networkFitness == self.vectorS:
                self.vectorP[i].fitness -= 1
            if self.vectorP[i].fitness > 0:
                self.vectorP[i].fitness = self.vectorP[i].fitness - self.networkP[i].fitness

            networkF.append(self.networkP[i].fitness)
            vectorF.append(self.vectorP[i].fitness)
            comparatorN.append(self.networkP[i].numOfComparators)

        return networkF, vectorF, comparatorN

    def elite(self):
        eliteSize = int(self.popS * 0.1)

        eliteVectorI = sorted(range(self.popS), key=lambda i: self.vectorP[i].fitness, reverse=True)[:eliteSize]
        eliteNetworkI = sorted(range(self.popS), key=lambda i: self.networkP[i].fitness, reverse=True)[:eliteSize]

        eliteVector = [self.vectorP[i] for i in eliteVectorI]
        eliteNetwork = [self.networkP[i] for i in eliteNetworkI]

        return eliteVector, eliteNetwork

    def parentSelection(self):
        if len(self.parentVector) <= 1:
            self.parentVector = self.vectorP.copy()
            self.parentNetwork = self.networkP.copy()
        else:
            pv1 = random.choice(self.parentVector)
            self.parentVector.remove(pv1)
            pv2 = random.choice(self.parentVector)

            pn1 = random.choice(self.parentNetwork)
            self.parentNetwork.remove(pn1)
            pn2 = random.choice(self.parentNetwork)

            return pv1, pv2, pn1, pn2

    def crossover(self, pv1, pv2, pn1, pn2):
        childVector = Vector([1], 0)
        if pv1.fitness > pv2.fitness:
            childVector.vector = pv1.vector.copy()
            childVector.fitness = pv1.fitness
        else:
            childVector.vector = pv2.vector.copy()
            childVector.fitness = pv2.fitness

        childNetwork = Network(pn1.numOfElements)
        childNetwork.numOfComparators = pn1.numOfElements * (pn1.numOfElements - 1) // 2
        i = 0
        if pn1.fitness > pn2.fitness:
            childNetwork.comparators = np.where(i < pn1.numOfComparators / 2, pn1.comparators, pn2.comparators)
        else:
            childNetwork.comparators = np.where(i < pn2.numOfComparators / 2, pn2.comparators, pn2.comparators)

        return childVector, childNetwork

