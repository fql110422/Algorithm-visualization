from PyQt5.QtWidgets import QWidget, QStackedWidget
from qfluentwidgets import (SegmentedWidget)

from interfaces.gallery_interface.main import GalleryInterface
from interfaces.sort_interface.easysort import EasySort
from interfaces.sort_interface.advancedsort import AdvancedSort

class SortInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(title="排序算法",subtitle="Sort",parent=parent)
        self.setObjectName('SortInterface')
        self.view = QWidget()

        self.segmentWidget = SegmentedWidget(self.view)
        self.stackWidget = QStackedWidget(self.view)
        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
    def initWidget(self):
        self.easySort = EasySort(self)
        self.advancedSort = AdvancedSort(self)
        
        self.segmentWidget.addItem(
            routeKey="easySort",
            text="简单排序",
            onClick=lambda: self.stackWidget.setCurrentWidget(self.easySort)
        )
        
        self.segmentWidget.addItem(
            routeKey="advancedSort",
            text="进阶排序",
            onClick=lambda: self.stackWidget.setCurrentWidget(self.advancedSort)
        )
        self.segmentWidget.setCurrentItem("easySort")
        self.stackWidget.addWidget(self.easySort)
        self.stackWidget.addWidget(self.advancedSort)
    
    def initLayout(self):
        self.vBoxLayout.addWidget(self.segmentWidget)
        self.vBoxLayout.addWidget(self.stackWidget)
        
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )