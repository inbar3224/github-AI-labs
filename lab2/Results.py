# Inbar Lev Tov 316327246
# Gal Gibly 315093435
# Note that the assignment was done with python version 3.11.0


class Results:
    def __init__(self, clockTicksTimesP, elapsedTime, fitnessP, meanP, stdP, varianceP, topAverageRP, uniqueP):
        self.clockTicksTimesP = clockTicksTimesP
        self.elapsedTime = elapsedTime
        self.fitnessP = fitnessP
        self.meanP = meanP
        self.stdP = stdP
        self.varianceP = varianceP
        self.topAverageRP = topAverageRP
        self.uniqueP = uniqueP


class WordR(Results):
    def __init__(self, clockTicksTimesP, elapsedTime, fitnessP, binaryFitnessP, meanP, stdP, varianceP,
                 topAverageRP, hammingP, editP, uniqueP):
        Results.__init__(self, clockTicksTimesP, elapsedTime, fitnessP, meanP, stdP, varianceP, topAverageRP, uniqueP)
        self.binaryFitnessP = binaryFitnessP
        self.hammingP = hammingP
        self.editP = editP


class QueensR(Results):
    def __init__(self, clockTicksTimesP, elapsedTime, fitnessP, meanP, stdP, varianceP, topAverageRP, kendallTP, uniqueP):
        Results.__init__(self, clockTicksTimesP, elapsedTime, fitnessP, meanP, stdP, varianceP, topAverageRP, uniqueP)
        self.kendallTP = kendallTP


class BinR(Results):
    def __init__(self, clockTicksTimesP, elapsedTime, fitnessP, firstFitP, meanP, stdP, varianceP, topAverageRP, ffDP,
                 uniqueP):
        Results.__init__(self, clockTicksTimesP, elapsedTime, fitnessP, meanP, stdP, varianceP, topAverageRP, uniqueP)
        self.firstFitP = firstFitP
        self.ffDP = ffDP
