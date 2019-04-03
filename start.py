from DataReader import DataReader
from DataReader import DataReaderMin
import matplotlib.pyplot as plt
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy.interpolate import make_interp_spline, BSpline
from scipy import signal
import numpy as np
import sys
from MainWindow import MW
from PyQt5 import QtWidgets


# --- Нормальный вывод ошибок
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))


    print('\n\n-------------------------------------------- \n')
    print(text)
    print('\n----------------------------------------------\n')


import sys
sys.excepthook = log_uncaught_exceptions

# ---

def plotSpec(X):
    f_s = 8000
    plt.figure()
    win = signal.get_window(('gaussian', 2000), len(X))
    plt.magnitude_spectrum(X, Fs=f_s, scale='dB', window=win)
    plt.grid(True)

def plotOsc(X, Y):
    f_s = 8000

    X = np.array(X)
    Y = np.array(Y)

    xnew = np.linspace(X.min(), X.max(), len(X) * 10)
    spl = make_interp_spline(X, Y, k=3)
    power_smooth = spl(xnew)

    plt.figure()
    #plt.plot(xnew,power_smooth)
    plt.scatter(X, Y, s=10)
    #plt.xlim(0, 500)
    #plt.ylim(-1200, 1200)
    plt.grid(True)




def start():
    app = QtWidgets.QApplication(sys.argv)
    mv = MW()
    mv.show()
    sys.exit(app.exec_())


def _start():
    datareader = DataReader()
    datareader.setChanN(2)

    chans = [0]

    datareader.initReader(chans, 10000)
    datareader.start()

    sch = 0
    for data in datareader.data:
        print('Строим график №' + str(sch))
        plotSpec(data.A)
        plotOsc(data.X, data.A)
        sch = sch + 1


    plt.show()
if __name__ == '__main__':
    start()