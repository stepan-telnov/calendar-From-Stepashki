import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter, QBrush, QPen
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'


class RoundedWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Окно с округленными рамками")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)  # удаляем системную рамку
        self.setGeometry(100, 100, 500, 400)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)  # удаляем фон
        #self.setStyleSheet("background-color: #303030;")

        self.show()

    # \/рисуем окно\/#
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rounded_rect = self.rect().adjusted(0, 0, -1, -1)
        painter.setBrush(QBrush(QColor("#303030")))
        painter.setPen(QPen(Qt.PenStyle.NoPen))
        painter.drawRoundedRect(rounded_rect, 10, 10)
    # /\рисуем окно/\


if __name__ == "__main__":
    app = QApplication(sys.argv)
    roundedWindow = RoundedWindow()
    roundedWindow.show()
    sys.exit(app.exec())