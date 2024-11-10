import os
import socket
import subprocess
import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRectF, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPainterPath

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\Админ\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt5\Qt5\plugins\platforms'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class CalendarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window
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
        self.states = 1 # 1: Main     2: Calendar    3:

        #style_CSS
        with open("style.css") as style:
            css = style.read()
        self.setStyleSheet(css)

        #Btns================================================================================================Btns

        #Btn_Exit
        self.btnExit = QPushButton(parent = self, text ="⨉")
        self.btnExit.setObjectName("newbtn")
        self.btnExit.setGeometry(self.widthWindow - 25, 8, 20, 20)
        self.btnExit.clicked.connect(self.close)

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

        # Btns================================================================================================Btns


        # lobis==============================================================================================lobis

        # Hi_menu
        self.text_hi = QLabel(parent=self, text=f"Hi {socket.gethostname()}")
        self.text_hi.setObjectName("text_hi")
        self.text_hi.setGeometry(self.widthWindow // 2 - len(self.text_hi.text()) * 2, self.heightWindow // 2 - 150, 300, 100)

        # Calendar_menu
        now = datetime.datetime.now()

        curTime = now.strftime("%H:%M")
        dayNow = now.strftime("%d")

        year = now.strftime("%Y")
        dayWeek = now.strftime("%A")

        self.text_CurTime_DayNow = QLabel(parent=self, text=f"{curTime} {dayNow}")
        self.text_Year_DayWeek = QLabel(parent=self, text=f"{year} {dayWeek}")

        self.text_CurTime_DayNow.setObjectName("text_CurTime_DayNow")
        self.text_Year_DayWeek.setObjectName("text_Year_DayWeek")

        #ToDo: не работает кнопка крестик, время не идет, размеры скачут, и впереди собака -> @

        self.text_CurTime_DayNow.setGeometry(self.widthWindow // 2 - 140, self.heightWindow // 2 - 190, 300, 100)
        self.text_Year_DayWeek.setGeometry(self.widthWindow // 2 + 140, self.heightWindow // 2 - 190, 300, 100)

        # lobis==============================================================================================lobis

    def updateStates(self, num=1):
        self.states = num
        self.hideLobis()

    def hideLobis(self):
        if self.states == 1:
            self.btnEditName.show()
            self.text_hi.show()

        if self.states == 2:
            self.btnEditName.hide()
            self.text_hi.hide()


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
        path2.arcTo(rectf2.right() - 20, rectf2.top(), 20, 20, 0, 90)
        path2.arcTo(rectf2.left(), rectf2.top(), 20, 20, 90, 90)

        painter.drawPath(path2)


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