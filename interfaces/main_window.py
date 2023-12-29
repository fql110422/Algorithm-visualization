import sys
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QProcess,QSize,QPoint
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QStackedWidget
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QSizePolicy
from PyQt5.QtGui import QIcon, QCursor, QMouseEvent
from qfluentwidgets import (ScrollArea, CardWidget, SegmentedWidget, SettingCardGroup, SwitchSettingCard, 
                            FluentIcon, StrongBodyLabel, BodyLabel, ExpandLayout, ToolTipFilter, ComboBoxSettingCard, 
                            ToolTipPosition, PrimaryPushSettingCard, InfoBar, InfoBarPosition, PushButton, TitleLabel, 
                            OptionsSettingCard, HyperlinkCard, PushSettingCard,FluentWindow,FluentIcon,Theme,setTheme,
                            Action,RoundMenu,NavigationItemPosition,NavigationAvatarWidget,StrongBodyLabel,BodyLabel,
                            ToolTipFilter,TitleLabel,SplashScreen)

from interfaces.home_interface.main import HomeInterface
from interfaces.sort_interface.main import SortInterface
from interfaces.search_interface.main import SearchInterface
from interfaces.find_interface.main import FindInterface

'''
//                            _ooOoo_  
//                           o8888888o  
//                           88" . "88  
//                           (| -_- |)  
//                            O\ = /O  
//                        ____/`---'\____  
//                      .   ' \\| |// `.  
//                       / \\||| : |||// \  
//                     / _||||| -:- |||||- \  
//                       | | \\\ - /// | |  
//                     | \_| ''\---/'' | |  
//                      \ .-\__ `-` ___/-. /  
//                   ___`. .' /--.--\ `. . __  
//                ."" '< `.___\_<|>_/___.' >'"".  
//               | | : `- \`.;`\ _ /`;.`/ - ` : | |  
//                 \ \ `-. \_ __\ /__ _/ .-` / /  
//         ======`-.____`-.___\_____/___.-`____.-'======  
//                            `=---='  
//  
//         .............................................  
//                  佛祖保佑             永无BUG 
//         .............................................
//                           23.12.12
'''


class mainWindow(FluentWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        setTheme(Theme.AUTO)
        
        self.initWindow()
        self.initWidget()
        self.initNavigation()
        
        self.splashScreen.finish()
        
    def initWidget(self):
        self.homeinterface = HomeInterface(self)
        self.sortinterface = SortInterface(self)
        self.searchinterface = SearchInterface(self)
        self.findinterface = FindInterface(self)
    
    def initNavigation(self):
        self.navigationInterface.panel.menuButton.setToolTip('展开菜单')
        self.navigationInterface.setExpandWidth(300)
        
        self.addSubInterface(
            interface=self.homeinterface,
            icon=FluentIcon.HOME,
            text='主页',
            position=NavigationItemPosition.TOP,
        )
        
        self.addSubInterface(
            interface=self.sortinterface,
            icon=FluentIcon.UNIT,
            text='排序',
            position=NavigationItemPosition.TOP,
        )
        
        self.addSubInterface(
            interface=self.searchinterface,
            icon=FluentIcon.IOT,
            text='搜索',
            position=NavigationItemPosition.TOP,
        )
        
        self.addSubInterface(
            interface=self.findinterface,
            icon=FluentIcon.ALBUM,
            text="查找",
            position=NavigationItemPosition.TOP
        )
        
        
    def initWindow(self):
        self.resize(875, 770)
        self.setMinimumWidth(875)
        self.setMinimumHeight(500)
        
        self.setWindowTitle('算法可视化')

        self.setMicaEffectEnabled(True)

        # 创建加载窗口
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()
        
    def closeEvent(self, e):
        sys.exit(0)