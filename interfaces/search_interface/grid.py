from PyQt5.QtCore import Qt, pyqtSignal
from qfluentwidgets import (PushButton,SimpleCardWidget,MessageBox,FlowLayout)

list = []

class GridItem(PushButton):
    rightClicked = pyqtSignal()
    def __init__(self, x, y, sidelength, parent=None):
        super().__init__(parent)
        global list
        self.sidelength = sidelength
        self.setFixedSize(self.sidelength, self.sidelength)
        self.x = x
        self.y = y
        
        self.color = "white"
        self.setcolor(self.color)
        
        self.clicked.connect(self.leftclick)
        self.rightClicked.connect(self.rightclick)
        
    def leftclick(self):
        #设置障碍
        self.setcolor("black")
        list[self.x][self.y] = 1
        
    def rightclick(self):
        #设置起点和终点
        if self.color == "white":
            if not self.checkifin(2):
                self.setcolor("green")
                list[self.x][self.y] = 2
            elif not self.checkifin(3):
                self.setcolor("red")
                list[self.x][self.y] = 3
            else:
                self.showMessageBox("错误", "起点和终点已经设置")
        else:
            self.setcolor("white")
            list[self.x][self.y] = 0
            self.setText(None)
            
    def checkifin(self, n):
        for i in range(len(list)):
            for j in range(len(list)):
                if list[i][j] == n:
                    return True

    def setcolor(self, color):
        #设置按钮颜色
        self.color = color
        self.setStyleSheet(
            "border: 1px solid black; "
            "background-color: {};".format(self.color)
        )
    
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        # 为右键单击事件建立信号
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
    
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        while not w.exec():
            pass

        

class Grid(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        global list
        
        self._____ = 15
        self.sidelength = 500
        list = [[0 for i in range(self._____)] for j in range(self._____)]
        
        self.setFixedSize(int(self.sidelength*1.05), int(self.sidelength*1.05))
        self.flowLayout = FlowLayout()
        self.setLayout(self.flowLayout)
        self.flowLayout.setHorizontalSpacing(0)
        self.flowLayout.setVerticalSpacing(0)
        
        self.initWidget()
        
    def initWidget(self):
        for i in range(self._____):
            for j in range(self._____):
                self.flowLayout.addWidget(GridItem(i, j, int(self.sidelength/self._____), self))
        self.itemList = self.findChildren(GridItem)
                
    def resetGridItem(self):
        #将网格颜色重置
        for item in self.itemList:
            item.setcolor("white")
            item.setText(None)
            list[item.x][item.y] = 0
            
            
    def resetStartAndEnd(self):
        #将起点和终点重置
        for item in self.itemList:
            if item.color == "green" or item.color == "red" or item.color == "yellow" or item.color == "pink" or item.color == "purple":
                item.setcolor("white")
                list[item.x][item.y] = 0
                item.setText(None)
                
    def resetPassedWay(self):
        #将已经走过的路重置
        for item in self.itemList:
            if item.color == "yellow" or item.color == "pink" or item.color == "purple":
                item.setcolor("white")
                list[item.x][item.y] = 0
                item.setText(None)
    
    def setGridItem(self, changedlist):
        #设置网格颜色,传入坐标然后更改颜色
        for __ in range(self._____):
            for _ in range(self._____):
                idx = __*self._____+_
                if changedlist[__][_] == -1:
                    self.itemList[idx].setcolor("yellow")
                
    def getlist(self):
        return list
    
    def setButtonText(self, __, _, text = None):
        idx = self._____*__ + _
        self.itemList[idx].setText(str(text))
        
    def setButtonColor(self, __, _, ____):
        #sleep(0.1)
        idx = self._____*__ + _
        self.itemList[idx].setcolor(____)
        
    def getButtonText(self, __, _):
        idx = self._____*__ + _
        return self.itemList[idx].text()
    
    def getButtonColor(self, __, _):
        idx = self._____*__ + _
        return self.itemList[idx].color
    
    def setButtonIcon(self, __, _, icon):
        idx = self._____*__ + _
        self.itemList[idx].setIcon(icon)