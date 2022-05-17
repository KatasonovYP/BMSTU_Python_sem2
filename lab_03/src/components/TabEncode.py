from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PIL import Image

from src.imageProcess import encodeImage


class TabEncode(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parent = parent
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.initVariables()
        self.initGui()
        self.connectBtns()

    def initVariables(self):
        self.dlg = QFileDialog()
        self.filename = ''
        self.image = None
        self.width = 640

    def initGui(self):
        self.setWindowTitle('Coding Image')

        self.input = QLineEdit('decode text')
        self.layout.addWidget(self.input, 0, 0)

        self.openFileBtn = QPushButton('Choose file')
        self.layout.addWidget(self.openFileBtn, 1, 0)
        self.EncodeBtn = QPushButton('Encode image')
        self.layout.addWidget(self.EncodeBtn, 2, 0)
        self.EncodeBtn.setDisabled(True)

        self.saveFileBtn = QPushButton('save file')
        self.layout.addWidget(self.saveFileBtn, 3, 0)
        self.saveFileBtn.setDisabled(True)
        
        # create label for image
        self.input_image_label = QLabel()
        self.layout.addWidget(self.input_image_label, 4, 0)

    def connectBtns(self):
        self.openFileBtn.clicked.connect(lambda: self.getFilename())
        self.saveFileBtn.clicked.connect(lambda: self.saveFile())
        self.EncodeBtn.clicked.connect(lambda: self.encodeMessage())

    def getFilename(self):
        self.filename = self.dlg.getOpenFileName(
            caption='Open image for encode',
            filter='*.bmp',
            directory='src/assets'
        )[0]
        if self.filename:
            self.image = Image.open(self.filename)
            self.openFileBtn.setText(self.filename.split('/')[-1])
            self.EncodeBtn.setEnabled(True)
            self.pixmap = QPixmap(self.filename)
            self.pixmap = self.pixmap.scaledToWidth(self.width)
            # show image on UI
            self.input_image_label.setPixmap(self.pixmap)

    def encodeMessage(self):
        message = self.input.text()
        encoded = encodeImage(self.image, message)
        if encoded['code'] == 0:
            self.image = encoded['image']
            self.saveFileBtn.setEnabled(True)

    def saveFile(self):
        filename = self.dlg.getSaveFileName(
            caption='Save encoded image',
            filter='*.bmp',
            directory='src/assets'
        )[0]
        if not filename:
            filename = 'untitled'
        filename = f'{filename.split(".")[0]}.bmp'
        self.image.save(filename, 'bmp')
