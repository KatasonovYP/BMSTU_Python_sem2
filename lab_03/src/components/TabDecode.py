from base64 import decode
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PIL import Image

from src.imageProcess import decodeImage


class TabDecode(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parent = parent
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.initGui()
        self.initVariables()
        self.connectBtns()

    def initVariables(self):
        self.dlg = QFileDialog()
        self.filename = ''
        self.image = None  # open image
        self.width = 640

    def initGui(self):
        self.openFileBtn = QPushButton('Choose file')
        self.layout.addWidget(self.openFileBtn, 0, 0)

        self.decodeBtn = QPushButton('Decode image')
        self.layout.addWidget(self.decodeBtn, 1, 0)
        self.decodeBtn.setDisabled(True)
        
        self.output = QLabel('Decoded Text: None')
        self.layout.addWidget(self.output, 2, 0)

        self.input_image_label = QLabel()
        self.layout.addWidget(self.input_image_label, 4, 0)

    def connectBtns(self):
        self.openFileBtn.clicked.connect(lambda: self.getFilename())
        self.decodeBtn.clicked.connect(lambda: self.decodeMessage())

    def getFilename(self):
        self.filename = self.dlg.getOpenFileName(
            caption='Open image for decode',
            filter='*.bmp',
            directory='src/assets'
        )[0]
        if self.filename:
            self.image = Image.open(self.filename)
            self.openFileBtn.setText(self.filename.split('/')[-1])
            self.decodeBtn.setEnabled(True)
            self.pixmap = QPixmap(self.filename)
            self.pixmap = self.pixmap.scaledToWidth(self.width)
            self.input_image_label.setPixmap(self.pixmap)

    def decodeMessage(self):
        message = decodeImage(self.image)['message']
        self.output.setText(f'Decoded Text: {message}')
