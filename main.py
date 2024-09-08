import os

from PyQt5.QtCore import Qt

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("style.css")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMaximizeButtonHint)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec_())
