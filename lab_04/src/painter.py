from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from itertools import permutations

from src.triangle import findMaxAngle


class Paint(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 300)
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

        # Закрасить фон холстаы
        self.drawBrushes(painter)

        # Рисование точки
        for point in self.points:
            painter.drawEllipse(*point, 2, 2)

        # Если искомый треугольник существует, рисуем его
        painter.setPen(QPen(Qt.red, 1.0))
        try:
            self.drawBestTriangle(painter)
        except:
            pass

    def drawBestTriangle(self, painter):
        maxAngle = 0
        bestPoints = ()
        for a, b, c in permutations(self.points, r=3):
            tmp = findMaxAngle(a, b, c)
            if tmp > maxAngle:
                maxAngle = tmp
                bestPoints = (a, b, c)
        self.drawTriangle(bestPoints, painter)

    
    def drawTriangle(self, points, painter):
        a, b, c = points
        painter.drawLine(*a, *b)
        painter.drawLine(*a, *c)
        painter.drawLine(*b, *c)




    def drawBrushes(self, qp):
        '''Закрасить фон холста'''
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(255, 255, 255))
        qp.setBrush(brush)
        qp.drawRect(-10, -10, 1000, 1000)