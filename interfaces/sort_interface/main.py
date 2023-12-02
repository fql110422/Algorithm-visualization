import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QProcess,QSize,QPoint
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QStackedWidget
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QSizePolicy
from PyQt5.QtGui import QIcon, QCursor
from qfluentwidgets import (ScrollArea, CardWidget, SegmentedWidget, SettingCardGroup, SwitchSettingCard, 
                            FluentIcon, StrongBodyLabel, BodyLabel, ExpandLayout, ToolTipFilter, ComboBoxSettingCard, 
                            ToolTipPosition, PrimaryPushSettingCard, InfoBar, InfoBarPosition, PushButton, TitleLabel, 
                            OptionsSettingCard, HyperlinkCard, PushSettingCard,FluentWindow,FluentIcon,Theme,setTheme,
                            Action,RoundMenu,NavigationItemPosition,NavigationAvatarWidget,StrongBodyLabel,BodyLabel,
                            ToolTipFilter,TitleLabel,SplashScreen)

from interfaces.gallery_interface.main import GalleryInterface
from interfaces.sort_interface.matplotlibfigure import MatplotlibFigure
from interfaces.sort_interface.easysort import EasySort

class SortInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(title="排序",subtitle="Sort",parent=parent)
        self.setObjectName('SortInterface')
        self.view = QWidget()

        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
    def initWidget(self):
        self.easySort = EasySort(self)
    
    def initLayout(self):
        self.vBoxLayout.addWidget(self.easySort)
        
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )