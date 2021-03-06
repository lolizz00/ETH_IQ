﻿from PyQt5 import QtCore, QtGui, QtWidgets
from mw import Ui_MainWindow

from DataReader import DataReader
from Plotter import Plotter
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon

from PlotWidget import PlotWidget

import numpy as np
class MW(QtWidgets.QMainWindow, Ui_MainWindow):



    # выбор файла для остройки из него
    def selectFilePushButtonClicked(self):
        self.filePathLineEdit.setText(QFileDialog.getOpenFileName()[0])

    # при нажатии на кноку автообновление
    def startUpdate(self):

        # берем интервал обновления и проверяем
        try:
            tout = float(self.updateLineEdit.text())
            tout = 1000 * tout
            tout = float(tout)
        except:
            self.showErr('Неверный интервал обновления!')
            return

        # разрешаем остановку
        self.stopPushButton.setEnabled(True)
        self.startPushButton.setEnabled(False)

        # запускаем считывание по таймеру
        self.timer.timeout.connect(self.start)
        self.timer.setInterval(tout)
        self.timer.start()

        self.start()

    # отсановка автообновления
    def stopUpdate(self):
        # меняем кнопочки
        self.stopPushButton.setEnabled(False)
        self.startPushButton.setEnabled(True)

        # останавливаем таймер
        self.timer.stop()

        #self.plotwidget.hide()

    # ясно
    def __init__(self):
        super(MW, self).__init__()
        self.preInitUi()
        self.connectSignals()
        self.initClass()
        self.hide()

    # отображение ошибки
    def showErr(self, text):
        QtWidgets.QMessageBox.critical(self, 'Ошибка!', text)

    # выборка каналов для Осцилограммы
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

    # обновление параметров чтения
    def updateReaderParams(self):
        try:
            channels = self._switchCnannels()


            if self.specModeRadioButton.isChecked() and self.SNR_checkBox.isChecked():
                n = int(self.SNR_chanComboBox.currentText()) - 1
                if not n in channels:
                    channels.append(n)

            if not len(channels):
                raise

            pointCnt = self.pointCntSpinBox.value()


            if self.chanCheckBox.isChecked():
                chanN = 1
            else:
                chanN = 2

            fs = self.getFs()

            # ---

            self.datareader.setChanN(chanN)
            self.datareader.initReader(fs, channels, pointCnt, self.addrLineEdit.text())


            return True
        except:
            self.showErr('Неверные параметры!')
            return False

    def getFs(self):
        fs =  int(self.SNR_fsLineEdit.text())
        if self.fsComboBox.currentText() == 'КГц':
            fs = fs * 1000
        elif self.fsComboBox.currentText() == 'МГц':
            fs = fs * 1000000
        return fs

    # обновление параметров графиков
    # в случае неверных параметров возвращает False
    def updatePlotParams(self):
        try:
            lst = {}

            if self.oscModeRadioButton.isChecked():
                lst['mode'] = 'osc'
                self.cnt = 1
            elif self.specModeRadioButton.isChecked():
                lst['mode'] = 'spec'
                self.cnt = int(self.cntLineEdit.text())


            lst['showSample'] = self.showSampleCheckBox.isChecked()
            lst['showSpline'] = self.showSplineCheckBox.isChecked()


            # выставляем значение частоты дискретизаци
            lst['fs'] = self.getFs()


            # работа с коэф. шума
            lst['offs'] = int(self.SNR_offsetLineEdit.text())
            if self.SNR_offsComboBox.currentText() == 'КГц':
                lst['offs'] = lst['offs'] * 1000
            elif self.SNR_offsComboBox.currentText() == 'МГц':
                lst['offs'] = lst['offs'] * 1000000

            lst['snr'] = self.SNR_checkBox.isChecked()

            lst['snrChan'] = int(self.SNR_chanComboBox.currentText())

            self.plotwidget.plotter.setParams(lst)

        except:
            self.showErr('Неверные параметры!')
            return False

        return True

    # вспомогательные классы
    def initClass(self):
        # читалка
        self.datareader = DataReader()
        self.datareader.log_signal.connect(self.writeLog)
        self.datareader.initDLL()

        # графики
        self.plotwidget = PlotWidget()
        self.plotwidget.plotter.log_signal.connect(self.writeLog)
        self.plotwidget.stop_signal.connect(self.stopPushButtonClicked)

        # таймер для регулярного обновления
        self.timer = QTimer()

    # включаем GUI
    def preInitUi(self):
        self.setupUi(self)
        self.setCentralWidget(self.cw)
        self.initTray()

    # работа в свернутом режиме
    def initTray(self):
        self.icon = QIcon("123.png")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.show()

    # отбражение сообщений из свернутого режима. Сказали отключить, т.к. бесит
    def showMessageTray(self, message):
        return
        self.tray.showMessage('Этажерка', message,msecs=10)

    # запись в лог
    def writeLog(self, msg, showErr=False):
        old_text = self.logTextEdit.toPlainText()

        # пустой
        if old_text == '':
            self.logTextEdit.setText(msg)
        else:
            self.logTextEdit.setText(old_text + '\n' + msg) # дополняем

        if showErr:
            pass
            self.showErr(msg)

    # запуск считыания
    def start(self):

        if not self.updatePlotParams():
            return

        self.showMessageTray('Обновляем графики...')


        data = {}



        for i in range(self.cnt):
            # пускаем, ждем, когда считается
            flg = True
            sch = 0
            while flg:

                if not self.updateReaderParams():
                    return
                if self.datareader.run():
                    flg = False
                    for k in self.datareader.data:
                        if not k in data:
                            data[k] = []
                        data[k].append(self.datareader.data[k])
                else:
                    sch = sch + 1
                    if sch > 10:
                        self.showErr('Не удалось считать после 10 попыток!')
                        return



        # если только считать файлы
        if self.onlySaveCheckBox.isChecked():
            return

        #  ---- костыль для усреднения. Выравниваем амплитуду и выравниваем между собой
        for chan in data:
            for i in range(len(data[chan])):
                data[chan][i].remA(int(self.cntSpinBox.text()))

        min = 999999
        for chan in data:
            for i in range(len(data[chan])):
                ln = len(data[chan][i].A)
                if(ln) < min:
                    min = ln


        for chan in data:
            for i in range(len(data[chan])):
                pass
                data[chan][i].remA(min)

        # ----


                #data[chan][i].rem(int(self.cntSpinBox.text()))

        # ображаем графиики
        self.plotwidget.show()

        if self.oscModeRadioButton.isChecked():
            for chanN in data:
                _data = data[chanN][0]
                self.plotwidget.plotter.oscSize = int(self.cntSpinBox.value())
                self.plotwidget.plotter.plotOsc(_data.X, _data.A, chanN + 1)
        elif self.specModeRadioButton.isChecked():
            for chanN in data:
                _data = data[chanN]
                self.plotwidget.plotter.plotSpec(_data, chanN + 1)
        else:
            return



    # нажатие на кнопку стоп
    def stopPushButtonClicked(self):
        self.stopUpdate()

    # рудимент
    def startFile(self):
            pass

    # нажатие на кнопку запуск
    def startPushButtonClicked(self):

        # если чтение в режиме реального времени
        if self.modeToolBox.currentWidget() == self.realPage:
            if self.updateCheckBox.isChecked():
                self.startUpdate() # циклический запуск
            else:
                self.start() # одиночный запуск
        else:

            # если чтение из файла


            if not self.suppFileCheckBox.isChecked(): # если выбрано "удерживать прошлый график"
                if not self.updatePlotParams(): # если неверные параметры графика, выходим
                    return
            else:
               if not self.plotwidget.plotter.specPlot and not self.plotwidget.plotter.oscPlot and not self.plotwidget.plotter.oscPlotQ: # если график еще не создан
                   self.updatePlotParams() # создаем


            # выбираем режим IQ I
            chanN = int(self.chanComboBox.currentText())

            # настраиваем-запускаем
            self.datareader.setChanN(chanN)
            self.datareader.fs = self.getFs()

            if not self.datareader.readFile(self.filePathLineEdit.text()):
                return


            #  пусто
            if not len(self.datareader.data):
                return 


            self.plotwidget.show()


            # берем данные
            data = self.datareader.data[0]


            # удаляем лишние данные
            data.rem(int(self.cntSpinBox.text()))


            # выбираем нужный вид графика и строим
            if self.oscModeRadioButton.isChecked():
                self.plotwidget.plotter.oscSize = int(self.cntSpinBox.value())
                self.plotwidget.plotter.plotOsc(data.X, data.A, 0)
            elif self.specModeRadioButton.isChecked():
                self.plotwidget.plotter.plotSpec([data], 0)
            else:
                return

    # очистка лога
    def clearLogPushButtonClicked(self):
        self.logTextEdit.setText('')

    # подключение кнопок к обработчикам
    def connectSignals(self):
        self.startPushButton.clicked.connect(self.startPushButtonClicked)
        self.clearLogPushButton.clicked.connect(self.clearLogPushButtonClicked)
        self.stopPushButton.clicked.connect(self.stopPushButtonClicked)
        self.selectFilePushButton.clicked.connect(self.selectFilePushButtonClicked)