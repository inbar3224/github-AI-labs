# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0
import random


def getMinimum(cityNumber, distanceM, marked):
    # distance row
    distanceRow = distanceM[cityNumber].copy()

    # remove row
    removeRow = distanceM[cityNumber].copy()
    removeRow.sort()
    removeRow.remove(0)

    index = 0
    while index == 0:
        min = removeRow[0]
        index = distanceRow.index(min)

        if index == 0:
            removeRow.remove(removeRow[0])
            if len(removeRow) == 0:
                return -1
            else:
                min = removeRow[0]
                index = distanceRow.index(min)

        if marked[index] == False:
            marked[index] = True
            return index
        else:
            removeRow.remove(removeRow[0])
            if len(removeRow) == 0:
                return -1
            else:
                index = 0


def getRandom(numberOfCities, marked):
    numberOfCities -= 1
    numbers = [i + 1 for i in range(numberOfCities)]
    i = 0

    while i < numberOfCities:
        index = random.choice(numbers)
        if marked[index] == False:
            marked[index] = True
            return index
        else:
            numbers.remove(index)
            if len(numbers) == 0:
                return -1


