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

class MatplotlibFigure(FigureCanvas):
    def __init__(self, width=10, heigh=10, dpi=100):
        plt.rcParams['figure.facecolor'] = 'w' # 设置窗体颜色
        plt.rcParams['axes.facecolor'] = 'w' # 设置绘图区颜色
        self.figs = Figure(figsize=(width, heigh), dpi=dpi)
        super(MatplotlibFigure, self).__init__(self.figs) # 在父类种激活self.fig， 否则不能显示图像
        self.axes = self.figs.add_subplot(111)