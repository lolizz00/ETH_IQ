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