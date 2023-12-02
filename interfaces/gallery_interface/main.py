import typing
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QProcess
from PyQt5.QtGui import QDesktopServices, QPainter, QPen, QColor
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSizePolicy, QStackedWidget
from qfluentwidgets import (CaptionLabel,isDarkTheme,ScrollArea, CardWidget, SegmentedWidget, SettingCardGroup, SwitchSettingCard, 
                            FluentIcon, StrongBodyLabel, BodyLabel, ExpandLayout, ToolTipFilter, ComboBoxSettingCard, 
                            ToolTipPosition, PrimaryPushSettingCard, InfoBar, InfoBarPosition, PushButton, TitleLabel, 
                            OptionsSettingCard, HyperlinkCard, PushSettingCard,ToolButton,toggleTheme)

class SeparatorWidget(QWidget):
    """ Seperator widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(6, 16)

    def paintEvent(self, e):
        painter = QPainter(self)
        pen = QPen(1)
        pen.setCosmetic(True)
        c = QColor(255, 255, 255, 21) if isDarkTheme() else QColor(0, 0, 0, 15)
        pen.setColor(c)
        painter.setPen(pen)

        x = self.width() // 2
        painter.drawLine(x, 0, x, self.height())

class ToolBar(QWidget):
    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent)
        self.titleLabel = TitleLabel(title, self)
        self.subtitleLabel = CaptionLabel(subtitle, self)
        self.themeButton = ToolButton(FluentIcon.CONSTRACT, self)
        self.separator = SeparatorWidget(self)
        self.submitButton = PushButton("联系开发者", self, FluentIcon.GITHUB)
        
        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()
        
        self.initWidget()
        
    def initWidget(self):
        self.setFixedHeight(140)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(36, 22, 36, 12)
        self.vBoxLayout.addWidget(self.titleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addWidget(self.subtitleLabel)
        self.vBoxLayout.addSpacing(4)
        self.vBoxLayout.addLayout(self.hBoxLayout,1)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        
        self.hBoxLayout.setSpacing(4)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.submitButton,0,Qt.AlignLeft)
        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.separator,0,Qt.AlignRight)
        self.hBoxLayout.addWidget(self.themeButton,0,Qt.AlignRight)
        self.hBoxLayout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        
        self.submitButton.installEventFilter(ToolTipFilter(self.submitButton))
        self.submitButton.setToolTip(self.tr('如果有任何问题或者有修改建议，欢迎联系开发者'))
        
        self.themeButton.installEventFilter(ToolTipFilter(self.themeButton))
        self.themeButton.setToolTip(self.tr('变更主题'))
        self.themeButton.clicked.connect(lambda: toggleTheme(True))
        
        self.subtitleLabel.setTextColor(QColor(96, 96, 96), QColor(216, 216, 216))
        
class GalleryInterface(ScrollArea):
    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent)
        self.view = QWidget()
        self.view.setObjectName('view')
        self.expandLayout = ExpandLayout()
        self.toolbar = ToolBar(title,subtitle,self)
        self.vBoxLayout = QVBoxLayout(self.view)
        
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0,self.toolbar.height(),0,0)
        self.setWidget(self.view)
        self.setWidgetResizable(True)
        
        self.vBoxLayout.addLayout(self.expandLayout)
        self.vBoxLayout.setSpacing(30)
        self.vBoxLayout.setAlignment(Qt.AlignTop)
        self.vBoxLayout.setContentsMargins(36, 0, 36, 36)
        
        self.expandLayout.setSpacing(5)
        
    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.toolbar.resize(self.width(), self.toolbar.height())       