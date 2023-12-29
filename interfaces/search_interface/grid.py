from collections.abc import Callable, Iterable, Mapping
import typing
from typing import Any
import win32api
import ctypes
import threading
from PyQt5 import QtCore
import matplotlib
matplotlib.use('Qt5Agg')
from time import sleep
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QProcess,QSize,QPoint
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QStackedWidget
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QSizePolicy, QMessageBox
from PyQt5.QtGui import QIcon, QCursor, QMouseEvent, QEnterEvent
from qfluentwidgets import (ScrollArea, CardWidget, SegmentedWidget, SettingCardGroup, SwitchSettingCard, 
                            FluentIcon, StrongBodyLabel, BodyLabel, ExpandLayout, ToolTipFilter, ComboBoxSettingCard, 
                            ToolTipPosition, PrimaryPushSettingCard, InfoBar, InfoBarPosition, PushButton, TitleLabel, 
                            OptionsSettingCard, HyperlinkCard, PushSettingCard,FluentWindow,FluentIcon,Theme,setTheme,
                            Action,RoundMenu,NavigationItemPosition,NavigationAvatarWidget,StrongBodyLabel,BodyLabel,
                            ToolTipFilter,TitleLabel,SplashScreen,SimpleCardWidget,Flyout,InfoBarIcon,LineEdit, MessageBox,
                            FlowLayout)

list = []

class GridItem(PushButton):
    rightClicked = pyqtSignal()
    def __init__(self, x, y, sidelength, parent=None):
        super().__init__(parent)
        global list
        self.sidelength = sidelength
        self.setFixedSize(self.sidelength, self.sidelength)
        self.x = x
        self.y = y
        
        self.color = "white"
        self.setcolor(self.color)
        
        self.clicked.connect(self.leftclick)
        self.rightClicked.connect(self.rightclick)
        
    def leftclick(self):
        #设置障碍
        self.setcolor("black")
        list[self.x][self.y] = 1
        
    def rightclick(self):
        #设置起点和终点
        if self.color == "white":
            if not self.checkifin(2):
                self.setcolor("green")
                list[self.x][self.y] = 2
            elif not self.checkifin(3):
                self.setcolor("red")
                list[self.x][self.y] = 3
            else:
                self.showMessageBox("错误", "起点和终点已经设置")
        else:
            self.setcolor("white")
            list[self.x][self.y] = 0
            self.setText(None)
            
    def checkifin(self, n):
        for i in range(len(list)):
            for j in range(len(list)):
                if list[i][j] == n:
                    return True

    def setcolor(self, color):
        #设置按钮颜色
        self.color = color
        self.setStyleSheet(
            "border: 1px solid black; "
            "background-color: {};".format(self.color)
        )
    
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        # 为右键单击事件建立信号
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
    
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        while not w.exec():
            pass

        

class Grid(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        global list
        
        self.num = 15
        self.sidelength = 500
        list = [[0 for i in range(self.num)] for j in range(self.num)]
        
        self.setFixedSize(int(self.sidelength*1.05), int(self.sidelength*1.05))
        self.flowLayout = FlowLayout()
        self.setLayout(self.flowLayout)
        self.flowLayout.setHorizontalSpacing(0)
        self.flowLayout.setVerticalSpacing(0)
        
        self.initWidget()
        
    def initWidget(self):
        for i in range(self.num):
            for j in range(self.num):
                self.flowLayout.addWidget(GridItem(i, j, int(self.sidelength/self.num), self))
        self.itemList = self.findChildren(GridItem)
                
    def resetGridItem(self):
        #将网格颜色重置
        for item in self.itemList:
            item.setcolor("white")
            item.setText(None)
            list[item.x][item.y] = 0
            
            
    def resetStartAndEnd(self):
        #将起点和终点重置
        for item in self.itemList:
            if item.color == "green" or item.color == "red" or item.color == "yellow" or item.color == "pink" or item.color == "purple":
                item.setcolor("white")
                list[item.x][item.y] = 0
                item.setText(None)
                
    def resetPassedWay(self):
        #将已经走过的路重置
        for item in self.itemList:
            if item.color == "yellow" or item.color == "pink" or item.color == "purple":
                item.setcolor("white")
                list[item.x][item.y] = 0
                item.setText(None)
    
    def setGridItem(self, changedlist):
        #设置网格颜色,传入坐标然后更改颜色
        for i in range(self.num):
            for j in range(self.num):
                idx = i*self.num+j
                if changedlist[i][j] == -1:
                    self.itemList[idx].setcolor("yellow")
                
    def getlist(self):
        return list
    
    def setButtonText(self, i, j, text = None):
        idx = self.num*i + j
        self.itemList[idx].setText(str(text))
        
    def setButtonColor(self, i, j, color):
        #sleep(0.1)
        idx = self.num*i + j
        self.itemList[idx].setcolor(color)
        
    def getButtonText(self, i, j):
        idx = self.num*i + j
        return self.itemList[idx].text()
    
    def getButtonColor(self, i, j):
        idx = self.num*i + j
        return self.itemList[idx].color