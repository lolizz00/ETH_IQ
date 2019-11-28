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

    def plus(self):
        if self.mode == 'osc' or self.mode == 'iq':

            if self.YLIM_max < self.XLIM_min:
                return

            self.YLIM_min = self.YLIM_min + self.K_Y
            self.YLIM_max = self.YLIM_max - self.K_Y



            if self.mode == 'iq':
                self.oscPlotQ.set_ylim(self.YLIM_min, self.YLIM_max)
                self.oscPlotI.set_ylim(self.YLIM_min, self.YLIM_max)
            else:
                plt.ylim(self.YLIM_min, self.YLIM_max)

            self.figure.canvas.draw()

    def minus(self):
        if self.mode == 'osc' or self.mode == 'iq':
            self.YLIM_min = self.YLIM_min - self.K_Y
            self.YLIM_max = self.YLIM_max + self.K_Y

            if self.mode == 'iq':
                self.oscPlotQ.set_ylim(self.YLIM_min, self.YLIM_max)
                self.oscPlotI.set_ylim(self.YLIM_min, self.YLIM_max)
            else:
                plt.ylim(self.YLIM_min, self.YLIM_max)


            self.figure.canvas.draw()

    def moveLeft(self):
        if self.mode == 'osc' or self.mode == 'iq':
            self.XLIM_min = self.XLIM_min - self.K_X
            self.XLIM_max = self.XLIM_max - self.K_X

            if self.mode == 'iq':
                passs
                self.oscPlotQ.set_xlim(self.XLIM_min, self.XLIM_max)
                self.oscPlotI.set_xlim(self.XLIM_min, self.XLIM_max)
            else:
                plt.xlim(self.XLIM_min, self.XLIM_max)

            self.figure.canvas.draw()

    def moveRight(self):
        if self.mode == 'osc' or self.mode == 'iq':
            self.XLIM_min = self.XLIM_min + self.K_X
            self.XLIM_max = self.XLIM_max + self.K_X

            if self.mode == 'iq':
                self.oscPlotQ.set_xlim(self.XLIM_min, self.XLIM_max)
                self.oscPlotI.set_xlim(self.XLIM_min, self.XLIM_max)
            else:
                plt.xlim(self.XLIM_min, self.XLIM_max)

            self.figure.canvas.draw()

    # отстройка отдельно I и Q
    def plotIQ(self, X, I, Q, n):


        # --- I
        leg = 'Канал #' + str(n) + ' - осцилограмма I'

        if self.showSample: # если отображаем точки, s - рамер точки
            self.oscPlotI.scatter(X, I, s=10, label='Канал #' + str(n) + ' - сeмплы I')

        if self.showSpline: # если отображаем графки
            # магия построения графиков из scipy
            xnew = np.linspace(X.min(), X.max(), len(X) * 10)
            spl = make_interp_spline(X, I, k=3)
            power_smooth = spl(xnew)
            self.oscPlotI.plot(xnew, power_smooth, label='Канал #' + str(n) + ' - график I')


        # легенда справа сверху
        self.oscPlotI.legend(loc='upper right')
        self.oscPlotI.grid(True)


        # масштабируем
        tmp = I.max()
        if tmp > self.maxOscValI:
            self.maxOscValI = tmp

        self.YLIM_min = -self.maxOscValI - self.K_Y
        self.YLIM_max = self.maxOscValI + self.K_Y

        self.oscPlotI.set_xlim(0, self.oscSize)

        self.figure.canvas.draw()

        # --- Q
        if self.showSample: # отображаем точки, s - размер точки
            self.oscPlotQ.scatter(X, Q, s=10, label='Канал #' + str(n) + ' - сeмплы Q')

        if self.showSpline: # график
            # магия scipy
            xnew = np.linspace(X.min(), X.max(), len(X) * 10)
            spl = make_interp_spline(X, Q, k=3)
            power_smooth = spl(xnew)
            self.oscPlotQ.plot(xnew, power_smooth, label='Канал #' + str(n) + ' - график Q')


        self.oscPlotQ.legend(loc='upper right')
        self.oscPlotQ.grid(True)
        plt.grid(True)

        tmp = Q.max()
        if tmp > self.maxOscValQ:
            self.maxOscValQ = tmp

        #self.oscPlotQ.set_ylim(-self.maxOscValQ - self.K_Y, self.maxOscValQ + self.K_Y)

        self.YLIM_min = -self.maxOscValQ - self.K_Y
        self.YLIM_max = self.maxOscValQ + self.K_Y

        self.oscPlotQ.set_xlim(0, self.oscSize)

        self.figure.canvas.draw()

    def plotOsc(self, X, Y, n):

        if self.mode != 'osc':
            return

        leg = 'Канал #' + str(n) + ' - осцилограмма'

        if self.showSample:
            self.oscPlot.scatter(X, Y, s=10, label='Канал #' + str(n) + ' - сeмплы')

        if self.showSpline:
            xnew = np.linspace(X.min(), X.max(), len(X) * 10)
            spl = make_interp_spline(X, Y, k=3)
            power_smooth = spl(xnew)
            self.oscPlot.plot(xnew, power_smooth, label='Канал #' + str(n) + ' - график')

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

    # остройка спектограммы
    def specWithSNR(self, Xarr):

        sch = 0

        sig_max = []
        noise = []

        for X in Xarr:
            sch = sch + 1
            N = len(X)
            win = np.hamming(N)
            fs = self.fs * 2
            sp = np.fft.rfft(X)
            freq = np.arange((N / 2) + 1) / (float(N) / fs)
            s_mag = np.abs(sp) * 2 / np.sum(win)

            ref = 32769
            s_dbfs = 20 * np.log10(s_mag / ref)

            # фильтер, гы
            for i in range(int(len(s_dbfs) /2 ), len(s_dbfs)):
                if s_dbfs[i] > -60:
                    pass
                    s_dbfs[i] = s_dbfs[i-1]

            self.specPlot.plot(freq, s_dbfs, label='Считывание #' + str(sch), alpha=.5)

            # ищем сигнал
            sig_max_y = np.max(s_dbfs)
            sig_max_x = freq[np.argmax(s_dbfs)]
            sig_max.append(sig_max_y)

            # ищем шум
            noise_x = sig_max_x + self.offs # нашли частоту

            noise_x = np.abs(freq - noise_x)
            noise_x = np.argmin(noise_x) # нашли индекс частоты, которая ближе всего к нужной частоте

            noise_y = s_dbfs[noise_x]
            noise_x = freq[noise_x]

            noise.append(noise_y)

            # легенду пишем только один раз
            marker_size = 50
            if sch == 1:
                self.specPlot.scatter([sig_max_x], [sig_max_y], label='Пик сигнала', marker='x', color='black',s=marker_size)
                self.specPlot.scatter([noise_x], [noise_y], label='Шум по смещению', marker='+', color='black',s=marker_size)
            else:
                self.specPlot.scatter([sig_max_x], [sig_max_y], marker='x', color='black', s=marker_size)
                self.specPlot.scatter([noise_x], [noise_y], marker='+', color='black', s=marker_size)

        sig_mid  = np.sum(sig_max) / len(sig_max)
        sig_mid = math.floor(sig_mid)
        noise_mid = np.sum(noise) / len(noise)
        noise_mid = math.floor(noise_mid)

        txt = 'Серднее значение сигнала: ' + str(sig_mid) + ' dBFS\n'
        txt = txt + 'Серднее значение шума: ' + str(noise_mid) + ' dBFS\n'
        txt = txt + 'SNR = ' + str(sig_mid - noise_mid) + ' dB'


        box = {'facecolor' : 'white', 'edgecolor' : 'red', 'boxstyle' : 'square'}

        plt.text(0.5, 0.5, txt,
             horizontalalignment='center',
             verticalalignment='center',
                 bbox=box)




        plt.xlabel('Частота, Hz')
        plt.ylabel('Сигнал, dBFS')
        plt.legend(loc='upper right')
        plt.grid(True)
        self.figure.canvas.draw()

    # отстройка спектограмы
    def plotSpec(self, X, n):



        #X = 20 * self.safe_ln(np.abs(X) / 32768)

        #self.specPlot.magnitude_spectrum(X, Fs=2 * self.fs, scale='dB', window=win, label='Канал #' + str(n), alpha=.5)
        #self.specPlot.magnitude_spectrum(X, Fs=2 * self.fs,  window=win, label='Канал #' + str(n), alpha=.5)



        N = len(X)
        win = np.hamming(N)
        fs = self.fs * 2
        sp = np.fft.rfft(X)
        freq = np.arange((N / 2) + 1) / (float(N) / fs)
        s_mag = np.abs(sp) * 2 / np.sum(win)

        ref = 32769
        s_dbfs = 20 * np.log10(s_mag / ref)

        # фильтер, гы
        for i in range(int(len(s_dbfs) / 2), len(s_dbfs)):
            if s_dbfs[i] > -60:
                pass
                s_dbfs[i] = s_dbfs[i - 1]

        self.specPlot.plot(freq, s_dbfs,label='Канал #' + str(n), alpha=.5)

        #plt.plot(s_dbfs)

        #N = 10
        #point_sig = [np.argmax(s_dbfs), np.max(s_dbfs)]
        #point_noise = [point_sig[0] + N, s_dbfs[point_sig[0] + N]]

        #plt.scatter(point_sig[0], point_sig[1],  color='black', marker='x')


        #plt.scatter(point_noise[0], point_noise[1], color='black', marker='x')

       # print(sig_level)
       # print(noise_level)

        #s_dbfs = self.moving_average(s_dbfs, 5)
        #plt.plot(s_dbfs, color='red')





        # легенда
        plt.xlabel('Частота')
        plt.ylabel('dBFS')
        plt.legend(loc='upper right')
        plt.grid(True)

        self.figure.canvas.draw()

    # установка параметров, сохраняем себе
    def setParams(self, lst):
        self.mode = lst['mode']
        self.showSample = lst['showSample']
        self.showSpline = lst['showSpline']
        self.fs = lst['fs']
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