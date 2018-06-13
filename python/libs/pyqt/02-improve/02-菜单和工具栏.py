import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # action
        exitAct = QAction(QIcon('image/web_icon.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        impMenu = QMenu('import', self)
        impAct = QAction('import mail', self, checkable=True)
        impAct.setChecked(True)
        impAct.triggered.connect(self.toggle_menu)
        impMenu.addAction(impAct)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addMenu(impMenu)

        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')
        self.show()

    def toggle_menu(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


app = QApplication(sys.argv)
ex = Example()
sys.exit(qApp.exec_())
