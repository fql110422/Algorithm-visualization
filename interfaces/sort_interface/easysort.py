from time import sleep
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout
from qfluentwidgets import (BodyLabel, PushButton, TitleLabel,setTheme,BodyLabel,TitleLabel,SimpleCardWidget,LineEdit,MessageBox)

from interfaces.sort_interface.matplotlibfigure import MatplotlibFigure

class EasySort(SimpleCardWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setObjectName('EasySort')
        self.Layout = QVBoxLayout()
        self.setLayout(self.Layout)
        #初始化数据
        self.data = []
        self.lastdata = []
        self.color = []
        self.sleeptime = 0
        #标题及按钮实例化
        self.Label = TitleLabel("简单排序")
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
        
        self.SelectionSortButton = PushButton("选择排序")
        self.BubbleSortButton = PushButton("冒泡排序")
        #布局
        self.hBoxLayout = QHBoxLayout()
        self.ButtonvBoxLayout = QVBoxLayout()
        self.samplesLabelhBoxLayout = QHBoxLayout()
        self.sleeptimeLabelhBoxLayout = QHBoxLayout()
        #实例化画布
        self.canvas = MatplotlibFigure(width=5, heigh=4, dpi=100)
        #按钮信号与槽
        self.RandomButton.clicked.connect(self.onClickedRandomButton)
        self.BubbleSortButton.clicked.connect(self.onClickedBubbleSortButton)
        self.SelectionSortButton.clicked.connect(self.onClickedSelectionSortButton)
        self.backDataButton.clicked.connect(self.onClickedBackDataButton)
        
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
        self.ButtonvBoxLayout.addWidget(self.SelectionSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.BubbleSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addStretch(1)
        
        
    def initStyle(self):
        #设置样式
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
        
    def onClickedBubbleSortButton(self):
        #冒泡排序
        self.showMessageBox('冒泡排序','冒泡排序的时间复杂度为O(n^2)，请耐心等待')
        self.showMessageBox('冒泡排序','它的工作原理是每次检查相邻两个元素，如果前面的元素与后面的元素满足给定的排序条件，就将相邻两个元素交换。当没有相邻的元素需要交换时，排序就完成了。')
        self.prohibitWidget()
        self.sleeptime = float(self.sleeptimeLineEdit.text())
        if not len(self.data) == 0:
            for i in range(len(self.data)):
                for j in range(len(self.data)-i-1):
                    self.darwEvent({j:'green',j+1:'red'})
                    if self.data[j] > self.data[j+1]:
                        self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
                        self.darwEvent({j:'red',j+1:'green'})       
        self.enableWidget()
                        
    def onClickedSelectionSortButton(self):
        #选择排序
        self.showMessageBox('选择排序','选择排序的时间复杂度为O(n^2)，请耐心等待')
        self.showMessageBox('选择排序','选择排序是一种简单直观的排序算法。它的工作原理是每次找出第 i 小的元素，然后将这个元素与数组第 i 个位置上的元素交换。')
        self.prohibitWidget()
        self.sleeptime = float(self.sleeptimeLineEdit.text())
        if not len(self.data) == 0:
            for i in range(len(self.data)):
                minIndex = i
                self.darwEvent({minIndex:'green'})
                for j in range(i+1,len(self.data)):
                    self.color = ['darkviolet']*len(self.data)
                    self.darwEvent({minIndex:'green',j:'red'})
                    if self.data[j] < self.data[minIndex]:
                        minIndex = j
                self.data[i],self.data[minIndex] = self.data[minIndex],self.data[i]
                self.darwEvent({minIndex:'green',i:'red'})
        self.enableWidget()
        
    def onClickedBackDataButton(self):
        #回退数据
        self.color = ['darkviolet']*len(self.data)
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.lastdata)),self.lastdata,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        self.data = self.lastdata.copy()
        
    def prohibitWidget(self):
        #排序开始后禁止所有按钮
        self.RandomButton.setEnabled(False)
        self.SelectionSortButton.setEnabled(False)
        self.BubbleSortButton.setEnabled(False)
        self.backDataButton.setEnabled(False)
        
    def enableWidget(self):
        #排序结束后开放按钮
        self.darwEvent() #排序完成后将所有颜色还原
        self.RandomButton.setEnabled(True)
        self.SelectionSortButton.setEnabled(True)
        self.BubbleSortButton.setEnabled(True)
        self.backDataButton.setEnabled(True)
        
    def darwEvent(self, changeColorDir={}):
        #根据传入的字典改变颜色并刷新画布
        self.color = ['darkviolet']*len(self.data)
        for i in changeColorDir.keys():
            self.color[i] = changeColorDir[i]
        
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.data)),self.data,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        sleep(self.sleeptime)
        
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        while not w.exec():
            pass