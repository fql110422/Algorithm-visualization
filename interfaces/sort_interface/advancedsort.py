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

class AdvancedSort(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('AdvancedSort')
        self.Layout = QVBoxLayout()
        self.setLayout(self.Layout)
        #初始化数据
        self.data = []
        self.lastdata = []
        self.color = []
        self.sleeptime = 0
        #标题及按钮实例化
        self.Label = TitleLabel("进阶排序")
        self.RandomButton = PushButton("随机生成数字")
        self.backDataButton = PushButton("还原数据")
        
        self.samplesLaebl = BodyLabel(self)
        self.samplesLaebl.setText("样本数:")
        self.samplesLineEdit = LineEdit(self)
        self.samplesLineEdit.setText("20")
        
        self.sleeptimeLabel = BodyLabel(self)
        self.sleeptimeLabel.setText("延时:")
        self.sleeptimeLineEdit = LineEdit(self)
        self.sleeptimeLineEdit.setText("0.1")
        
        self.canvas = MatplotlibFigure(width=5, heigh=4, dpi=100)
        self.quickSortButton = PushButton("快速排序")
        self.mergeSortButton = PushButton("归并排序")
        self.heapSortButton = PushButton("堆排序")
        #布局
        self.hBoxLayout = QHBoxLayout()
        self.ButtonvBoxLayout = QVBoxLayout()
        self.samplesLabelhBoxLayout = QHBoxLayout()
        self.sleeptimeLabelhBoxLayout = QHBoxLayout()
        #按钮信号与槽
        self.RandomButton.clicked.connect(self.onClickedRandomButton)
        self.backDataButton.clicked.connect(self.onClickedBackDataButton)
        self.quickSortButton.clicked.connect(self.onClickedQuickSortButton)
        self.mergeSortButton.clicked.connect(self.onClickedMergeSortButton)
        self.heapSortButton.clicked.connect(self.onClickedHeapSortButton)
        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
    def initWidget(self):
        pass
    
    def initLayout(self):
        #布局初始化
        self.Layout.addWidget(self.Label)
        self.Layout.addLayout(self.hBoxLayout)
        
        self.hBoxLayout.addWidget(self.canvas)
        self.hBoxLayout.addLayout(self.ButtonvBoxLayout)
        
        self.samplesLabelhBoxLayout.addWidget(self.samplesLaebl)
        self.samplesLabelhBoxLayout.addWidget(self.samplesLineEdit)
        self.sleeptimeLabelhBoxLayout.addWidget(self.sleeptimeLabel)
        self.sleeptimeLabelhBoxLayout.addWidget(self.sleeptimeLineEdit)
        
        self.ButtonvBoxLayout.addWidget(self.RandomButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addLayout(self.samplesLabelhBoxLayout)
        self.ButtonvBoxLayout.addLayout(self.sleeptimeLabelhBoxLayout)
        self.ButtonvBoxLayout.addWidget(self.backDataButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.quickSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.mergeSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.heapSortButton,0,Qt.AlignTop)
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
        
    def onClickedBackDataButton(self):
        #回退数据
        self.color = ['darkviolet']*len(self.data)
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.lastdata)),self.lastdata,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        self.data = self.lastdata.copy()
        
    def prohibitWidget(self):
        #禁用按钮
        self.RandomButton.setEnabled(False)
        self.quickSortButton.setEnabled(False)
        self.mergeSortButton.setEnabled(False)
        self.heapSortButton.setEnabled(False)
        self.backDataButton.setEnabled(False)
        
    def enableWidget(self):
        #启用按钮
        self.darwEvent() #还原颜色
        self.RandomButton.setEnabled(True)
        self.quickSortButton.setEnabled(True)
        self.mergeSortButton.setEnabled(True)
        self.heapSortButton.setEnabled(True)
        self.backDataButton.setEnabled(True)
        
    def darwEvent(self,changeColorDir={}):
        #根据传入的字典改变颜色并刷新画布
        self.color = ['darkviolet']*len(self.data)
        for i in changeColorDir.keys():
            self.color[i] = changeColorDir[i]
        
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.data)),self.data,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        sleep(self.sleeptime)
        
    def onClickedQuickSortButton(self):
        self.prohibitWidget()
        #快速排序
        pass
        self.enableWidget()
        
    def onClickedMergeSortButton(self):
        self.prohibitWidget()
        #归并排序
        pass
        self.enableWidget()
    
    def onClickedHeapSortButton(self):
        self.prohibitWidget()
        #堆排序
        pass
        self.enableWidget()