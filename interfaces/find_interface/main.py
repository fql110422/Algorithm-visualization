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
from interfaces.find_interface.grid import Grid

class FindInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(title = "查找算法", subtitle = "Find", parent = parent)
        self.setObjectName("FindInterface")
        self.view = QWidget()
        
        self.grid = Grid(self)
        self.cardWidget = SimpleCardWidget(self)
        self.cardVBoxLayout = QVBoxLayout()
        
        self.resetButton = PushButton("重置",self)
        self.sortrandomButton = PushButton("随机生成数字",self)
        
        self.resetButton.clicked.connect(self.grid.resetGridItem)
        self.sortrandomButton.clicked.connect(self.onClickedsortrandomButton)
        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
    def initWidget(self):
        self.cardWidget.setFixedHeight(500)
    
    def initLayout(self):
        self.vBoxLayout.addWidget(self.cardWidget, 0, Qt.AlignTop)
        self.cardWidget.setLayout(self.cardVBoxLayout)
        
        self.cardVBoxLayout.addWidget(self.grid, 0, Qt.AlignTop)
        self.cardVBoxLayout.addStretch(1)
        self.cardVBoxLayout.addWidget(self.resetButton, 0, Qt.AlignTop)
        self.cardVBoxLayout.addWidget(self.sortrandomButton, 0, Qt.AlignTop)
        
    
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )
        
    def onClickedsortrandomButton(self):
        self.data = []
        for i in range(21):
            self.data.append(random.randint(1,100))
        self.data.sort()
        for i in range(21):
            self.grid.setButtonText(i,self.data[i])