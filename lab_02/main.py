from cProfile import label
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.components import *
from src.logic import calculate_result



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
        self.input_tab = Inputs()
        self.layout.addWidget(self.input_tab, 0, 0)
        
    
    def init_methods(self):
        self.show_result()
    

    def show_result(self):
        self.input_tab.btn_res.clicked.connect(lambda: self.get_data())
        self.input_tab.btn_res.clicked.connect(lambda: self.show_table())
        self.input_tab.btn_res.clicked.connect(lambda: self.show_plot())
    

    def get_data(self):
        data = calculate_result(
            self.input_tab.input_func.text(),
            float(self.input_tab.input_start.text()),
            float(self.input_tab.input_end.text()),
            float(self.input_tab.input_step.text()),
            int(self.input_tab.input_Nmax.text()),
            float(self.input_tab.input_eps.text())
        )
        self.data = data['f']
        self.df = data['df']
        self.ddf = data['ddf']


    def show_table(self):
        self.table = Table(self.data['roots'])
        self.layout.addWidget(self.table, 1, 0)
    

    def show_plot(self):
        self.layout.addWidget(My_plot(
            self.data['points'],
            self.df['roots'],
            self.ddf['roots']
        ), 2, 0)
        

if __name__ == '__main__':
    app = QApplication([])
    screen = MainWindow()
    screen.show()
    sys.exit(app.exec_())