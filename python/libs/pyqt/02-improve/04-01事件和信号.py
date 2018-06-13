# 发送自定义信号
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = Communicate()
        self.initUI()

    def initUI(self):
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Email signal')
        self.show()

    def mousePressEvent(self, event):
        # 发送消息
        self.c.closeApp.emit()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
