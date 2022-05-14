import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



class Inputs(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.init_gui()
        self.init_methods()
    
    def init_gui(self):
        self.input_func = QLineEdit('x ** 2 - 2')
        self.input_start = QLineEdit('-10')
        self.input_end = QLineEdit('10')
        self.input_step = QLineEdit('0.5')
        self.input_Nmax = QLineEdit('200')
        self.input_eps = QLineEdit('10e-7')

        self.label_func = QLabel('Введите функцию')
        self.label_start = QLabel('Начало отрезка')
        self.label_end = QLabel('Конец отрезка')
        self.label_step = QLabel('Шаг')
        self.label_Nmax = QLabel('Максимальная итерация')
        self.label_eps = QLabel('Точность')

        self.btn_res = QPushButton('Найти корни')

        self.layout.addWidget(self.label_func, 0, 0)
        self.layout.addWidget(self.label_start, 1, 0)
        self.layout.addWidget(self.label_end, 2, 0)
        self.layout.addWidget(self.label_step, 3, 0)
        self.layout.addWidget(self.label_Nmax, 4, 0)
        self.layout.addWidget(self.label_eps, 5, 0)

        self.layout.addWidget(self.input_func, 0, 1)
        self.layout.addWidget(self.input_start, 1, 1)
        self.layout.addWidget(self.input_end, 2, 1)
        self.layout.addWidget(self.input_step, 3, 1)
        self.layout.addWidget(self.input_Nmax, 4, 1)
        self.layout.addWidget(self.input_eps, 5, 1)

        self.layout.addWidget(self.btn_res, 6, 0, 1, 2)
        
        
    
    def init_methods(self):
        ...


if __name__ == '__main__':
    app = QApplication([])
    screen = Inputs()
    screen.show()
    sys.exit(app.exec_())