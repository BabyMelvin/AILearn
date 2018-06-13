from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.checkbox1 = QCheckBox('Kestrel')
        self.checkbox1.setCheckable(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 0, 0)

        self.checkbox2 = QCheckBox('Sparrowhawk')
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 1, 10)

        self.checkbox3 = QCheckBox('Hobby')
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 2, 0)

    def checkbox_toggled(self):
        # 　利用局部变量，触发后释放
        selected = []
        if self.checkbox1.isChecked():
            selected.append('Kestrel')

        if self.checkbox2.isChecked():
            selected.append('Sparrowhawk')

        if self.checkbox3.isChecked():
            selected.append('Hobby')
        print("selected:%s" % " ".join(selected))


qApp = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(qApp.exec_())
