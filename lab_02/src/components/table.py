from PyQt5.QtWidgets import QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
    
    
# Наследуемся от QMainWindow
class Table(QWidget):
    # Переопределяем конструктор класса
    def __init__(self, data):
        # Обязательно нужно вызвать метод супер класса
        QWidget.__init__(self)
        grid_layout = QGridLayout()             # Создаём QGridLayout
        self.setLayout(grid_layout)
    
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(5)     # Устанавливаем три колонки 
        table.setRowCount(len(data))        # и одну строку в таблице
    
        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels([
            '[x(1); x(i+1)]', 
            'x\'',
            'f(x\')',
            'Количество итераций',
            'Код ошибки'
        ])
    
        # Устанавливаем всплывающие подсказки на заголовки
        table.horizontalHeaderItem(0).setToolTip('элементарный отрезок,на котором производится вычисление корня функции заданным методом')
        table.horizontalHeaderItem(1).setToolTip('Приближенное значение корня')
        table.horizontalHeaderItem(2).setToolTip('значение функции в точке корня(данная величина является вещественным числом в нормальной форме, вводится с одним значащим разрядом в мантиссе)')
        table.horizontalHeaderItem(3).setToolTip('Количество итераций')
        table.horizontalHeaderItem(4).setToolTip('числовое значение,отражающее причину невозможности определения приближенного значения корня функции на данном интервале заданным методом')
    
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignRight)
        table.horizontalHeaderItem(4).setTextAlignment(Qt.AlignRight)

        # заполняем строк
        for i in range(len(data)):
            for j in range(len(data[i])):
                table.setItem(i, j, QTableWidgetItem(data[i][j]))
    
        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()
    
        grid_layout.addWidget(table, 0, 0)   # Добавляем таблицу в сетку
    