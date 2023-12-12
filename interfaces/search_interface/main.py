import typing
import matplotlib
matplotlib.use('Qt5Agg')
from time import sleep
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QProcess,QSize,QPoint
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QStackedWidget
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QSizePolicy
from PyQt5.QtGui import QIcon, QCursor
from qfluentwidgets import (ScrollArea, CardWidget, SegmentedWidget, SettingCardGroup, SwitchSettingCard, 
                            FluentIcon, StrongBodyLabel, BodyLabel, ExpandLayout, ToolTipFilter, ComboBoxSettingCard, 
                            ToolTipPosition, PrimaryPushSettingCard, InfoBar, InfoBarPosition, PushButton, TitleLabel, 
                            OptionsSettingCard, HyperlinkCard, PushSettingCard,FluentWindow,FluentIcon,Theme,setTheme,
                            Action,RoundMenu,NavigationItemPosition,NavigationAvatarWidget,StrongBodyLabel,BodyLabel,
                            ToolTipFilter,TitleLabel,SplashScreen,SimpleCardWidget,Flyout,InfoBarIcon,LineEdit, MessageBox)

from interfaces.gallery_interface.main import GalleryInterface
from interfaces.search_interface.grid import Grid

class SearchInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(title="搜索算法",subtitle="Search",parent=parent)
        self.setObjectName('SearchInterface')
        self.view = QWidget()
        
        self.grid = Grid(self)
        self.cardWidget = SimpleCardWidget(self)
        self.hBoxLayout = QHBoxLayout()
        self.ButtonvBoxLayout = QVBoxLayout()

        self.resetGridButton = PushButton("重置网格", self)
        self.resetStartAndEndButton = PushButton("重置起点和终点", self)
        self.BFSButton = PushButton("广度优先搜索(BFS)", self)
        self.DFSButton = PushButton("深度优先搜索(DFS)", self)
        
        self.resetGridButton.clicked.connect(self.grid.resetGridItem)
        self.resetStartAndEndButton.clicked.connect(self.grid.resetStartAndEnd)
        self.BFSButton.clicked.connect(self.onclickedBFS)
        self.DFSButton.clicked.connect(self.onclickedDFS)
        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
    def initWidget(self):
        pass
    
    def initLayout(self):
        self.vBoxLayout.addWidget(self.cardWidget)
        self.cardWidget.setLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.grid, 0, Qt.AlignLeft)
        self.hBoxLayout.addLayout(self.ButtonvBoxLayout)
        
        self.ButtonvBoxLayout.addWidget(self.resetGridButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.resetStartAndEndButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.BFSButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.DFSButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addStretch(1)
    
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )
        
    def onclickedBFS(self):
        #广度优先搜索
        self.unableButton()
        self.list = self.grid.returnlist() #获取网格迷宫
        if self.checkifin(2) and self.checkifin(3): #检查是否设置了起点和终点
            pass
            #广度优先搜索代码
            start = self.findStart()
            end = self.findEnd()
            
            
        else:
            self.showMessageBox("错误", "请设置起点和终点")
        self.enableButton()
        
    def onclickedDFS(self):
        #深度优先搜索
        self.unableButton()
        self.list = self.grid.returnlist()
        if self.checkifin(2) and self.checkifin(3):
            pass
            start = self.findStart()
            end = self.findEnd()
            
            
        else:
            self.showMessageBox("错误", "请设置起点和终点")
        self.enableButton()
            
    def unableButton(self):
        self.resetGridButton.setEnabled(False)
        self.resetStartAndEndButton.setEnabled(False)
        self.BFSButton.setEnabled(False)
        self.DFSButton.setEnabled(False)
        
    def enableButton(self):
        self.resetGridButton.setEnabled(True)
        self.resetStartAndEndButton.setEnabled(True)
        self.BFSButton.setEnabled(True)
        self.DFSButton.setEnabled(True)
    
    def checkifin(self, n):
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i][j] == n:
                    return True
    
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        while not w.exec():
            pass
        
    def findStart(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i][j] == 2:
                    return i, j
                
    def findEnd(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i][j] == 3:
                    return i, j