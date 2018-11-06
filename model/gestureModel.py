import numpy as np
import random


class GestureModel:
    I = [0] * 2200
    Q = [0] * 2200
    bsRecord = [0] * 4400

    curDataCountI = 0
    curDataCountQ = 0
    curDataCountBs = 0

    def __init__(self, ui):
        self.ui = ui

        self.I = [0] * 2200
        self.Q = [0] * 2200
        self.BsRecord = [0] * 4400

    def Normalize(self, data):
        m = np.mean(data)
        mx = max(data)
        mn = min(data)
        return [(float(i) - m) / (mx - mn) for i in data]

    def updateI(self, strNewI):

        value_i = strNewI.split(",")

        temp_i = []

        for i in value_i:
            temp_i.append(float(i))

        temp_i = self.Normalize(temp_i)


        if self.curDataCountI == 20:
            self.I[0:2090] = self.I[110:2200]
            self.I[2090:2200] = temp_i

        else:

            for i in range(0, 110):
                self.I[self.curDataCountI * 110 + i] = float(temp_i[i])
            self.curDataCountI = self.curDataCountI + 1

        self.ui.updateI(self.I)

    def updateQ(self, strNewQ):
        value_q = strNewQ.split(",")

        temp_q = []

        for i in value_q:
            temp_q.append(float(i))

        temp_q = self.Normalize(temp_q)

        if self.curDataCountQ == 20:
            self.Q[0:2090] = self.Q[110:2200]
            self.Q[2090:2200] = temp_q

        else:

            for i in range(0, 110):
                self.Q[self.curDataCountQ * 110 + i] = float(temp_q[i])
            self.curDataCountQ = self.curDataCountQ + 1

        self.ui.updateQ(self.Q)

    def updateBsRecord(self, bsdata):

        value_1 = bsdata.split(",")

        floatBs = []

        for i in value_1:
            floatBs.append(float(i))

        self.BsRecord = self.Normalize(floatBs)

        # self.BsRecord[self.curDataCountBs * 4400:(self.curDataCountBs + 1) * 4400] = normalBs
        # self.curDataCountBs = self.curDataCountBs + 1
        # self.curDataCountBs = self.curDataCountBs % 2

        self.ui.updateBsRecord(self.BsRecord)
