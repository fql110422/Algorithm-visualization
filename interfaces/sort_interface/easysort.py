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
                            ToolTipFilter,TitleLabel,SplashScreen,SimpleCardWidget,Flyout,InfoBarIcon,LineEdit)

from interfaces.sort_interface.matplotlibfigure import MatplotlibFigure

class EasySort(SimpleCardWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setObjectName('EasySort')
        self.Layout = QVBoxLayout()
        self.setLayout(self.Layout)
        
        self.data = []
        self.lastdata = []
        self.color = []
        self.sleeptime = 0
        
        self.hBoxLayout = QHBoxLayout()
        self.Label = TitleLabel("简单排序")
        self.RandomButton = PushButton("随机生成数字")
        self.samplesLineEdit = LineEdit(self)
        self.samplesLineEdit.setText("20")
        self.sleeptimeLineEdit = LineEdit(self)
        self.sleeptimeLineEdit.setText("0.5")
        self.backDataButton = PushButton("还原数据")
        self.SelectionSortButton = PushButton("选择排序")
        self.BubbleSortButton = PushButton("冒泡排序")
        self.ButtonvBoxLayout = QVBoxLayout()
        self.canvas = MatplotlibFigure(width=5, heigh=4, dpi=100)
        
        self.RandomButton.clicked.connect(self.onClickedRandomButton)
        self.BubbleSortButton.clicked.connect(self.onClickedBubbleSortButton)
        self.SelectionSortButton.clicked.connect(self.onClickedSelectionSortButton)
        self.backDataButton.clicked.connect(self.onClickedBackDataButton)
        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
        
    def initWidget(self):
        pass
    
    def initLayout(self):
        self.Layout.addWidget(self.Label)
        self.Layout.addLayout(self.hBoxLayout)
        
        self.hBoxLayout.addWidget(self.canvas)
        self.hBoxLayout.addLayout(self.ButtonvBoxLayout)
        
        self.ButtonvBoxLayout.addWidget(self.RandomButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.samplesLineEdit,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.sleeptimeLineEdit,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.backDataButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.SelectionSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.BubbleSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addStretch(1)
        
        
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )
        
    def onClickedRandomButton(self):
        #随机生成一个数组,并绘制
        self.data = []
        num = int(self.samplesLineEdit.text())
        for i in range(num):
            self.data.append(random.randint(1,100))
        self.lastdata = self.data.copy()
        self.color = ['darkviolet']*len(self.data)
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.data)),self.data,color=self.color)
        self.canvas.draw()
        
    def onClickedBubbleSortButton(self):
        #冒泡排序
        self.prohibitWidget()
        self.sleeptime = float(self.sleeptimeLineEdit.text())
        if not len(self.data) == 0:
            for i in range(len(self.data)):
                for j in range(len(self.data)-i-1):
                    self.color = ['darkviolet']*len(self.data)
                    self.color[j] = 'green'
                    self.color[j+1] = 'red'
                    self.darwEvent()
                    sleep(self.sleeptime)
                    if self.data[j] > self.data[j+1]:
                        self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
                        self.color[j] = 'red'
                        self.color[j+1] = 'green'
                        self.darwEvent()
                        sleep(self.sleeptime)
                    
        self.enableWidget()
                        
    def onClickedSelectionSortButton(self):
        #选择排序
        self.prohibitWidget()
        self.sleeptime = float(self.sleeptimeLineEdit.text())
        if not len(self.data) == 0:
            for i in range(len(self.data)):
                minIndex = i
                self.color = ['darkviolet']*len(self.data)
                self.color[minIndex] = 'green'
                self.darwEvent()
                sleep(self.sleeptime)
                for j in range(i+1,len(self.data)):
                    self.color = ['darkviolet']*len(self.data)
                    self.color[minIndex] = 'green'
                    self.color[j] = 'red'
                    self.darwEvent()
                    sleep(self.sleeptime)
                    if self.data[j] < self.data[minIndex]:
                        minIndex = j
                self.data[i],self.data[minIndex] = self.data[minIndex],self.data[i]
                self.color[i] = 'red'
                self.color[minIndex] = 'green'
                self.darwEvent()
                sleep(self.sleeptime)
        self.enableWidget()
        
    def onClickedBackDataButton(self):
        #回退数据
        self.color = ['darkviolet']*len(self.data)
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.lastdata)),self.lastdata,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        self.data = self.lastdata.copy()
        
    def prohibitWidget(self):
        self.RandomButton.setEnabled(False)
        self.SelectionSortButton.setEnabled(False)
        self.BubbleSortButton.setEnabled(False)
        self.backDataButton.setEnabled(False)
        
    def enableWidget(self):
        self.RandomButton.setEnabled(True)
        self.SelectionSortButton.setEnabled(True)
        self.BubbleSortButton.setEnabled(True)
        self.backDataButton.setEnabled(True)
        
    def darwEvent(self):
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.data)),self.data,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        
        
        