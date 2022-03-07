import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.table import Table



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.window = QWidget()
        self.layout = QGridLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)
        self.init_gui()
        self.init_methods()
    
    def init_gui(self):
        self.table = Table()
        self.layout.addChildWidget(self.table)
        
    
    def init_methods(self):
        ...


if __name__ == '__main__':
    app = QApplication([])
    screen = MainWindow()
    screen.show()
    sys.exit(app.exec_())