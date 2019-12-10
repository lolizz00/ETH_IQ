from PyQt5 import QtCore, QtGui, QtWidgets

from plotform import Ui_Plot
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from scipy.interpolate import make_interp_spline, BSpline
import scipy.fftpack as fftpack
from scipy.fftpack import fft, fftfreq, fftshift
import numpy as np
from helpplot import Ui_Form as helpPlotUI

import pyqtgraph as pg

from myGridItem import myGridItem
from  myLegendItem import  myLegendItem

class PlotWid(QtWidgets.QWidget, Ui_Plot):

    stop_signal = pyqtSignal()

    def clear(self):
        self.plotter.plotItem.clear()
        self.delLegend()

    def delLegend(self):
        try:
            self.legend.scene().removeItem(self.legend)
        except Exception as e:
            pass

    def helpPushButtonClicked(self):
        self.helpui = helpPlotUI()
        self.wid = QWidget()
        self.helpui.setupUi(self.wid)
        self.wid.show()

    def __init__(self, parent=None):
        super(PlotWid, self).__init__(parent)
        self.preInitUi()
        self.initSignals()
        self.legend = None

    def resizeEvent(self, event):
        QtWidgets.QWidget.resizeEvent(self, event)

    def closeEvent(self, event):
        self.hide()
        self.stop_signal.emit()
        event.ignore()


    def preInitUi(self):
        self.setupUi(self)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.plotter)
        self.layout.addWidget(self.controlGroupBox)
        self.setLayout(self.layout)

    def initSignals(self):
        self.clearPushButton.clicked.connect(self.clear)
        self.helpPushButton.clicked.connect(self.helpPushButtonClicked)


    # запись сообщений в лог
    def log(self, msg):
        msg = 'PLotter :: ' + msg
        self.log_signal.emit(msg)

    # для matplolib, разметка и тд
    def initFigure(self):
        pass


    def plotOsc(self, X, Y, n, pen='8B0000', showLeg=False):
        if self.mode != 'osc':
            return

        self.plotter.plotItem.getViewBox().setBackgroundColor('w')
        p = myGridItem()
        p.setColor([0, 0, 0])
        self.plotter.addItem(p)



        leg = 'Канал #' + str(n)

        if showLeg:
            self.plotter.plotItem.legend = myLegendItem(None, offset=(30, 30))
            self.plotter.plotItem.legend.setParentItem(self.plotter.plotItem.vb)
            self.legend = self.plotter.plotItem.legend

        if self.showSample:
            self.plotter.plotItem.scatterPlot(X, Y, pen=pg.mkPen({'color': pen}), size=2)

        if self.showSpline:
            xnew = np.linspace(X.min(), X.max(), len(X) * 10)
            spl = make_interp_spline(X, Y, k=3)
            power_smooth = spl(xnew)
            self.plotter.plotItem.plot(xnew, power_smooth, pen=pg.mkPen({'color': pen}), name=leg)





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


        marker_size = 15
        pen = pg.mkPen({'color': '10162b'})
        self.plotter.plotItem.scatterPlot([sig_max_x], [sig_max_y], size=marker_size, symbol='d', name='Пик', pen=pen)

        self.plotter.plotItem.scatterPlot([noise_x], [noise_y], size=marker_size, symbol='+', name='Шум',pen=pen)

        sig_max_y = round(sig_max_y)
        noise_y = round(noise_y)


        txt = 'Канал # ' + str(chanN)+ '\n'
        txt = txt + 'Серднее значение сигнала: ' + str(sig_max_y) + ' dBFS\n'
        txt = txt + 'Серднее значение шума: ' + str(noise_y) + ' dBFS\n'
        txt = txt + 'SNR = ' + str(sig_max_y - noise_y) + ' dB'

        text = pg.TextItem(txt,color=pg.mkColor('000000'))
        self.plotter.plotItem.addItem(text)


    def find_nearest(self, array, value):
        array = np.asarray(array)
        t, = np.where(array == value)
        if len(t):
            return t[0]

        idx = (np.abs(array - value)).argmin()
        return idx

    def sumAmp(self, Amp, freq, Amp1, freq1):
        for i in range(len(Amp)):
            ind = self.find_nearest(freq1, freq[i]) # нашли под каким индексом частота, наиболее близкая к нашей
            Amp[i] = Amp[i] + Amp1[ind]
        return Amp

    def fixIQSize(self,data):

        min = 1e10
        for iterN in range(len(data)):
            ln = len(data[iterN].IQ)

            if ln < min:
                min = ln

        for iterN in range(len(data)):
            data[iterN].IQ = data[iterN].IQ[:min]

        return data

    # отстройка спектограмы
    def plotSpec(self, data, n, pen='8B0000', showLeg=False):

        #self.plotter.plotItem.updateGrid()

        self.plotter.plotItem.getViewBox().setBackgroundColor('w')

        Amp =   None
        freq = None
        iterCnt = len(data)

        data = self.fixIQSize(data)

        for iterN in range(iterCnt):
            IQ = data[iterN].IQ
            ln = len(IQ)

            T = 1 / self.fs
            IQ = fft(IQ)
            IQ = fftshift(IQ)

            win = np.hamming(ln)

            IQ = np.abs(IQ) * 2 / np.sum(win)
            ref = 32769
            X = 20 * np.log10(IQ / ref)

            _freq = fftfreq(ln, T)
            _freq = fftshift(_freq)

            if iterN == 0:
                freq = _freq
                Amp = X
            else:
                Amp = Amp + X
                #Amp = self.sumAmp(Amp, freq, X, _freq)


        Amp = Amp / iterCnt

        if iterN == 0:
            legend = 'Канал #' + str(n)
        else:
            legend = 'Канал #' + str(n) + ', Количество итераций: ' +  str(iterN + 1)


        if showLeg:
            self.plotter.plotItem.legend = myLegendItem(None, offset=(30, 30))
            self.plotter.plotItem.legend.setParentItem(self.plotter.plotItem.vb)
            self.legend = self.plotter.plotItem.legend


        self.plotter.plotItem.plot(freq, Amp, pen=pg.mkPen({'color': pen}), name=legend)


        p = myGridItem()
        p.setColor([0,0,0])
        self.plotter.addItem(p)



        if self.snr and n == self.snrChan:
            self.plotSNR(Amp, freq, n)


        self.plotter.plotItem.setLabel('left',   'Power, dBFS')
        self.plotter.plotItem.setLabel('bottom', 'Frequency, Hz')


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

    # смена режима графиков
    def switchMode(self):
        pass