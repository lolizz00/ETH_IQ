from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Point import Point
from pyqtgraph import functions as fn

from  pyqtgraph.graphicsItems.GraphicsWidget import  GraphicsWidget
from  pyqtgraph.graphicsItems.GraphicsWidgetAnchor import  GraphicsWidgetAnchor

from  pyqtgraph.GraphicsScene.mouseEvents import MouseDragEvent

from PyQt5.QtCore import pyqtSignal

class myTextItem(pg.TextItem):

    mouseSig = pyqtSignal(MouseDragEvent)

    def __init__(self):
        pg.TextItem.__init__(self, color=pg.mkColor('000000'), border=pg.mkColor('000000'))

    def mouseDragEvent(self, ev):
        ev.accept()
        self.mouseSig.emit(ev)



