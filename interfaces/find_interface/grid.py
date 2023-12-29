import typing
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
from PyQt5.QtGui import QIcon, QCursor
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
        self.is_choosed = False
        
        self.color = "white"
        self.setcolor(self.color)
        self.rightClicked.connect(self.rightclick)
        
    def rightclick(self):
        #设置要查找的数
        if not 1 in list:
            if self.x != 1:
                pass
            else:
                self.setcolor("red")
                list[self.y] = 1
        else:
            self.showMessageBox("错误", "要查找的数已设置")
            
    def setcolor(self, color):
        #设置按钮颜色
        self.color = color
        if self.x == 1:
            self.setStyleSheet(
                "border: 1px solid black; "
                "background-color: {};".format(self.color)
            )
        else:
            self.setStyleSheet(
                "border: 0px solid black; "
                "background-color: white;"
            )
           
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        while not w.exec():
            pass
    
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        # 为右键单击事件建立信号
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()

    def setButtonIcon(self, state = False):
        if state:
            self.setIcon(FluentIcon.UP)
        else:
            self.setIcon(None)


class Grid(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        global list
        
        self.col = 3
        self.num = 21
        self.sidelength = 700
        list = [0 for i in range(self.num)]
        
        self.setFixedSize(int(self.sidelength*1.05), int(self.sidelength/self.num*3.5))
        self.flowLayout = FlowLayout()
        self.setLayout(self.flowLayout)
        self.flowLayout.setHorizontalSpacing(0)
        self.flowLayout.setVerticalSpacing(0)
        
        self.initWidget()
        
    def initWidget(self):
        for i in range(self.col):
            for j in range(self.num):
                self.flowLayout.addWidget(GridItem(i, j, int(self.sidelength/self.num), self))
        self.itemList = self.findChildren(GridItem)
                
    def resetGridItem(self):
        #将网格重置
        for item in self.itemList:
            item.setcolor("white")
            list[item.y] = 0
            item.setIcon(None)
    
    def setGridItem(self, changedlist):
        #设置网格颜色,传入坐标然后更改颜色
        for i in range(self.col):
            for j in range(self.num):
                idx = i*self.col+j
                if changedlist[idx] == -1:
                    self.itemList[idx].setcolor("yellow")
                
    def getlist(self):
        return list
    
    def getTarget(self):
        for i in range(len(list)):
            if list[i] == 1:
                return i
        return -1
    
    def setArrowhead(self, j, state = True):
        # 设置箭头显示
        idx = 2*self.num + j
        self.itemList[idx].setButtonIcon(state)
        
    def setButtonText(self, j, text = None):
        # 设置按钮文本
        idx = self.num + j
        self.itemList[idx].setText(str(text))
        
    def setButtonColor(self, j, color = None):
        # 设置按钮颜色
        idx = self.num + j
        self.itemList[idx].setcolor(color)
        