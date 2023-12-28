import typing
import matplotlib
matplotlib.use('Qt5Agg')
from time import sleep
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, QProcess,QSize,QPoint, QTimer
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
        self.data = []
        self.timer = QTimer()
        
        self.grid = Grid(self)
        self.cardWidget = SimpleCardWidget(self)
        self.cardVBoxLayout = QVBoxLayout()
        
        self.samplesLabel = BodyLabel(self)
        self.samplesLabel.setText("请输入要查找的数:")
        self.samplesLineEdit = LineEdit(self)
        self.sampleshBoxLayout = QHBoxLayout()
        
        self.resetButton = PushButton("重置")
        self.sortrandomButton = PushButton("随机生成数字")
        self.sequential_search_Button = PushButton("顺序查找")
        self.binary_search_Button = PushButton("二分查找")
        self.interpolation_search_Button = PushButton("插值查找")
        self.fibonacci_search_Button = PushButton("斐波那契查找")
        self.hash_search_Button = PushButton("哈希查找")
        
        self.resetButton.clicked.connect(self.onClickedresetButton)
        self.sortrandomButton.clicked.connect(self.onClickedsortrandomButton)
        self.sequential_search_Button.clicked.connect(self.onClickedsequentialSearchButton)
        self.binary_search_Button.clicked.connect(self.onClickedbinarysearchButton)
        self.interpolation_search_Button.clicked.connect(self.onClickedinterpolationSearchButton)
        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
    def initWidget(self):
        self.cardWidget.setFixedHeight(500)
    
    def initLayout(self):
        self.vBoxLayout.addWidget(self.cardWidget, 0, Qt.AlignTop)
        self.cardWidget.setLayout(self.cardVBoxLayout)
        
        self.sampleshBoxLayout.addWidget(self.samplesLabel)
        self.sampleshBoxLayout.addWidget(self.samplesLineEdit)
        
        self.cardVBoxLayout.addWidget(self.grid, 0, Qt.AlignTop)
        self.cardVBoxLayout.addWidget(self.sortrandomButton, 0, Qt.AlignTop)
        self.cardVBoxLayout.addLayout(self.sampleshBoxLayout)
        self.cardVBoxLayout.addWidget(self.resetButton, 0, Qt.AlignTop)
        self.cardVBoxLayout.addWidget(self.sequential_search_Button, 0, Qt.AlignTop)
        self.cardVBoxLayout.addWidget(self.binary_search_Button, 0, Qt.AlignTop)
        self.cardVBoxLayout.addWidget(self.interpolation_search_Button, 0, Qt.AlignTop)
        self.cardVBoxLayout.addWidget(self.fibonacci_search_Button, 0, Qt.AlignTop)
        self.cardVBoxLayout.addWidget(self.hash_search_Button, 0, Qt.AlignTop)
        self.cardVBoxLayout.addStretch(1)
        
        
    
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )
        
    def onClickedresetButton(self):
        self.grid.resetGridItem()
        
    def onClickedsortrandomButton(self):
        self.grid.resetGridItem()
        self.data = []
        for i in range(21):
            self.data.append(random.randint(1,100))
        self.data.sort()
        for i in range(21):
            self.grid.setButtonText(i,self.data[i])
            
#---------------------顺序查找部分----------------------------
            
    def update_gui_sequential(self):
        try:
            next(self.sequential_generator)
        except StopIteration:
            self.timer.stop()
            self.enableWidget()
            try:
                self.timer.timeout.disconnect(self.update_gui_sequential)  # 断开旧的连接
            except TypeError:
                pass
            
    def onClickedsequentialSearchButton(self):
        self.onClickedresetButton()
        if self.data == []:
            self.showMessageBox("错误","请先生成一组数字")
        elif self.samplesLineEdit.text() == '':
            self.showMessageBox("错误","请输入要找的数字")           
        else:
            self.unableWidget()
            self.target = int(self.samplesLineEdit.text())
            
            
            self.timer.timeout.connect(self.update_gui_sequential)
            self.sequential_generator = self.sequentialSearch()
            self.timer.start(500)
            
            
    def sequentialSearch(self):
        last_i = 0
        for i in range(len(self.data)):
            self.grid.setArrowhead(last_i,False)
            self.grid.setArrowhead(i)
            yield
            if self.data[i] == self.target:
                self.showMessageBox("查找成功","数字"+str(self.target)+"在第"+str(i+1)+"个位置")
                return
            elif self.data[i] > self.target:   
                self.showMessageBox("查找失败","未能找到该数字")
                return
            last_i = i
        self.showMessageBox("查找失败","未能找到该数字")
        
    
#----------------------二分查找部分------------------------
    def update_gui_binary(self):
        try:
            next(self.binary_generator)
        except StopIteration:
            self.timer.stop()
            self.enableWidget()
            try:
                self.timer.timeout.disconnect(self.update_gui_binary)  # 断开旧的连接
            except TypeError:
                pass
            
    def onClickedbinarysearchButton(self):
        self.onClickedresetButton()
        if self.data == []:
            self.showMessageBox("错误","请先生成一组数字")
        elif self.samplesLineEdit.text() == '':
            self.showMessageBox("错误","请输入要找的数字")
        else:
            self.unableWidget()
            self.target = int(self.samplesLineEdit.text())
            
            
            self.timer.timeout.connect(self.update_gui_binary)
            self.binary_generator = self.binarySearch()
            self.timer.start(500)
            
            
    def binarySearch(self):
        left = 0
        right = len(self.data)-1
        self.arrowheadshow(left, right)
        yield
        while left<=right:
            mid = (left + right) // 2
            last_left = left
            last_right = right
            if self.data[mid] == self.target:
                self.arrowheadshow(left,right,False)
                self.grid.setArrowhead(mid)
                yield
                self.showMessageBox("查找成功","数字"+str(self.target)+"在第"+str(mid+1)+"个位置")
                return 
            elif self.data[mid] < self.target:
                left = mid + 1
                self.grid.setArrowhead(last_left,False)
                self.grid.setArrowhead(left)
                yield
            else:
                right = mid - 1
                self.grid.setArrowhead(last_right,False)
                self.grid.setArrowhead(right)
                yield
        self.showMessageBox("查找失败","所要找的数不在列表中")
                
    def arrowheadshow(self, i, j, state = True):
            self.grid.setArrowhead(i,state)
            self.grid.setArrowhead(j,state)

#------------------------------插值查找部分--------------------------
    def update_gui_interpolation(self):
        try:
            next(self.interpolation_generator)
        except StopIteration:
            self.timer.stop()
            self.enableWidget()
            try:
                self.timer.timeout.disconnect(self.update_gui_interpolation)  # 断开旧的连接
            except TypeError:
                pass
            
    def onClickedinterpolationSearchButton(self):
        self.onClickedresetButton()
        if self.data == []:
            self.showMessageBox("错误","请先生成一组数字")
        elif self.samplesLineEdit.text() == '':
            self.showMessageBox("错误","请输入要找的数字")
        else:
            self.unableWidget()
            self.target = int(self.samplesLineEdit.text())
            
            self.timer.timeout.connect(self.update_gui_interpolation)
            self.interpolation_generator = self.interpolationSearch()
            self.timer.start(500)
            
    def interpolationSearch(self):
        low = 0
        high = len(self.data) - 1
        self.arrowheadshow(low, high)
        yield
        while low <= high and self.target >= self.data[low] and self.target <= self.data[high]:
            last_low = low
            last_high = high

            mid = low + round(((high - low) / (self.data[high] - self.data[low])) * (self.target - self.data[low]))
                
            if self.data[mid] == self.target:
                self.arrowheadshow(low, high, False)
                self.grid.setArrowhead(mid)
                yield
                self.showMessageBox("查找成功","数字"+str(self.target)+"在第"+str(mid+1)+"个位置")
                return

            elif self.data[mid] < self.target:
                low = mid + 1
                self.grid.setArrowhead(last_low,False)
                self.grid.setArrowhead(low)
                yield
            else:
                high = mid - 1
                self.grid.setArrowhead(last_high,False)
                self.grid.setArrowhead(high)
                yield

        self.showMessageBox("查找失败", "所要找的数不在列表中")
            
#------------------------斐波那契查找部分-------------------------
    def update_gui_fibonacci(self):
        try:
            next(self.fibonacci_generator)
        except StopIteration:
            self.timer.stop()
            self.enableWidget()
            try:
                self.timer.timeout.disconnect(self.update_gui_fibonacci)  # 断开旧的连接
            except TypeError:
                pass
            
    def onClickedfibonacciSearchButton(self):
        self.onClickedresetButton()
        if self.data == []:
            self.showMessageBox("错误","请先生成一组数字")
        elif self.samplesLineEdit.text() == '':
            self.showMessageBox("错误","请输入要找的数字")
        else:
            self.unableWidget()
            self.target = int(self.samplesLineEdit.text())
            
            self.timer.timeout.connect(self.update_gui_fibonacci)
            self.fibonacci_generator = self.fibonacciSearch()
            self.timer.start(500)
            
    def fibonacciSearch(self):
        pass
#--------------------------哈希查找部分--------------------------
    def update_gui_hash(self):
        try:
            next(self.hash_generator)
        except StopIteration:
            self.timer.stop()
            self.enableWidget()
            try:
                self.timer.timeout.disconnect(self.update_gui_hash)  # 断开旧的连接
            except TypeError:
                pass
            
    def onClickedhashSearchButton(self):
        self.onClickedresetButton()
        if self.data == []:
            self.showMessageBox("错误","请先生成一组数字")
        elif self.samplesLineEdit.text() == '':
            self.showMessageBox("错误","请输入要找的数字")
        else:
            self.unableWidget()
            self.target = int(self.samplesLineEdit.text())
            
            self.timer.timeout.connect(self.update_gui_hash)
            self.hash_generator = self.hashSearch()
            self.timer.start(500)
            
    def hashSearch(self):
        pass
#-------------------------------------------------------------------
    
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        while not w.exec():
            pass
        
    def enableWidget(self):
        #排序结束后开放按钮
        self.resetButton.setEnabled(True)
        self.sortrandomButton.setEnabled(True)
        self.sequential_search_Button.setEnabled(True)
        self.binary_search_Button.setEnabled(True)
        self.interpolation_search_Button.setEnabled(True)
        self.fibonacci_search_Button.setEnabled(True)
        self.hash_search_Button.setEnabled(True)
        
    def unableWidget(self):
        self.resetButton.setEnabled(False)
        self.sortrandomButton.setEnabled(False)
        self.sequential_search_Button.setEnabled(False)
        self.binary_search_Button.setEnabled(False)
        self.interpolation_search_Button.setEnabled(False)
        self.fibonacci_search_Button.setEnabled(False)
        self.hash_search_Button.setEnabled(False)