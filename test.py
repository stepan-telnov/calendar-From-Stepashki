from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from datetime import datetime
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Часы")

        # Создаем метку для отображения времени
        self.time_label = QLabel(self)
        self.time_label.setText("HH:MM")
        self.time_label.setGeometry(50, 50, 100, 30)  # Задаем размеры метки

        # Таймер для обновления времени
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Обновляем каждую секунду

        self.update_time()  # Обновляем сразу при запуске

    def update_time(self):
        # Получаем текущее время в формате "HH:MM"
        current_time = datetime.now().strftime("%H:%M")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()