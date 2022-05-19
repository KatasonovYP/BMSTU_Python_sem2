import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.layout = QGridLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)
        self.initUI()
    
    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    screen = MainWindow()
    screen.show()
    sys.exit(app.exec_())
