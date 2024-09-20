import os

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPainterPath

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window
        self.setWindowTitle(" ")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowOpacity(0.9)

        #style_CSS
        with open("style.css") as style:
            css = style.read()
        self.setStyleSheet(css)

        #Btn_Exit
        self.test = QPushButton(parent = self, text = "⨉")
        self.test.setObjectName("newbtn")
        self.test.setGeometry(575, 8, 20, 20)
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
        rectf = QRectF(0.0, 0.0, 600.0, 35.0)
        #painter.drawRoundedRect(rectf, 10, 10)

        #colorBorder
        path = QPainterPath()
        path.moveTo(rectf.topLeft())
        path.lineTo(rectf.bottomLeft())
        path.lineTo(rectf.bottomRight())
        path.lineTo(rectf.topRight())
        path.arcTo(rectf.right() - 20, rectf.top(), 20, 20, 0, 90)
        path.lineTo(rectf.left(), rectf.top())

        painter.drawPath(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec_())
