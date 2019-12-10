import numpy as np
from scipy import signal
from scipy import fftpack
from scipy.signal import butter, lfilter
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import scipy.fftpack as fftpack



# Для удобства хранения отсчетов
class IQ:

    LIMIT = None # максимальное количество хранимых точек

    def __init__(self):
        self.Q = np.array([]) # отсчеты I
        self.I = np.array([]) # отсчеты Q

        self.A = np.array([]) # Вычисляемая амплитуда
        self.X = np.array([]) # Генерируемые номер отсчетов для графика


    # сохраняем новые отсчеты
    def addIQ(self, _I, _Q=None):

        self.I = np.append(self.I, _I)

        # если прищли только I, добиваем Q нулями
        if not _Q:
            self.Q = np.append(self.Q, np.zeros_like(_I))
        else:
            self.Q = np.append(self.Q, _Q)


    def remA(self, lim):
        if lim > len(self.A):
            return

        self.A = self.A[:lim]
        self.X = self.X[:lim]
        self.IQ = self.IQ[:lim]



    # удаление 'лишних' данные для возвращения в лимит
    def rem(self, lim):

        return

        if lim > len(self.I):
            return

        self.X = self.X[:lim]
        self.I = self.I[:lim]

        if len(self.Q) > 0:
            self.Q = self.Q[:lim]

    # генерация номеров отсчетов
    def genreateX(self):
        self.X = np.arange(0, len(self.A))

    #def filter(self):

    def upsample(self, X):
        ind = np.arange(1, len(X), 1)
        X = np.insert(X, ind, 0)
        return X

    def LPF(self, X, fs):
        w = (fs / 2) / (fs)
        b, a = signal.butter(5, w, 'low')
        X = signal.filtfilt(b, a, X)
        return X


        # генерация амплитуды
    def generateA(self, Fs):

        I = self.I
        Q = self.Q

        IQ = I + 1j * Q
        self.IQ = IQ

        IQ = self.upsample(IQ)

        IQ = IQ * np.exp(1j * 2 * np.pi * Fs / 4)



        IQ = np.real(IQ)

        # срезаем после 2500 для осцилограммы
        IQ = self.LPF(IQ, Fs)

        #self.A = IQ
        self.A = IQ[20:]

