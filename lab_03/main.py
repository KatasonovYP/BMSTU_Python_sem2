import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.components import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = QWidget()
        self.layout = QGridLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)
        self.init_gui()
    
    def init_gui(self):
        self.tab_bar = QTabWidget()
        self.layout.addWidget(self.tab_bar, 0, 0)
        tabEncode = TabEncode(self)
        tabDecode = TabDecode(self)
        self.tab_bar.insertTab(0, tabEncode, 'Encode')
        self.tab_bar.insertTab(1, tabDecode, 'Decode')


if __name__ == '__main__':
    app = QApplication([])
    screen = MainWindow()
    screen.show()
    sys.exit(app.exec_())