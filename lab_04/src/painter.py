from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Paint(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 300)
        self.setMinimumSize(700, 300)
        self.ansTriangle = None
        self.points = []
    
    def addPoint(self, x, y):
        self.points.append((x, y))
        self.update()

    def mousePressEvent(self, event):
        '''При нажатии клавиши добавляем в массив точку
        и перерисовываем весь холст
        '''
        self.points.append((event.x(), event.y()))
        self.update()

    def mouseReleaseEvent(self, event): ...

    def paintEvent(self, event):
        '''Отрисовка всех фигур на холсте.
        вызывается при методе update()
        '''
        # Инициализация холста и кисти
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5.0))

        self.drawBrushes(painter)

        # Рисование точки

        for point in self.points:
            painter.drawEllipse(*point, 2, 2)

        # Если искомый треугольник существует, рисуем его
        if self.ansTriangle is not None:
            self.paintTriangle(painter, self.ansTriangle)

    def drawBrushes(self, qp):
        '''Закрасить фон холста'''
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(255, 255, 255))
        qp.setBrush(brush)
        qp.drawRect(-10, -10, 1000, 1000)