# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\NEW_ETH_IQ\mw.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 757)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cw = QtWidgets.QWidget(self.centralwidget)
        self.cw.setGeometry(QtCore.QRect(0, 0, 961, 721))
        self.cw.setMinimumSize(QtCore.QSize(750, 500))
        self.cw.setObjectName("cw")
        self.gridLayout = QtWidgets.QGridLayout(self.cw)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.cw)
        self.groupBox.setObjectName("groupBox")
        self.startPushButton = QtWidgets.QPushButton(self.groupBox)
        self.startPushButton.setGeometry(QtCore.QRect(90, 340, 75, 23))
        self.startPushButton.setObjectName("startPushButton")
        self.modeToolBox = QtWidgets.QToolBox(self.groupBox)
        self.modeToolBox.setGeometry(QtCore.QRect(30, 120, 311, 181))
        self.modeToolBox.setObjectName("modeToolBox")
        self.realPage = QtWidgets.QWidget()
        self.realPage.setGeometry(QtCore.QRect(0, 0, 311, 127))
        self.realPage.setObjectName("realPage")
        self.layoutWidget = QtWidgets.QWidget(self.realPage)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 232, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pointCntSpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.pointCntSpinBox.setMinimum(100)
        self.pointCntSpinBox.setMaximum(5000)
        self.pointCntSpinBox.setSingleStep(10)
        self.pointCntSpinBox.setProperty("value", 100)
        self.pointCntSpinBox.setObjectName("pointCntSpinBox")
        self.horizontalLayout_2.addWidget(self.pointCntSpinBox)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.layoutWidget1 = QtWidgets.QWidget(self.realPage)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 50, 195, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.updateCheckBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.updateCheckBox.setObjectName("updateCheckBox")
        self.horizontalLayout_3.addWidget(self.updateCheckBox)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.updateLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.updateLineEdit.setObjectName("updateLineEdit")
        self.horizontalLayout_3.addWidget(self.updateLineEdit)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.onlySaveCheckBox = QtWidgets.QCheckBox(self.realPage)
        self.onlySaveCheckBox.setGeometry(QtCore.QRect(70, 90, 151, 16))
        self.onlySaveCheckBox.setObjectName("onlySaveCheckBox")
        self.modeToolBox.addItem(self.realPage, "")
        self.filePage = QtWidgets.QWidget()
        self.filePage.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.filePage.setObjectName("filePage")
        self.layoutWidget2 = QtWidgets.QWidget(self.filePage)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 254, 27))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.filePathLineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        self.horizontalLayout.addWidget(self.filePathLineEdit)
        self.selectFilePushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.selectFilePushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.selectFilePushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.selectFilePushButton.setObjectName("selectFilePushButton")
        self.horizontalLayout.addWidget(self.selectFilePushButton)
        self.suppFileCheckBox = QtWidgets.QCheckBox(self.filePage)
        self.suppFileCheckBox.setGeometry(QtCore.QRect(60, 0, 181, 21))
        self.suppFileCheckBox.setObjectName("suppFileCheckBox")
        self.modeToolBox.addItem(self.filePage, "")
        self.stopPushButton = QtWidgets.QPushButton(self.groupBox)
        self.stopPushButton.setEnabled(False)
        self.stopPushButton.setGeometry(QtCore.QRect(200, 340, 75, 23))
        self.stopPushButton.setObjectName("stopPushButton")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 30, 301, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 0, 0, 1, 2)
        self.cntSpinBox = QtWidgets.QSpinBox(self.layoutWidget3)
        self.cntSpinBox.setMinimum(10)
        self.cntSpinBox.setMaximum(10000000)
        self.cntSpinBox.setSingleStep(100)
        self.cntSpinBox.setProperty("value", 10000)
        self.cntSpinBox.setObjectName("cntSpinBox")
        self.gridLayout_6.addWidget(self.cntSpinBox, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 1, 0, 1, 1)
        self.addrLineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.addrLineEdit.setObjectName("addrLineEdit")
        self.gridLayout_6.addWidget(self.addrLineEdit, 1, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.cw)
        self.groupBox_2.setObjectName("groupBox_2")
        self.clearLogPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.clearLogPushButton.setGeometry(QtCore.QRect(160, 210, 75, 23))
        self.clearLogPushButton.setObjectName("clearLogPushButton")
        self.logTextEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.logTextEdit.setGeometry(QtCore.QRect(20, 20, 341, 161))
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.cw)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 400))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(280, 80, 141, 65))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.oscModeRadioButton = QtWidgets.QRadioButton(self.layoutWidget4)
        self.oscModeRadioButton.setChecked(True)
        self.oscModeRadioButton.setObjectName("oscModeRadioButton")
        self.gridLayout_5.addWidget(self.oscModeRadioButton, 0, 0, 1, 1)
        self.specModeRadioButton = QtWidgets.QRadioButton(self.layoutWidget4)
        self.specModeRadioButton.setChecked(False)
        self.specModeRadioButton.setObjectName("specModeRadioButton")
        self.gridLayout_5.addWidget(self.specModeRadioButton, 1, 0, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget5.setGeometry(QtCore.QRect(30, 30, 152, 31))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.SNR_fsLineEdit = QtWidgets.QLineEdit(self.layoutWidget5)
        self.SNR_fsLineEdit.setObjectName("SNR_fsLineEdit")
        self.horizontalLayout_5.addWidget(self.SNR_fsLineEdit)
        self.fsComboBox = QtWidgets.QComboBox(self.layoutWidget5)
        self.fsComboBox.setObjectName("fsComboBox")
        self.fsComboBox.addItem("")
        self.fsComboBox.addItem("")
        self.fsComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.fsComboBox)
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget6.setGeometry(QtCore.QRect(30, 80, 201, 88))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chan1checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan1checkBox.setChecked(True)
        self.chan1checkBox.setObjectName("chan1checkBox")
        self.gridLayout_2.addWidget(self.chan1checkBox, 0, 0, 1, 1)
        self.chan5checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan5checkBox.setChecked(False)
        self.chan5checkBox.setObjectName("chan5checkBox")
        self.gridLayout_2.addWidget(self.chan5checkBox, 0, 1, 1, 1)
        self.chan2checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan2checkBox.setChecked(False)
        self.chan2checkBox.setObjectName("chan2checkBox")
        self.gridLayout_2.addWidget(self.chan2checkBox, 1, 0, 1, 1)
        self.chan6checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan6checkBox.setChecked(False)
        self.chan6checkBox.setObjectName("chan6checkBox")
        self.gridLayout_2.addWidget(self.chan6checkBox, 1, 1, 1, 1)
        self.chan3checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan3checkBox.setChecked(False)
        self.chan3checkBox.setObjectName("chan3checkBox")
        self.gridLayout_2.addWidget(self.chan3checkBox, 2, 0, 1, 1)
        self.chan7checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan7checkBox.setChecked(False)
        self.chan7checkBox.setObjectName("chan7checkBox")
        self.gridLayout_2.addWidget(self.chan7checkBox, 2, 1, 1, 1)
        self.chan4checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan4checkBox.setChecked(False)
        self.chan4checkBox.setObjectName("chan4checkBox")
        self.gridLayout_2.addWidget(self.chan4checkBox, 3, 0, 1, 1)
        self.chan8checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.chan8checkBox.setChecked(False)
        self.chan8checkBox.setObjectName("chan8checkBox")
        self.gridLayout_2.addWidget(self.chan8checkBox, 3, 1, 1, 1)
        self.layoutWidget7 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 180, 261, 120))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.cntLineEdit = QtWidgets.QLineEdit(self.layoutWidget7)
        self.cntLineEdit.setObjectName("cntLineEdit")
        self.horizontalLayout_6.addWidget(self.cntLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SNR_offsetLineEdit = QtWidgets.QLineEdit(self.layoutWidget7)
        self.SNR_offsetLineEdit.setObjectName("SNR_offsetLineEdit")
        self.gridLayout_3.addWidget(self.SNR_offsetLineEdit, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.SNR_checkBox = QtWidgets.QCheckBox(self.layoutWidget7)
        self.SNR_checkBox.setObjectName("SNR_checkBox")
        self.gridLayout_3.addWidget(self.SNR_checkBox, 0, 0, 1, 1)
        self.SNR_chanComboBox = QtWidgets.QComboBox(self.layoutWidget7)
        self.SNR_chanComboBox.setObjectName("SNR_chanComboBox")
        self.SNR_chanComboBox.addItem("")
        self.SNR_chanComboBox.addItem("")
        self.SNR_chanComboBox.addItem("")
        self.SNR_chanComboBox.addItem("")
        self.SNR_chanComboBox.addItem("")
        self.SNR_chanComboBox.addItem("")
        self.SNR_chanComboBox.addItem("")
        self.SNR_chanComboBox.addItem("")
        self.gridLayout_3.addWidget(self.SNR_chanComboBox, 1, 1, 1, 1)
        self.SNR_offsComboBox = QtWidgets.QComboBox(self.layoutWidget7)
        self.SNR_offsComboBox.setObjectName("SNR_offsComboBox")
        self.SNR_offsComboBox.addItem("")
        self.SNR_offsComboBox.addItem("")
        self.SNR_offsComboBox.addItem("")
        self.gridLayout_3.addWidget(self.SNR_offsComboBox, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.layoutWidget8 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget8.setGeometry(QtCore.QRect(290, 180, 153, 91))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.showSampleCheckBox = QtWidgets.QCheckBox(self.layoutWidget8)
        self.showSampleCheckBox.setChecked(True)
        self.showSampleCheckBox.setObjectName("showSampleCheckBox")
        self.verticalLayout.addWidget(self.showSampleCheckBox)
        self.showSplineCheckBox = QtWidgets.QCheckBox(self.layoutWidget8)
        self.showSplineCheckBox.setChecked(True)
        self.showSplineCheckBox.setObjectName("showSplineCheckBox")
        self.verticalLayout.addWidget(self.showSplineCheckBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chanCheckBox = QtWidgets.QCheckBox(self.layoutWidget8)
        self.chanCheckBox.setObjectName("chanCheckBox")
        self.horizontalLayout_4.addWidget(self.chanCheckBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.modeToolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Синхронная этажерка"))
        self.groupBox.setTitle(_translate("MainWindow", "Управление"))
        self.startPushButton.setText(_translate("MainWindow", "Старт!"))
        self.label_2.setText(_translate("MainWindow", "Кол-во посылок:"))
        self.label_12.setText(_translate("MainWindow", "[100;5000]"))
        self.updateCheckBox.setText(_translate("MainWindow", "Обновлять "))
        self.label_7.setText(_translate("MainWindow", "Раз в "))
        self.updateLineEdit.setText(_translate("MainWindow", "5"))
        self.label_8.setText(_translate("MainWindow", "с"))
        self.onlySaveCheckBox.setText(_translate("MainWindow", "Не отстраивать графики"))
        self.modeToolBox.setItemText(self.modeToolBox.indexOf(self.realPage), _translate("MainWindow", "Реальное время"))
        self.label.setText(_translate("MainWindow", "Путь:"))
        self.selectFilePushButton.setText(_translate("MainWindow", "..."))
        self.suppFileCheckBox.setText(_translate("MainWindow", "Удерживать прошлый график"))
        self.modeToolBox.setItemText(self.modeToolBox.indexOf(self.filePage), _translate("MainWindow", "Файл"))
        self.stopPushButton.setText(_translate("MainWindow", "Стоп!"))
        self.label_10.setText(_translate("MainWindow", "Кол-во точек для отстройки:"))
        self.label_11.setText(_translate("MainWindow", "Адрес:"))
        self.addrLineEdit.setText(_translate("MainWindow", "192.168.18.70"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Лог"))
        self.clearLogPushButton.setText(_translate("MainWindow", "Очистить"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Графики"))
        self.oscModeRadioButton.setText(_translate("MainWindow", "Осцилограмма"))
        self.specModeRadioButton.setText(_translate("MainWindow", "Спектограмма"))
        self.label_13.setText(_translate("MainWindow", "Fs:"))
        self.SNR_fsLineEdit.setText(_translate("MainWindow", "5000"))
        self.fsComboBox.setItemText(0, _translate("MainWindow", "Гц"))
        self.fsComboBox.setItemText(1, _translate("MainWindow", "КГц"))
        self.fsComboBox.setItemText(2, _translate("MainWindow", "МГц"))
        self.chan1checkBox.setText(_translate("MainWindow", "Канал 1"))
        self.chan5checkBox.setText(_translate("MainWindow", "Канал 5"))
        self.chan2checkBox.setText(_translate("MainWindow", "Канал 2"))
        self.chan6checkBox.setText(_translate("MainWindow", "Канал 6"))
        self.chan3checkBox.setText(_translate("MainWindow", "Канал 3"))
        self.chan7checkBox.setText(_translate("MainWindow", "Канал 7"))
        self.chan4checkBox.setText(_translate("MainWindow", "Канал 4"))
        self.chan8checkBox.setText(_translate("MainWindow", "Канал 8"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Настройки спектограммы</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Усреднение: "))
        self.cntLineEdit.setText(_translate("MainWindow", "1"))
        self.SNR_offsetLineEdit.setText(_translate("MainWindow", "1000"))
        self.label_9.setText(_translate("MainWindow", "Канал:"))
        self.label_3.setText(_translate("MainWindow", "Смещение от пика"))
        self.SNR_checkBox.setText(_translate("MainWindow", "Вычислить SNR"))
        self.SNR_chanComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.SNR_chanComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.SNR_chanComboBox.setItemText(2, _translate("MainWindow", "3"))
        self.SNR_chanComboBox.setItemText(3, _translate("MainWindow", "4"))
        self.SNR_chanComboBox.setItemText(4, _translate("MainWindow", "5"))
        self.SNR_chanComboBox.setItemText(5, _translate("MainWindow", "6"))
        self.SNR_chanComboBox.setItemText(6, _translate("MainWindow", "7"))
        self.SNR_chanComboBox.setItemText(7, _translate("MainWindow", "8"))
        self.SNR_offsComboBox.setItemText(0, _translate("MainWindow", "Гц"))
        self.SNR_offsComboBox.setItemText(1, _translate("MainWindow", "КГц"))
        self.SNR_offsComboBox.setItemText(2, _translate("MainWindow", "МГц"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Настройки осцилограммы</span></p></body></html>"))
        self.showSampleCheckBox.setText(_translate("MainWindow", "Отображать точки"))
        self.showSplineCheckBox.setText(_translate("MainWindow", "Отображать график"))
        self.chanCheckBox.setText(_translate("MainWindow", "Вещественный"))


