from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # tool tip
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("this is <b>QWidget</b> widget")

        btn = QPushButton('button', self)
        btn.setToolTip('this is <b>QPushButton</b> widget')
        # sizeHint默认大小
        btn.resize(btn.sizeHint())

        # 改变位置
        btn.move(50, 50)



        # slot
        qbtn = QPushButton('quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        # 窗口位置
        # 1.带窗口图标
        self.setGeometry(300, 300, 600, 400)

        # 是窗口居中
        self.center()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web_icon.jpg'))

    # 关闭会产生一个QCloseEvent事件
    def loseEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit'
                                     , QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 中心窗口
    def center(self):
        qr = self.frameGeometry()
        # QDesktopWidget提供桌面信息，包括屏幕大小
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


qApp = QApplication(sys.argv)
screen = Example()
screen.show()
sys.exit(qApp.exec_())
