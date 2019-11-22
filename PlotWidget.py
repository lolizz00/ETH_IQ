from PyQt5 import QtCore, QtGui, QtWidgets

from plotform import Ui_Plot
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from helpplot import Ui_Form as helpPlotUI

class PlotWidget(QtWidgets.QWidget, Ui_Plot):

    stop_signal = pyqtSignal()

    def clear(self):
        self.plotter.clearPlots()

    def helpPushButtonClicked(self):
        self.helpui = helpPlotUI()
        self.wid = QWidget()
        self.helpui.setupUi(self.wid)
        self.wid.show()

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)
        self.preInitUi()
        self.initSignals()

    def resizeEvent(self, event):
        self.plotter.figure.tight_layout()
        QtWidgets.QWidget.resizeEvent(self, event)

    def closeEvent(self, event):
        self.hide()
        self.stop_signal.emit()
        event.ignore()


    def preInitUi(self):
        self.setupUi(self)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.plotter)
        self.layout.addWidget(self.controlGroupBox)
        self.setLayout(self.layout)

    def initSignals(self):
        self.clearPushButton.clicked.connect(self.clear)
        self.helpPushButton.clicked.connect(self.helpPushButtonClicked)
