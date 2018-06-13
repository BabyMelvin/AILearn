from PyQt5.QtWidgets import *
import sys


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton('Brazil')
        radiobutton.setCheckable(True)
        # 相当于object id?
        radiobutton.country = "Brazil"
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton('Ecuador')
        radiobutton.country = 'Ecuador'
        radiobutton.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(radiobutton, 0, 2)

    def on_radio_button_toggled(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            print('selected country is %s' % radiobutton.country)


qApp = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(qApp.exec_())
