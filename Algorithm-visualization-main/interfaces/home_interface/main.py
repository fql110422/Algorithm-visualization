from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import (FluentIcon,FluentIcon)

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
            content="搜索是对状态空间进行枚举，找到与搜索条件匹配的信息。它有很多优化方式，如减小状态空间，更改搜索顺序，剪枝等。",
            routeKey="SearchInterface",
            index=1
        )
        cardView.addSampleCard(
            icon=FluentIcon.ALBUM,
            title="查找算法",
            content="查找是在有序或无序的数据集中找到特定元素的过程。这里我们仅展示单调递增数列的部分查找算法",
            routeKey="FindInterface",
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