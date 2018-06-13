from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton('click me')
        # slot and signal
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 0, 0)

    @pyqtSlot()
    def on_button_clicked(self):
        print('the button was pressed')


qApp = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(qApp.exec_())
