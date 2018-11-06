import numpy as np
import random


class GestureModel:
    I = [0] * 2200
    Q = [0] * 2200
    bsRecord = []
    curDataCountI = 0
    curDataCountQ = 0

    def __init__(self, ui):
        self.ui = ui

        self.I = [0] * 2200
        self.Q = [0] * 2200
        self.bsRecord = [0] * 4400

    def Normalize(self, data):
        m = np.mean(data)
        mx = max(data)
        mn = min(data)
        return [(float(i) - m) / (mx - mn) for i in data]

    def updateI(self, strNewI):

        value_i = strNewI.split(",")

        floatI = []

        for i in value_i:
            floatI.append(float(i))

        normalI = self.Normalize(floatI)

        self.I[self.curDataCountI * 110:(self.curDataCountI + 1) * 110] = normalI
        self.curDataCountI = self.curDataCountI + 1
        self.curDataCountI = self.curDataCountI % 20
        self.ui.updateI(self.I)

    def updateQ(self, strNewQ):
        value_1 = strNewQ.split(",")

        floatQ = []

        for i in value_1:
            floatQ.append(float(i))

        normalQ = self.Normalize(floatQ)

        self.Q[self.curDataCountQ * 110:(self.curDataCountQ + 1) * 110] = normalQ
        self.curDataCountQ = self.curDataCountQ + 1
        self.curDataCountQ = self.curDataCountQ % 20
        self.ui.updateQ(self.Q)
