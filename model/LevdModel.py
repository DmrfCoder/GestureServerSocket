import numpy as np
import scipy.signal
import matplotlib.pyplot as plt


def Levd(II):
    Thr = 1e14
    EPks = []
    ELoc = []
    EV = 0

    ILocs1 = scipy.signal.find_peaks(II)
    ILocs2 = scipy.signal.find_peaks(-II)
    IFLoc = np.hstack((ILocs1, ILocs2))

    IPks2 = -IPks2
    IFLoc = np.unique((IFLoc))

    IFPks = II(IFLoc)
    IFV = []
    if (ILocs1(1) < ILocs2(1)): \
            IFV = [-1, 1]

    else:
        IFV = [1, -1]

    n = 1;
    # -------findfirst - ------------
    for i in range(2, len(IFPks)):
        if (abs(IFPks(i - 1) - IFPks(i)) > Thr):
            EPks[n] = IFPks(i - 1)
            ELoc[n] = IFLoc(i - 1)
            n = n + 1
            EPks[n] = IFPks(i)
            ELoc[n] = IFLoc(i)
            EV = IFV(np.mod(i, 2) + 1)
            break

    for i in range(len(IFPks)):

        if (IFV(np.mod(i, 2) + 1) == EV):
            if (IFV(np.mod(i, 2) + 1) == 1 & & IFPks(i) > EPks(n)):
                EPks(n) = IFPks(i)
                ELoc(n) = IFLoc(i)
            elif (IFV(np.mod(i, 2) + 1) == -1 & & IFPks(i) < EPks(n)):
                EPks(n) = IFPks(i)
                ELoc(n) = IFLoc(i)

        elif (abs(EPks(n) - IFPks(i)) > Thr):

            n = n + 1
            EPks(n) = IFPks(i)
            ELoc(n) = IFLoc(i)
            EV = IFV(mod(i, 2) + 1)

    SI = np.zeros(len(II), 1)
    SI[1] = (II[1] + EPks[1]) / 2
    for i in range(2, ELoc(1)):
        SI[i] = 0.95 * SI[i - 1] + 0.05 * (II[1] + EPks[1]) / 2

    n = 1
    for i in range(ELoc(1) + 1, len(II)):
        SI[i] = 0.95 * SI[i - 1] + 0.05 * (EPks[n] + EPks[min(n + 1, len(EPks)])) / 2

        if (n + 1 < len(ELoc) and i > ELoc[n + 1]):
            n = n + 1;

    DyN = II - SI
