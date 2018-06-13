from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton('sample Tooltip')
        button.setToolTip('this ToolTip simply displays text')
        layout.addWidget(button, 0, 0)

        button = QPushButton('Formatted ToolTip')
        button.setToolTip("<b>Formatted text</b>can also be displayed")
        layout.addWidget(button, 1, 0)

        label = QLabel("Focus ComboBox and press SHIFT+F1")
        layout.addWidget(label)

        self.combobox = QComboBox()
        self.combobox.setWhatsThis("this is a 'what's' object description")
        layout.addWidget(self.combobox)

qApp = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(qApp.exec_())
