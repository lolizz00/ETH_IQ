from PyQt5 import QtCore, QtGui, QtWidgets
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

from helpspec import Ui_Form as helpSpecUI

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
            tout = int(tout)
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

    # выборка каналов для Спектра
    def switchChannelsSpec(self):
        channels = []

        if self.specChan1checkBox.isChecked():
            channels.append(0)
        if self.specChan2checkBox.isChecked():
            channels.append(1)
        if self.specChan3checkBox.isChecked():
            channels.append(2)
        if self.specChan4checkBox.isChecked():
            channels.append(3)
        if self.specChan5checkBox.isChecked():
            channels.append(4)
        if self.specChan6checkBox.isChecked():
            channels.append(5)
        if self.specChan7checkBox.isChecked():
            channels.append(6)
        if self.specChan8checkBox.isChecked():
            channels.append(7)


        return channels

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


            if self.snrModeRadioButton.isChecked():
                channels = [int(self.SNR_chanComboBox.currentText()) -1 ]
            elif not self.specModeRadioButton.isChecked():
                channels = self._switchCnannels()
                if not len(channels):
                    raise
            else:
                channels = self.switchChannelsSpec()


            if not len(channels):
                raise

            pointCnt = self.pointCntSpinBox.value()

            chanN = int(self.chanComboBox.currentText())

            fs = int(self.SNR_fsLineEdit.text())

            # ---

            self.datareader.setChanN(chanN)
            self.datareader.initReader(fs, channels, pointCnt, self.addrLineEdit.text())

        except:
            self.showErr('Неверные параметры!')


    # обновление параметров графиков
    # в случае неверных параметров возвращает False
    def updatePlotParams(self):
        try:
            lst = {}

            if self.oscModeRadioButton.isChecked():
                lst['mode'] = 'osc'
            elif self.iqModeRadioButton.isChecked():
                lst['mode'] = 'iq'
            elif self.specModeRadioButton.isChecked():
                lst['mode'] = 'spec'
            elif self.snrModeRadioButton.isChecked():
                lst['mode'] = 'snr'


            lst['showSample'] = self.showSampleCheckBox.isChecked()
            lst['showSpline'] = self.showSplineCheckBox.isChecked()



            lst['fs'] = int(self.SNR_fsLineEdit.text())



            lst['offs'] = int(self.SNR_offsetLineEdit.text())

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
    def writeLog(self, msg):
        old_text = self.logTextEdit.toPlainText()

        # пустой
        if old_text == '':
            self.logTextEdit.setText(msg)
        else:
            self.logTextEdit.setText(old_text + '\n' + msg) # дополняем

    # остройка SNR
    def startSNR(self):
        if not self.updatePlotParams():
            return

        self.showMessageTray('Обновляем графики...')




        data = []
        n = int(self.SNR_cntLineEdit.text())
        for i in range(n):
            self.updateReaderParams()
            self.datareader.run()
            _data = self.datareader.data[0]
            _data.rem(int(self.cntSpinBox.text()))
            _data = _data.A
            data.append(_data)






        self.plotwidget.plotter.specWithSNR(data)
        self.plotwidget.show()

    # запуск считыания
    def start(self):

        # обрабатываем особоым способом
        if self.snrModeRadioButton.isChecked():
            self.startSNR()
            return

        if not self.updatePlotParams():
            return

        self.showMessageTray('Обновляем графики...')


        # выставляем параметры DataReader
        self.updateReaderParams()

        # пускаем
        self.datareader.run()

        # если только считать файлы
        if self.onlySaveCheckBox.isChecked():
            return 


        # ображаем графиики
        self.plotwidget.show()   
        sch = 0
        for data in self.datareader.data: # перебираем каналы

            n = self.datareader.THREAD_N[sch] + 1
            sch = sch + 1
            data.rem(int(self.cntSpinBox.text()))

            self.plotwidget.plotter.oscSize = int(self.cntSpinBox.value())

            if self.oscModeRadioButton.isChecked():
                self.plotwidget.plotter.plotOsc(data.X, data.A, n)

            if self.iqModeRadioButton.isChecked():
                self.plotwidget.plotter.plotIQ(data.X, data.I, data.Q, n)

            if self.specModeRadioButton.isChecked():
                self.plotwidget.plotter.plotSpec(data.A, n)

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
            self.datareader.readFile(self.filePathLineEdit.text())


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
                self.plotwidget.plotter.plotOsc(data.X, data.A, 0)

            if self.iqModeRadioButton.isChecked():
                   self.plotwidget.plotter.plotIQ(data.X, data.I, data.Q, 0)

            if self.specModeRadioButton.isChecked():
                self.plotwidget.plotter.plotSpec(data.A, 0)

    # очистка лога
    def clearLogPushButtonClicked(self):
        self.logTextEdit.setText('')

    # подключение кнопок к обработчикам
    def connectSignals(self):
        self.startPushButton.clicked.connect(self.startPushButtonClicked)
        self.clearLogPushButton.clicked.connect(self.clearLogPushButtonClicked)
        self.stopPushButton.clicked.connect(self.stopPushButtonClicked)
        self.selectFilePushButton.clicked.connect(self.selectFilePushButtonClicked)