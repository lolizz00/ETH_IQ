# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\NEW_ETH_IQ\plotform.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Plot(object):
    def setupUi(self, Plot):
        Plot.setObjectName("Plot")
        Plot.resize(758, 556)
        self.controlGroupBox = QtWidgets.QGroupBox(Plot)
        self.controlGroupBox.setGeometry(QtCore.QRect(20, 440, 711, 100))
        self.controlGroupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.controlGroupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.controlGroupBox.setObjectName("controlGroupBox")
        self.clearPushButton = QtWidgets.QPushButton(self.controlGroupBox)
        self.clearPushButton.setGeometry(QtCore.QRect(30, 30, 75, 23))
        self.clearPushButton.setObjectName("clearPushButton")
        self.helpPushButton = QtWidgets.QPushButton(self.controlGroupBox)
        self.helpPushButton.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.helpPushButton.setObjectName("helpPushButton")
        self.plotter = QtWidgets.QWidget(Plot)
        self.plotter.setGeometry(QtCore.QRect(20, 40, 721, 401))
        self.plotter.setObjectName("plotter")

        self.retranslateUi(Plot)
        QtCore.QMetaObject.connectSlotsByName(Plot)

    def retranslateUi(self, Plot):
        _translate = QtCore.QCoreApplication.translate
        Plot.setWindowTitle(_translate("Plot", "Графики"))
        self.controlGroupBox.setTitle(_translate("Plot", "Управление"))
        self.clearPushButton.setText(_translate("Plot", "Очистить"))
        self.helpPushButton.setText(_translate("Plot", "Справка"))


