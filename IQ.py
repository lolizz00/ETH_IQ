import numpy as np
from scipy import signal
from scipy import fftpack
from scipy.signal import butter, lfilter
from scipy.signal import butter, lfilter, freqz

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


    # удаление 'лишних' данные для возвращения в лимит
    def rem(self, lim):

        if lim > len(self.I):
            return


        self.A = self.A[:lim]
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

    def butter_lowpass(self, cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_lowpass(cutoff, fs, order=order)
        y = lfilter(b, a, data)
        return y

    # генерация амплитуды
    def generateA(self, Fs):

        I = self.I
        Q = self.Q

        #Fs = 5e3


        IQ = I + 1j* Q

        IQ = self.upsample(IQ)



        IQ = IQ * np.exp(1j * 2 * np.pi * Fs / 4)

        IQ = np.real(IQ)


        self.A = IQ


        pass
        #self.A = np.add(self.I, self.Q)
        #self.A = self.A

