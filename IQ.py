import numpy as np



class IQ:

    LIMIT = None

    def __init__(self):
        self.Q = np.array([])
        self.I = np.array([])

        self.A = np.array([])
        self.X = np.array([])

    def addIQ(self, _I, _Q=None):

        self.I = np.append(self.I, _I)
        if not _Q:
            self.Q = np.append(self.Q, np.zeros_like(_I))
        else:
            self.Q = np.append(self.Q, _Q)

    def rem(self, lim):
        if lim > len(self.I):
            return


        self.A = self.A[:lim]
        self.X = self.X[:lim]
        self.I = self.I[:lim]
        if len(self.Q) > 0:
            self.Q = self.Q[:lim]

    def genreateX(self):
        self.X = np.arange(0, len(self.A))

    def generateA(self):
        self.A = np.add(self.I, self.Q)
        self.A = self.A