# used to display widgets


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class Window(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle('window')
        self.resize(400, 300)

    def setTitle(self, title):
        self.setTitle()

    def setMinMax(self, max, min):
        if max:
            self.showMinimized()

        if min:
            self.showMinimized()

    def showFullScreen(self):
        self.showFullScreen()

    def showNormal(self):
        self.showNormal()

    def setSize(self, minHeight, maxHeight, minWidth, maxWidth):
        self.setMinimumHeight(minHeight)
        self.setMaximumHeight(maxHeight)
        self.setMinimumWidth(minWidth)
        self.setMaximumWidth(maxWidth)
        # set size
        self.setWidth(maxWidth)
        self.setHeight(maxHeight)


qApp = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(qApp.exec_())
