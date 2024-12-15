import os
import socket
import subprocess
import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QRectF, QPoint, QTimer
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPainterPath

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QColorDialog


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window
        try:
            self.setWindowTitle(" ")
            self.widthWindow = 600
            self.heightWindow = 400
            self.setGeometry(1500, 100, self.widthWindow, self.heightWindow)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
            self.setWindowOpacity(0.9)
            self.oldPos = None
            self.heightGrabBorder = 0
            self.widthGrabBorder = 0
            """
            1 - main
            2 - calendar
            3 - timer
            -1 - settings
            -2 - settings -> change color
            """
            self.states = 1 # 1: Main     2: Calendar    3:

            #style_CSS
            with open("style.css") as style:
                css = style.read()
            self.setStyleSheet(css)

            #Btns================================================================================================Btns

            self.widg = QWidget()
            self.widg.setGeometry(100, 300, 100, 300)
            self.setStyleSheet("""
            QWidget {
                background-color: #3498db; /* Синий цвет фона */
                border: 2px solid #2980b9; /* Тёмно-синий цвет рамки */
                border-radius: 0px; /* Без закруглений */
            }
        """)

            #Btn_Exit
            self.btnExit = QPushButton(parent = self, text ="⨉")
            self.btnExit.setObjectName("newbtn")
            self.btnExit.setGeometry(self.widthWindow - 25, 8, 20, 20)
            self.btnExit.clicked.connect(self.close)

            # Btn_Options
            self.btnOp = QPushButton(parent=self, text="⚙️")
            self.btnOp.setObjectName("op_btn")
            self.btnOp.setGeometry(10, self.heightWindow - 30, 20, 20)
            self.btnOp.clicked.connect(lambda:self.updateStates(-1))

            #Btn_Main_menu
            self.btnMain = QPushButton(parent=self, text="Home")
            self.btnMain.setObjectName("home_btn")
            self.btnMain.setGeometry(0, 35, 150, 30)
            self.btnMain.clicked.connect(lambda:self.updateStates(1))

            # Btn_rename_nhame228
            self.btnEditName = QPushButton(parent=self, text="Edit name")
            self.btnEditName.setObjectName("btnEditName")
            self.btnEditName.setGeometry((self.widthWindow + 150) // 2 - 40, self.heightWindow - 50, 90, 40)
            self.btnEditName.clicked.connect(self.openWindows_Microsoft_System)

            # Btn_Calendar_menu
            self.btnCalendar = QPushButton(parent=self, text="Calendar")
            self.btnCalendar.setObjectName("calendar_btn")
            self.btnCalendar.setGeometry(0, 65, 150, 30)
            self.btnCalendar.clicked.connect(lambda:self.updateStates(2))

            # Btn_Timer_menu
            self.btnTimer = QPushButton(parent=self, text="Timer")
            self.btnTimer.setObjectName("home_btn")
            self.btnTimer.setGeometry(0, 95, 150, 30)
            self.btnTimer.clicked.connect(lambda: self.updateStates(3))


            # --------------------- Settings --------------------- #

            self.btnChangeColor = QPushButton(parent=self, text="Colors")
            self.btnChangeColor.setObjectName("home_btn")
            self.btnChangeColor.setGeometry(0, 35, 150, 30)
            self.btnChangeColor.clicked.connect(lambda:self.updateStates(-2))

            # ------- Buttons in "Colors" ------- #

            # Change background
            self.btnChangeBackground = QPushButton(parent=self, text="Change background")
            self.btnChangeBackground.setObjectName("home_btn")
            self.btnChangeBackground.setGeometry(150, 35, 150, 30)
            # self.btnChangeBackground.clicked.connect()

            # Change foreground
            self.btnChangeForeground = QPushButton(parent=self, text="Change foreground")
            self.btnChangeForeground.setObjectName("home_btn")
            self.btnChangeForeground.setGeometry(300, 35, 150, 30)
            # self.btnChangeBackground.clicked.connect()


            # Button "Kek"
            self.btnKek = QPushButton(parent=self, text="Kek")
            self.btnKek.setObjectName("calendar_btn")
            self.btnKek.setGeometry(0, 65, 150, 30)
            # self.btnCalendar.clicked.connect(lambda:self.updateStates(2))

            # Btns================================================================================================Btns


            # lobis==============================================================================================lobis

            # Hi_menu
            self.text_hi = QLabel(parent=self, text=f"Hi {socket.gethostname()}")
            self.text_hi.setObjectName("text_hi")
            self.text_hi.setGeometry(self.widthWindow // 2 - len(self.text_hi.text()) * 2, self.heightWindow // 2 - 150, 300, 100)

            # Calendar_menu
            #curTime = now.strftime("%H:%M")
            #dayNow = now.strftime("%d")     <- это стиреть но инфа важна

            #year = now.strftime("%Y")
            #dayWeek = now.strftime("%A")

            self.text_CurTime_DayNow = QLabel(parent=self, text=f"")
            self.text_Year_DayWeek = QLabel(parent=self, text=f"")

            self.text_CurTime_DayNow.hide()
            self.text_Year_DayWeek.hide()

            self.text_CurTime_DayNow.setObjectName("text_CurTime_DayNow")
            self.text_Year_DayWeek.setObjectName("text_Year_DayWeek")

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)

            self.update_time()

            #ToDo: не работает кнопка крестик, время не идет, размеры скачут, и впереди собака -> @

            self.text_CurTime_DayNow.setGeometry(self.widthWindow // 2 - 140, self.heightWindow // 2 - 190, 300, 100)
            self.text_Year_DayWeek.setGeometry(self.widthWindow // 2 + 140, self.heightWindow // 2 - 190, 300, 100)

            #Timer_menu
            self.text_riadMy_Timer = QLabel(parent=self, text=f"choose the time")
            self.text_riadMy_Timer.setObjectName("text_riadMy_Timer")
            self.text_riadMy_Timer.setGeometry(self.widthWindow // 2 - 50, self.heightWindow // 2 - 180, 700, 150)

            # lobis==============================================================================================lobis
            self.updateStates()
        except Exception as err:
            print(err)

        self.setStyleSheet("""
                    QPainter {
                        background-color: #2ecc71;
                        border: 2px solid #27ae60;
                        border-radius: 25px;
                    }
                """)

    def updateStates(self, num=1):
        self.states = num
        self.hideLobis()

    def hideLobis(self):

        if self.states == -2:
            pass

        if self.states == -1:
            self.btnChangeColor.show()
            self.btnKek.show()

            self.btnTimer.hide()
            self.btnCalendar.hide()
            self.btnMain.hide()

            self.btnEditName.hide()
            self.text_hi.hide()
            self.text_CurTime_DayNow.hide()
            self.text_Year_DayWeek.hide()
            self.text_riadMy_Timer.hide()

            # calafulWindow = QColorDialog.getColor()

            # if calafulWindow.isValid():
            #     self.setStyleSheet(f"background-color: {calafulWindow.name()};")

        if self.states == 1:
            self.btnEditName.show()
            self.text_hi.show()
            self.text_CurTime_DayNow.hide()
            self.text_Year_DayWeek.hide()
            self.text_riadMy_Timer.hide()
            self.btnChangeColor.hide()
            self.btnKek.hide()

        if self.states == 2:
            self.text_CurTime_DayNow.show()
            self.text_Year_DayWeek.show()
            self.btnEditName.hide()
            self.text_hi.hide()
            self.text_riadMy_Timer.hide()

        if self.states == 3:
            self.text_CurTime_DayNow.hide()
            self.text_Year_DayWeek.hide()
            self.btnEditName.hide()
            self.text_hi.hide()
            self.text_riadMy_Timer.show()



    def openWindows_Microsoft_System(self):
        subprocess.run(['control', '/name', 'Microsoft.System'])

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
        rectf2 = QRectF(0, 32, 150, self.heightWindow)
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


        #leftBorderMainSuperPuperOmega+version1000000000-300Menu
        path2 = QPainterPath()
        path2.moveTo(rectf2.topLeft())
        path2.lineTo(rectf2.bottomLeft())
        path2.lineTo(rectf2.bottomRight())
        path2.lineTo(rectf2.topRight())
        #path2.arcTo(rectf2.right() - 20, rectf2.top(), 20, 20, 0, 90)
        #path2.arcTo(rectf2.left(), rectf2.top(), 20, 20, 90, 90)

        painter.drawPath(path2)


    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        current_year = datetime.datetime.now().strftime("%Y %A")
        self.text_CurTime_DayNow.setText(current_time)
        self.text_Year_DayWeek.setText(current_year)


    def mousePressEvent(self, event):
        self.oldPos:QPoint = event.globalPos()


    def mouseMoveEvent(self, event):
        if 0 <= event.x() <= self.widthWindow and 0 <= event.y() <= 32:
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = CalendarWindow()
    window.show()
    sys.exit(app.exec_())
