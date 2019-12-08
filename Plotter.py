from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from scipy.interpolate import make_interp_spline, BSpline
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


import math
# остройка графиков


# оставляем только нужные кнопки
class MyNavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Pan', 'Zoom', 'Save')]

class Plotter(QtWidgets.QWidget):

    log_signal = pyqtSignal(str)

    maxOscVal = 0
    K_X = 100
    K_Y = 1000

    maxOscValI = 0
    maxOscValQ = 0
    oscSize = 100

    XLIM_min = 0
    XLIM_max = oscSize

    YLIM_min = -K_Y
    YLIM_max = K_Y

    windows_need_k = ['gaussian', 'kaiser']

    def clear(self):
        pass

    # запись сообщений в лог
    def log(self, msg):
        msg = 'PLotter :: ' + msg
        self.log_signal.emit(msg)

    def __init__(self, parent=None):
        super(Plotter, self).__init__(parent)
        self.initFigure()
        self.initPlots()

    # создаем нужные типы графиков
    def initPlots(self):
        self.oscPlot = None
        self.oscPlotI = None
        self.oscPlotQ = None
        self.specPlot = None

    # для matplolib, разметка и тд
    def initFigure(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = MyNavigationToolbar(self.canvas, self)


        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        self.setLayout(layout)
        self.figure.canvas.draw()

    def plotOsc(self, X, Y, n):

        if self.mode != 'osc':
            return

        leg = 'Канал #' + str(n) + ' - осцилограмма'

        if self.showSample:
            self.oscPlot.scatter(X, Y, s=10, label='Канал #' + str(n) + ' - сeмплы', alpha=.5)

        if self.showSpline:
            xnew = np.linspace(X.min(), X.max(), len(X) * 10)
            spl = make_interp_spline(X, Y, k=3)
            power_smooth = spl(xnew)
            self.oscPlot.plot(xnew, power_smooth, label='Канал #' + str(n) + ' - график', alpha=.5)

        # легенда справа сверху
        plt.legend(loc='upper right')
        plt.grid(True)

        # масштабируем
        tmp = Y.max()
        if tmp > self.maxOscVal:
            self.maxOscVal = tmp

        #plt.ylim(-self.maxOscVal - self.K_Y, self.maxOscVal + self.K_Y)


        self.YLIM_min = -self.maxOscVal - self.K_Y
        self.YLIM_max = self.maxOscVal + self.K_Y

        plt.xlim(0, self.oscSize)

        self.figure.canvas.draw()

    def safe_ln(self, x, minval=0.0000000001):
        return np.log10(x.clip(min=minval))

    def moving_average(self, a, n=3):
        ret = np.cumsum(a, dtype=float)
        ret[n:] = ret[n:] - ret[:-n]
        return ret[n - 1:] / n


    def plotSNR(self, s_dbfs, freq, chanN):

        # ищем сигнал
        sig_max_y = np.max(s_dbfs)
        sig_max_x = freq[np.argmax(s_dbfs)]
        sig_max_y

        # ищем шум
        noise_x = sig_max_x + self.offs  # нашли частоту

        noise_x = np.abs(freq - noise_x)
        noise_x = np.argmin(noise_x)  # нашли индекс частоты, которая ближе всего к нужной частоте

        noise_y = s_dbfs[noise_x]
        noise_x = freq[noise_x]

        # легенду пишем только один раз
        marker_size = 50
        self.specPlot.scatter([sig_max_x], [sig_max_y], label='Пик сигнала', marker='x', color='black',
                                  s=marker_size)
        self.specPlot.scatter([noise_x], [noise_y], label='Шум по смещению', marker='+', color='black',
                                  s=marker_size)

        sig_max_y = round(sig_max_y)
        noise_y = round(noise_y)

        txt = 'Канал # ' + str(chanN)+ '\n'
        txt = txt + 'Серднее значение сигнала: ' + str(sig_max_y) + ' dBFS\n'
        txt = txt + 'Серднее значение шума: ' + str(noise_y) + ' dBFS\n'
        txt = txt + 'SNR = ' + str(sig_max_y - noise_y) + ' dB'

        box = {'facecolor': 'white', 'edgecolor': 'red', 'boxstyle': 'square'}

        plt.text(0, sig_max_y - 10, txt,
                 horizontalalignment='center',
                 verticalalignment='center',
                 bbox=box)

    # отстройка спектограмы
    def plotSpec(self, data, n):


        Amp =   None
        freq = None
        iterCnt = len(data)
        flg = True

        for iterN in range(iterCnt):
            X = data[iterN].A

            N = len(X)
            win = np.hamming(N)
            fs = self.fs * 2
            sp = np.fft.rfft(X)
            s_mag = np.abs(sp) * 2 / np.sum(win)

            ref = 32769
            s_dbfs = 20 * np.log10(s_mag / ref)


            # отображаем только часть спектра
            s_dbfs = s_dbfs[:int(len(s_dbfs) / 2)]

            if flg:
                Amp = np.zeros_like(s_dbfs)
                freq = np.arange((N / 2) + 1) / (float(N) / fs)
                freq = freq[:int(len(freq) / 2)]
                flg = False

            if len (s_dbfs) > len(Amp):
                s_dbfs =  s_dbfs[0:len(Amp)]
            elif len(Amp) > len(s_dbfs):
                Amp = Amp[0:len(s_dbfs)]

            Amp = Amp + s_dbfs

        Amp = Amp / iterCnt

        if iterN == 0:
            legend = 'Канал #' + str(n)
        else:
            legend = 'Канал #' + str(n) + ', Количество итераций: ' +  str(iterN + 1)


        if len(freq) > len(Amp):
            freq = freq[0:len(Amp)]
        elif len(Amp) > len(freq):
            Amp = Amp[0:len(freq)]

        self.specPlot.plot(freq, Amp, label=legend, alpha=.5)


        if self.snr and n == self.snrChan:
            self.plotSNR(Amp, freq, n)

        # легенда
        plt.xlabel('Частота, Гц')
        plt.ylabel('Амплитуда, dBFS')
        plt.legend(loc='upper right')
        plt.grid(True)

        self.figure.canvas.draw()

    # установка параметров, сохраняем себе
    def setParams(self, lst):
        self.mode = lst['mode']
        self.showSample = lst['showSample']
        self.showSpline = lst['showSpline']
        self.fs = lst['fs']


        self.snr = lst['snr']
        self.snrChan = lst['snrChan']
        self.offs = lst['offs']



        maxOscVal = 0

        self.switchMode()

    # очистка графиковы
    def clearPlots(self):
        if self.oscPlot:
            self.figure.delaxes(self.oscPlot)
            self.oscPlot = None

        if self.oscPlotI:
            self.figure.delaxes(self.oscPlotI)
            self.oscPlotI = None

        if self.oscPlotQ:
            self.figure.delaxes(self.oscPlotQ)
            self.oscPlotQ = None

        if self.specPlot:
            self.figure.delaxes(self.specPlot)
            self.specPlot = None
        self.figure.canvas.draw()

    # смена режима графиков
    def switchMode(self):

        self.clearPlots()

        if self.mode == 'osc':
            self.oscPlot = self.figure.subplots(1)
            self.oscPlot.set_title('Осцилограмма')
        elif self.mode == 'iq':
            self.oscPlotI, self.oscPlotQ =  self.figure.subplots(2)
            self.oscPlotI.set_title('Осцилограмма I')
            self.oscPlotQ.set_title('Осцилограмма Q')
        elif self.mode == 'spec' or self.mode == 'snr':
            self.specPlot = self.figure.subplots(1)
            self.specPlot.set_title('Спектограмма')



        self.figure.canvas.draw()