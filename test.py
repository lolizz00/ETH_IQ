from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

from random import randint

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)

    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            #self.autoRange()
            self.setXRange(0,5)
            self.setYRange(0,10)

    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)


app = pg.mkQApp()

vb = CustomViewBox()

graph = pg.PlotWidget(viewBox=vb, enableMenu=False)

colour = []

for i in range(0,3):
    colourvalue = [randint(0,255), randint(0,255), randint(0,255)]
    tuple(colourvalue)
    colour.append(colourvalue)

y_data = [
     [['a',0],['b',1],['c',None],['d',6],['e',7]],
     [['a',5],['b',2],['c',1],['d',None],['e',1]],
     [['a',3],['b',None],['c',4],['d',9],['e',None]],
     ]

x_data = [0, 1, 2, 3, 4]

for i in range(3):
    xv = []
    yv = []
    for j, v in enumerate(row[i][1] for row in y_data):
        if v is not None:
            xv.append(int(j))
            yv.append(float(v))
        graph.plot(xv, yv, pen = colour[i], name=y_data[0][i][0])

graph.show()
graph.setWindowTitle('Hourly Frequency Graph')
graph.setXRange(0,5)
graph.setYRange(0,10)

graph.setLabel('left', "Frequency", units='%')
graph.setLabel('bottom', "Hour")
graph.showGrid(x=True, y=True)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()