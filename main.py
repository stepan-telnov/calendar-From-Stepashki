import os

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRectF, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPainterPath

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window
        self.setWindowTitle(" ")
        self.widthWindow = 600
        self.heightWindow = 400
        self.setGeometry(100, 100, self.widthWindow, self.heightWindow)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)
        self.oldPos = None
        self.heightGrabBorder = 0
        self.widthGrabBorder = 0

        #style_CSS
        with open("style.css") as style:
            css = style.read()
        self.setStyleSheet(css)

        #Btn_Exit
        self.test = QPushButton(parent = self, text = "⨉")
        self.test.setObjectName("newbtn")
        self.test.setGeometry(self.widthWindow - 25, 8, 20, 20)
        self.test.clicked.connect(self.close)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rounded_rect = self.rect().adjusted(0, 0, -1, -1)
        painter.setBrush(QBrush(QColor("#454545")))
        painter.setPen(QPen(Qt.NoPen))
        painter.drawRoundedRect(rounded_rect, 10, 10)

        #grabBorder
        painter.setBrush(QBrush(QColor("#222222")))
        rectf = QRectF(0.0, 0.0, self.widthWindow, 35.0)
        self.widthGrabBorder = rectf.width()
        self.heightGrabBorder = rectf.height()
        print(self.widthGrabBorder, self.heightGrabBorder)
        #painter.drawRoundedRect(rectf, 10, 10)

        #colorGrabBorder
        path = QPainterPath()
        path.moveTo(rectf.topLeft())
        path.lineTo(rectf.bottomLeft())
        path.lineTo(rectf.bottomRight())
        path.lineTo(rectf.topRight())
        path.arcTo(rectf.right() - 20, rectf.top(), 20, 20, 0, 90)
        path.arcTo(rectf.left(), rectf.top(), 20, 20, 90, 90)

        painter.drawPath(path)

    def mousePressEvent(self, event):
        self.oldPos:QPoint = event.globalPos()


    def mouseMoveEvent(self, event):
        print(event.globalPos())
        delta = QPoint (event.globalPos() - self.oldPos)    # todo: остановились здесь, нужно вместо глобалПос вставить коорды квадрата
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec_())