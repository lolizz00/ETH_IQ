from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy.interpolate import make_interp_spline, BSpline
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import *
from PyQt5.QtWidgets import *
from mpl_toolkits.mplot3d import *
from PyQt5.QtCore import *

class Plotter(QtWidgets.QWidget):

    log_signal = pyqtSignal(str)


    def initFigure(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.figure.canvas.draw()

    def __init__(self, parent=None):
        super(Plotter, self).__init__(parent)
        self.initFigure()

    def clear(self):
        return
        plt.clf()

    def log(self, msg):
        return
        msg = 'Plotter :: ' + msg
        self.log_signal.emit(msg)

    def run(self):
       return
       self.show()

    def show(self):
        return
        plt.show()

    def plotSpec(self, X, n):
        return
        self.log('Строим спектограмму...')
        plt.figure('Канал #' + str(n) + ' - спектограмма')
        win = signal.get_window((self.fftWin, self.k), len(X))
        plt.magnitude_spectrum(X, Fs=self.fs, scale='dB', window=win)
        plt.grid(True)

        self.log('Спектограмма успешно построена...')

    def plotIQ(self,X, I, Q, n ):
        return
        leg = 'Канал #' + str(n) + ' - осцилограмма'

        if self.showSpline:
            xnew = np.linspace(X.min(), X.max(), len(X) * 10)
            splI = make_interp_spline(X, I, k=3)
            splQ = make_interp_spline(X, Q, k=3)

            power_smoothI = splI(xnew)
            power_smoothQ = splQ(xnew)

        if self.scopeOsc:
            # --- I
            if self.showSpline:
                self.oscPlotI.plot(xnew, power_smoothI, label='Канал #' + str(n) + ' - график I')

            if self.showSample:
                self.oscPlotI.scatter(X, I,  s=10, label='Канал #' + str(n) + ' - сeмплы I')

            self.oscPlotI.set_xlim(0, 500)
            self.oscPlotI.set_ylim(-1200, 1200)
            self.oscPlotI.grid(True)
            self.oscPlotI.legend()

            # --- Q

            if self.showSpline:
                self.oscPlotQ.plot(xnew, power_smoothQ, label='Канал #' + str(n) + ' - график Q')

            if self.showSample:
                self.oscPlotQ.scatter(X, Q,  s=10, label='Канал #' + str(n) + ' - сeмплы Q')

            plt.xlim(0, 500)
            plt.ylim(-1200, 1200)
            plt.grid(True)
            plt.legend()

        else:
            # --- I
            plt.figure(leg + ' I')

            if self.showSpline:
                self.oscPlotQ(xnew, power_smoothI, label='Канал #' + str(n) + ' - график I')

            if self.showSample:
                self.oscPlotQ(X, I, color='r', s=10, label='Канал #' + str(n) + ' - сeмплы I')

            plt.xlim(0, 500)
            plt.ylim(-1200, 1200)
            plt.grid(True)
            plt.legend()

            # --- Q
            plt.figure(leg + ' Q')
            if self.showSpline:
                plt.plot(xnew, power_smoothQ, label='Канал #' + str(n) + ' - график Q')

            if self.showSample:
                plt.scatter(X, Q, color='r', s=10, label='Канал #' + str(n) + ' - сeмплы Q')

            plt.xlim(0, 500)
            plt.ylim(-1200, 1200)
            plt.grid(True)
            plt.legend()



    def plotOsc(self, X, Y, n):
        return
        self.log('Строим осцилорамму...')
        if self.showSpline:
            xnew = np.linspace(X.min(), X.max(), len(X) * 10)
            spl = make_interp_spline(X, Y, k=3)
            power_smooth = spl(xnew)

        leg = 'Канал #' + str(n)  + ' - осцилограмма'

        if self.scopeOsc:
            if self.showSample:
                self.oscPlot.scatter(X, Y, s=10,  label='Канал #' + str(n) + ' - сeмплы' )

            if self.showSpline:
                self.oscPlot.plot(xnew, power_smooth,label='Канал #' + str(n) + ' - график')
        else:
            plt.figure(leg)

            if self.showSpline:
                self.plot.plot(xnew, power_smooth, label='Канал #' + str(n) + ' - график')
            if self.showSample:
                self.plot.scatter(X, Y, color='r', s=10, label='Канал #' + str(n) + ' - сeмплы')

        self.log('Осцилорамма успешно построена...')
        plt.xlim(0, 2048)
        plt.ylim(min(Y) - 500, max(Y) + 500)
        plt.grid(True)
        plt.legend()



    def switchMode(self):
        if self.mode == 'osc':
            pass
        elif self.mode == 'iq':
            pass
        elif self.mode == 'spec':
            pass

    def createOscFigure(self):
        return
        if self.splitIQ:
            self.oscFigI = plt.figure('Осцилограмма I')
            self.oscFigQ = plt.figure('Осцилограмма Q')

            self.oscPlotI = self.oscFigI.subplots(1)
            self.oscPlotQ = self.oscFigQ.subplots(1)
        else:
            self.oscFig = plt.figure('Осцилограммы')
            self.oscPlot = self.oscFig.subplots(1)

    def setParams(self, lst):
        self.mode = lst['mode']
        self.showSample = lst['showSample']
        self.showSpline = lst['showSpline']

        self.switchMode()


