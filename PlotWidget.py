from PyQt5 import QtCore, QtGui, QtWidgets

from plotform import Ui_Plot


class PlotWidget(QtWidgets.QWidget, Ui_Plot):
    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)
        self.preInitUi()
        self.initSignals()

    def resizeEvent(self, event):
        self.plotter.figure.tight_layout()
        QtWidgets.QWidget.resizeEvent(self, event)

    def closeEvent(self, event):
        self.hide()
        event.ignore()

    def plusPushButtonClicked(self):
        self.plotter.plus()

    def minusPushButtonClicked(self):
        self.plotter.minus()

    def leftPushButtonClicked(self):
        self.plotter.moveLeft()

    def rightPushButtonClicked(self):
        self.plotter.moveRight()

    def preInitUi(self):
        self.setupUi(self)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.plotter)
        self.layout.addWidget(self.controlGroupBox)
        self.setLayout(self.layout)



    def initSignals(self):
        self.leftPushButton.clicked.connect(self.leftPushButtonClicked)
        self.rightPushButton.clicked.connect(self.rightPushButtonClicked)
        self.plusPushButton.clicked.connect(self.plusPushButtonClicked)
        self.minusPushButton.clicked.connect(self.minusPushButtonClicked)