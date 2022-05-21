from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from src.painter import Paint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.layout = QGridLayout()
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)
        self.initUI()
        self.connectBtns()

    def initUI(self):
        self.painter = Paint()
        self.layout.addWidget(self.painter, 0, 0, 1, 3)

        self.inputX = QLineEdit()
        self.inputX.setPlaceholderText('Введите X')
        self.layout.addWidget(self.inputX, 1, 0)

        self.inputY = QLineEdit()
        self.inputY.setPlaceholderText('Введите Y')
        self.layout.addWidget(self.inputY, 1, 1)

        self.addBtn = QPushButton('Добавить точку')
        self.layout.addWidget(self.addBtn, 1, 2)

    def connectBtns(self):
        self.addBtn.clicked.connect(lambda: self.addPoint())

    def addPoint(self):
        try:
            x = int(self.inputX.text())
            y = int(self.inputY.text())
        except:
            self.inputX.setPlaceholderText('Введите численный X!')
            self.inputY.setPlaceholderText('Введите численный Y!')
        else:
            self.inputX.setPlaceholderText('Введите X')
            self.inputY.setPlaceholderText('Введите Y')
            self.painter.addPoint(x, y)
        self.inputX.setText('')
        self.inputY.setText('')

if __name__ == '__main__':
    app = QApplication([])
    screen = MainWindow()
    screen.show()
    app.exec()
