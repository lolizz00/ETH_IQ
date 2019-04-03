from PyQt5 import QtCore, QtGui, QtWidgets
from mw import Ui_MainWindow

from DataReader import DataReader
from Plotter import Plotter
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *

from PlotWidget import PlotWidget

import numpy as np

class MW(QtWidgets.QMainWindow, Ui_MainWindow):

    def selectFilePushButtonClicked(self):
        self.filePathLineEdit.setText(QFileDialog.getOpenFileName()[0])

    def startUpdate(self):
        self.stopPushButton.setEnabled(True)
        self.startPushButton.setEnabled(False)

        tout = float(self.updateLineEdit.text())
        tout = 1000 * tout
        tout = int(tout)

        self.timer.timeout.connect(self.start)
        self.timer.setInterval(tout)
        self.timer.start()

        self.start()

    def stopUpdate(self):
        self.stopPushButton.setEnabled(False)
        self.startPushButton.setEnabled(True)
        self.timer.stop()

        #self.plotwidget.hide()


    def __init__(self):
        super(MW, self).__init__()
        self.preInitUi()
        self.connectSignals()
        self.initClass()

    def showErr(self, text):
        QtWidgets.QMessageBox.critical(self, 'Ошибка!', text)


    def _switchCnannels(self):
        channels = []

        if self.chan1checkBox.isChecked():
            channels.append(0)
        if self.chan2checkBox.isChecked():
            channels.append(1)
        if self.chan3checkBox.isChecked():
            channels.append(2)
        if self.chan4checkBox.isChecked():
            channels.append(3)
        if self.chan5checkBox.isChecked():
            channels.append(4)
        if self.chan6checkBox.isChecked():
            channels.append(5)
        if self.chan7checkBox.isChecked():
            channels.append(6)
        if self.chan8checkBox.isChecked():
            channels.append(7)

        return channels

    def updateReaderParams(self):
        try:

            if not self.specModeRadioButton.isChecked():
                channels = self._switchCnannels()
                if not len(channels):
                    raise
            else:
                channels = [int(self.specChanComboBox.currentText()) - 1]

            pointCnt = self.pointCntSpinBox.value()

            chanN = int(self.chanComboBox.currentText())

            # ---

            self.datareader.setChanN(chanN)
            self.datareader.initReader(channels, pointCnt)

        except:
            raise
            self.showErr('Неверные параметры!')

    def updatePlotParams(self):
        try:
            lst = {}

            if self.oscModeRadioButton.isChecked():
                lst['mode'] = 'osc'
            elif self.iqModeRadioButton.isChecked():
                lst['mode'] = 'iq'
            elif self.specModeRadioButton.isChecked():
                lst['mode'] = 'spec'


            lst['showSample'] = self.showSampleCheckBox.isChecked()
            lst['showSpline'] = self.showSplineCheckBox.isChecked()
            lst['fftWin'] = self.fftWinComboBox.currentText()
            lst['k'] = float(self.fftKLineEdit.text())
            lst['fs'] = int(self.fsLineEdit.text())


            self.plotwidget.plotter.setParams(lst)

        except:
            self.showErr('Неверные параметры!')
            return False

        return True

    def initClass(self):
        self.datareader = DataReader()
        self.datareader.log_signal.connect(self.writeLog)



        self.plotwidget = PlotWidget()
        self.plotwidget.plotter.log_signal.connect(self.writeLog)


        self.timer = QTimer()

    def preInitUi(self):
        self.setupUi(self)
        self.setCentralWidget(self.cw)


    def writeLog(self, msg):
        old_text = self.logTextEdit.toPlainText()

        if old_text == '':
            self.logTextEdit.setText(msg)
        else:
            self.logTextEdit.setText(old_text + '\n' + msg)

    def start(self):

        if not self.updatePlotParams():
            return


        self.plotwidget.show()

        self.updateReaderParams()
        self.datareader.run()

        sch = 0
        for data in self.datareader.data:
            n = self.datareader.THREAD_N[sch] + 1
            sch = sch + 1

            if self.oscModeRadioButton.isChecked():
                self.plotwidget.plotter.plotOsc(data.X, data.A, n)

            if self.iqModeRadioButton.isChecked():
                self.plotwidget.plotter.plotIQ(data.X, data.I, data.Q, n)

            if self.specModeRadioButton.isChecked():
                self.plotwidget.plotter.plotSpec(data.A, n)


    def stopPushButtonClicked(self):
        self.stopUpdate()

    def startPushButtonClicked(self):

        if self.modeToolBox.currentWidget() == self.realPage:
            if self.updateCheckBox.isChecked():
                self.startUpdate()
            else:
                self.start()
        else:

            if not self.updatePlotParams():
                return



            chanN = int(self.chanComboBox.currentText())
            self.datareader.setChanN(chanN)
            self.datareader.readFile(self.filePathLineEdit.text())
            self.plotwidget.show()

            data = self.datareader.data[0]

            if self.oscModeRadioButton.isChecked():
                self.plotwidget.plotter.plotOsc(data.X, data.A, 0)

            if self.iqModeRadioButton.isChecked():
                   self.plotwidget.plotter.plotIQ(data.X, data.I, data.Q, 0)

            if self.specModeRadioButton.isChecked():
                self.plotwidget.plotter.plotSpec(data.A, 0)

    def clearLogPushButtonClicked(self):
        self.logTextEdit.setText('')

    def connectSignals(self):
        self.startPushButton.clicked.connect(self.startPushButtonClicked)
        self.clearLogPushButton.clicked.connect(self.clearLogPushButtonClicked)
        self.stopPushButton.clicked.connect(self.stopPushButtonClicked)
        self.selectFilePushButton.clicked.connect(self.selectFilePushButtonClicked)