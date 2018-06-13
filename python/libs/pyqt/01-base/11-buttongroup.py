from PyQt5.QtWidgets import *
import sys


# push button or check button
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.button_group = QButtonGroup()
        # enforce only on button in the group can be select at a time
        self.button_group.setExclusive(False)
        self.button_group.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton('button 1')
        # 1 id
        self.button_group.addButton(button, 1)
        layout.addWidget(button)

        button = QPushButton('button 2')
        self.button_group.addButton(button, 2)
        layout.addWidget(button)

    def on_button_clicked(self, id):
        for button in self.button_group.buttons():
            if button is self.button_group.button(id):
                print("%s was clicked" % button.text())


qApp = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(qApp.exec_())
