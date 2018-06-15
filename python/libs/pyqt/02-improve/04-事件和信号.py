from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('signal and slot')
        self.show()


# 重构事件处理器
class Example2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Enter handler')
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


# 事件发送
class Example3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        x = 0
        y = 0
        self.text = "x:{0},y:{1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        text = "x:{0},y:{0}".format(x, y)
        self.label.setText(text)


# 事件发送 sender()方法
class Example4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('button 1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('button 2', self)
        btn2.move(150, 50)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    # ｓｌｏｔ
    def buttonClicked(self):
        # sender 是btn1 或 btn2
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + 'was passed')


# 信号发送
class Communicate(QObject):
    closeApp = pyqtSignal()


class Example5(QMainWindow):
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


def example():
    app = QApplication(sys.argv)
    ex = Example4()
    sys.exit(app.exec_())


example()
