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
                            ToolTipFilter,TitleLabel,SplashScreen,SimpleCardWidget,Flyout,InfoBarIcon,LineEdit, MessageBox,
                            FlowLayout)

from interfaces.gallery_interface.main import GalleryInterface
from interfaces.home_interface.sample_card import SampleCardView
from interfaces.home_interface.style_sheet import StyleSheet

class HomeInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__("主页", "Home", parent)
        self.setObjectName('HomeInterface')
        self.view = QWidget()


        self.initWidget()
        self.initLayout()
        self.initStyle()
        self.loadSamples()
        
    def loadSamples(self):
        cardView = SampleCardView("算法目录", self.view)
        cardView.addSampleCard(
            icon=FluentIcon.UNIT,
            title="排序算法",
            content="排序算法是计算机程序中最基本的算法之一，它的功能是对一组数据按照指定的顺序进行排列。",
            routeKey="SortInterface",
            index=0
        )
        cardView.addSampleCard(
            icon=FluentIcon.IOT,
            title="搜索算法",
            content="包含广度优先搜索(BFS)和深度优先搜索(DFS)。",
            routeKey="SearchInterface",
            index=1
        )
        self.vBoxLayout.addWidget(cardView, 0, Qt.AlignTop)
        self.vBoxLayout.addStretch(1)
        
    def initWidget(self):
        StyleSheet.HOME_INTERFACE.apply(self)
    
    def initLayout(self):
        pass
    
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )