import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class My_plot(QWidget):
    def __init__(self, data, df, ddf):
        QMainWindow.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.init_gui(data, df, ddf)
    

    def init_gui(self, data, df, ddf):
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        df_X = [point[1] for point in df]
        df_Y = [point[2] for point in df]
        ddf_X = [point[1] for point in ddf]
        ddf_Y = [point[2] for point in ddf]
            
        sc.axes.scatter(df_X, df_Y, color='orange', s=40, marker='o')
        sc.axes.scatter(ddf_X, ddf_Y, color='blue', s=40, marker='o')
        sc.axes.plot(*data)
        sc.axes.set_ylim(-6,6)
        sc.axes.set_xlim(-10,10)
        self.layout.addWidget(sc)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    screen = My_plot()
    screen.show()
    sys.exit(app.exec_())