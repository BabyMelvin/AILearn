from PyQt5.QtWidgets import *
import sys


class GroupBox(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('GroupBox')

        layout = QGridLayout()
        self.setLayout(layout)

        groupbox = QGroupBox('group box example')
        # programatically setting the checked state of the GroupBox can be done using
        groupbox.setCheckable(True)
        layout.addWidget(groupbox)

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        radiobutton = QRadioButton('radiobutton 1')
        radiobutton.setCheckable(True)
        vbox.addWidget(radiobutton)
        radiobutton = QRadioButton('radiobutton 2')
        vbox.addWidget(radiobutton)


qApp = QApplication(sys.argv)
screen = GroupBox()
screen.show()
sys.exit(qApp.exec_())
