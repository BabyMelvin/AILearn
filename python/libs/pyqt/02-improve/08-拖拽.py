from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

"""
在GUI里，拖放是指用户点击一个虚拟对象，拖动放置到另一个对象的动作
一般拖动两种东西：数据和图形界面。
    把图像从一个应用拖放到另一个应用上实质是操作二进制数据
    把一个表格从Firefox上拖放到一个实质是操作一个图形组
"""


# 1. 简单拖放
class Button1(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    # 激活组件的拖拽事件
    # 设定好接受拖拽的数据类型(plain text)
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())


class Example1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button1('Button', self)
        button.move(190, 65)

        self.setWindowTitle('simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


# 2.拖放按钮组件
class Button2(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.RightButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            print('press')


class Example2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button2('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        position = event.pos()
        self.button.move(position)

        event.setDropAction(Qt.MoveAction)
        event.accept()


def example_main():
    app = QApplication(sys.argv)
    ex = Example2()
    ex.show()
    app.exec_()


example_main()
