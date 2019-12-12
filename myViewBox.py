from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Point import Point
from pyqtgraph import functions as fn

__all__ = ['ViewBox']

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)

        self.setMouseMode(self.RectMode)
        self.setMouseMode(self.RectMode)

    def mouseDragEvent(self, ev, axis=None):
        ev.accept()

        pos = ev.pos()
        lastPos = ev.lastPos()
        dif = pos - lastPos
        dif = dif * -1
        mouseEnabled = np.array(self.state['mouseEnabled'], dtype=np.float)
        mask = mouseEnabled.copy()
        if axis is not None:
            mask[1 - axis] = 0.0

        if ev.button() & (QtCore.Qt.LeftButton | QtCore.Qt.MidButton):
            tr = dif * mask
            tr = self.mapToView(tr) - self.mapToView(Point(0, 0))
            x = tr.x() if mask[0] == 1 else None
            y = tr.y() if mask[1] == 1 else None

            self._resetTarget()
            if x is not None or y is not None:
                self.translateBy(x=x, y=y)
                self.sigRangeChangedManually.emit(self.state['mouseEnabled'])
        elif ev.button() & QtCore.Qt.RightButton:
            if ev.isFinish():
                self.rbScaleBox.hide()
                ax = QtCore.QRectF(Point(ev.buttonDownPos(ev.button())), Point(pos))
                ax = self.childGroup.mapRectFromParent(ax)
                self.showAxRect(ax)
                self.axHistoryPointer += 1
                self.axHistory = self.axHistory[:self.axHistoryPointer] + [ax]
            else:
                self.updateScaleBox(ev.buttonDownPos(), ev.pos())
