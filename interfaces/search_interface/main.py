import typing
from collections import deque
import matplotlib
matplotlib.use('Qt5Agg')
from time import sleep
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QProcess,QSize,QPoint, QTimer
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

dir = [[-1,0],[0,-1],[0,1],[1,0]]

class SearchInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(title="搜索算法",subtitle="Search",parent=parent)
        self.setObjectName('SearchInterface')
        self.view = QWidget()
        
        self.grid = Grid(self)
        self.cardWidget = SimpleCardWidget(self)
        self.hBoxLayout = QHBoxLayout()
        self.ButtonvBoxLayout = QVBoxLayout()

        self.resetGridButton = PushButton("重置网格")
        self.resetStartAndEndButton = PushButton("重置起点和终点")
        self.BFSButton = PushButton("广度优先搜索(BFS)")
        self.DFSButton = PushButton("深度优先搜索(DFS)")
        
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
       
#------------------------------DFS----------------------------------------------------       
 
    def onclickedDFS(self):
        #深度优先搜索
        self.unableWidget()
        self.list = self.grid.getlist() #获取网格迷宫
        self.vis = [[False for _ in range(len(self.list))] for _ in range(len(self.list))]
        if self.checkifin(2) and self.checkifin(3): #检查是否设置了起点和终点
            pass
            #广度优先搜索代码
            start_i, start_j = self.findStart()
            end_i, end_j = self.findEnd()
            
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_gui_dfs)
            self.dfs_generator = self.DFS(start_i, start_j, end_i, end_j)
            self.timer.start(50)
            
        else:
            self.showMessageBox("错误", "请设置起点和终点")
        
    def update_gui_dfs(self):
        try:
            next(self.dfs_generator)
        except:
            self.timer.stop()
            self.enableWidget()
            
    def DFS(self, start_i, start_j, end_i, end_j):
        Q = deque()
        Q.append(Node(start_i, start_j, 0))
        
        while Q:
            now = Q.pop()
            for i in range(4):
                xx, yy = now.x, now.y
                while True:
                    xx += dir[i][0]
                    yy += dir[i][1]
                    if self.in_map(xx, yy):
                        if not self.vis[xx][yy] and self.list[xx][yy] != 1:
                            self.vis[xx][yy] = True
                            now.step += 1
                            Q.append(Node(xx, yy, now.step))
                            self.grid.setButtonText(xx, yy, str(now.step))
                            if self.list[xx][yy] == 3:
                                self.showMessageBox("成功", "已经走到终点")
                                return
                            elif self.list[xx][yy] == 0:
                                self.grid.setButtonColor(xx, yy, "blue")
                            yield
                            self.grid.setButtonColor(xx,yy,"yellow")
                            yield
                        else:
                            break
                    else:
                        break
        if not self.vis[end_i][end_j]:
            self.showMessageBox("失败","没有找到一条成功路径")
        
#--------------------------BFS----------------------------------------------

    def onclickedBFS(self):
        #广度优先搜索
        self.unableWidget()
        self.list = self.grid.getlist()
        self.vis = [[False for _ in range(len(self.list))] for _ in range(len(self.list))]
        if self.checkifin(2) and self.checkifin(3):
            pass
            start_i, start_j = self.findStart()
            end_i, end_j = self.findEnd()
            
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_gui_bfs)
            self.bfs_generator = self.BFS(start_i, start_j, end_i, end_j)
            self.timer.start(50)
            
        else:
            self.showMessageBox("错误", "请设置起点和终点")
    
    def update_gui_bfs(self):
        try:
            next(self.bfs_generator)
        except:
            self.timer.stop()
            self.enableWidget()
            
    
    def BFS(self, start_i, start_j, end_i, end_j):
        Q = deque()
        Q.append(Node(start_i, start_j, 0))
        self.vis[start_i][start_j] = True
        while Q:
            now = Q.popleft()
            #print(f"Step for node ({now.x}, {now.y}): {now.step}")
            x, y = now.x, now.y
            for i in range(4):
                xx, yy = x + dir[i][0], y + dir[i][1]
                if self.in_map(xx, yy):
                    if not self.vis[xx][yy] and self.list[xx][yy] != 1:
                        self.vis[xx][yy] = True
                        self.grid.setButtonText(xx, yy, str(now.step + 1))
                        if self.list[xx][yy] == 3:
                            self.showMessageBox("成功", "已经走到终点")
                            return
                        elif self.list[xx][yy] == 0:
                            self.grid.setButtonColor(xx, yy, "blue")
                        Q.append(Node(xx, yy, now.step + 1))
                        yield
                        self.grid.setButtonColor(xx,yy,"yellow")
                        yield
        if not self.vis[end_i][end_j]:
            self.showMessageBox("失败","没有找到一条成功路径")
                
    def in_map(self, x, y):
        return 0 <= x < len(self.list) and 0 <= y < len(self.list)
        
            
    def unableWidget(self):
        self.resetGridButton.setEnabled(False)
        self.resetStartAndEndButton.setEnabled(False)
        self.BFSButton.setEnabled(False)
        self.DFSButton.setEnabled(False)
        
    def enableWidget(self):
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
                
    
    
class Node:
    def __init__(self, x=0, y=0, step=0):
        self.x = x
        self.y = y
        self.step = step