import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPainterPath, QColor
from PyQt5.QtCore import QRectF
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Квадрат с закруглением")
        self.setGeometry(100, 100, 400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)

        # Создаем путь для рисования квадрата с закруглением внизу справа
        path = QPainterPath()

        # Размер и позиция квадрата
        rect = QRectF(50, 50, 200, 200)

        # Добавляем линии для сторон квадрата
        path.moveTo(rect.topLeft())
        path.lineTo(rect.topRight())

        # Закругляем нижний правый угол
        corner_radius = 50
        path.lineTo(rect.right(), rect.bottom() - corner_radius)
        path.arcTo(
            rect.right() - 2 * corner_radius,
            rect.bottom() - 2 * corner_radius,
            2 * corner_radius,
            2 * corner_radius,
            0,
            -90
        )

        # Завершаем путь до нижнего левого угла
        path.lineTo(rect.bottomLeft())
        path.lineTo(rect.topLeft())

        # Рисуем путь
        painter.setBrush(QColor("lightblue"))
        painter.drawPath(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())