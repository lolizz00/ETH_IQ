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
        self.plotter = Plotter(Plot)
        self.plotter.setGeometry(QtCore.QRect(80, 20, 551, 371))
        self.plotter.setObjectName("plotter")
        self.controlGroupBox = QtWidgets.QGroupBox(Plot)
        self.controlGroupBox.setGeometry(QtCore.QRect(110, 430, 501, 50))
        self.controlGroupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.controlGroupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.controlGroupBox.setObjectName("controlGroupBox")
        self.layoutWidget = QtWidgets.QWidget(self.controlGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 20, 120, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.leftPushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.leftPushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.leftPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftPushButton.setIcon(icon)
        self.leftPushButton.setObjectName("leftPushButton")
        self.horizontalLayout.addWidget(self.leftPushButton)
        self.rightPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.rightPushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.rightPushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.rightPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightPushButton.setIcon(icon1)
        self.rightPushButton.setObjectName("rightPushButton")
        self.horizontalLayout.addWidget(self.rightPushButton)
        self.minusPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.minusPushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.minusPushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.minusPushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("minus.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minusPushButton.setIcon(icon2)
        self.minusPushButton.setObjectName("minusPushButton")
        self.horizontalLayout.addWidget(self.minusPushButton)
        self.plusPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.plusPushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.plusPushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.plusPushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plus.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plusPushButton.setIcon(icon3)
        self.plusPushButton.setObjectName("plusPushButton")
        self.horizontalLayout.addWidget(self.plusPushButton)
        self.clearPushButton = QtWidgets.QPushButton(self.controlGroupBox)
        self.clearPushButton.setGeometry(QtCore.QRect(220, 20, 75, 23))
        self.clearPushButton.setObjectName("clearPushButton")

        self.retranslateUi(Plot)
        QtCore.QMetaObject.connectSlotsByName(Plot)

    def retranslateUi(self, Plot):
        _translate = QtCore.QCoreApplication.translate
        Plot.setWindowTitle(_translate("Plot", "Графики"))
        self.controlGroupBox.setTitle(_translate("Plot", "Управление"))
        self.clearPushButton.setText(_translate("Plot", "Очистить"))


from Plotter import Plotter
