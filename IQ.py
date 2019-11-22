import numpy as np


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

    # генерация амплитуды
    def generateA(self):
        self.A = np.add(self.I, self.Q)
        self.A = self.A