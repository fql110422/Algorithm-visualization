import random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout
from qfluentwidgets import (BodyLabel, PushButton, BodyLabel,SimpleCardWidget,LineEdit, MessageBox)

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
        self.fibonacci_search_Button.clicked.connect(self.onClickedfibonacciSearchButton)
        self.hash_search_Button.clicked.connect(self.onClickedhashSearchButton)
        
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
            self.showMessageBox("顺序查找","顺序查找是按照序列原有顺序对数组进行遍历比较查询的基本查找算法。")
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
            self.showMessageBox("二分查找","二分查找也称折半查找，它是一种效率较高的查找方法。")
            self.showMessageBox("二分查找","首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；\n否则利用中间位置记录将表分成前、后两个子表，如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。\n重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。")
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
                if left < len(self.data):
                    self.grid.setArrowhead(last_left,False)
                    self.grid.setArrowhead(left)
                    yield
            else:
                right = mid - 1
                if right >= 0:
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
            self.showMessageBox("插值查找","插值查找是根据查找关键字与查找表中最大最小记录关键字比较后的查找方法。插值查找基于二分查找，将查找点的选择改进为自适应选择，提高查找效率。")
            self.showMessageBox("插值查找","插值类似于平常查英文字典的方法，在查一个以字母C开头的英文单词时，决不会用二分查找，从字典的中间一页开始，因为知道它的大概位置是在字典的较前面的部分，因此可以从前面的某处查起，这就是插值查找的基本思想。")
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
            self.showMessageBox("斐波那契查找","斐波那契查找就是在二分查找的基础上根据斐波那契数列来进行分割的。")
            self.showMessageBox("斐波那契查找","在斐波那契数列找一个等于略大于查找表中元素个数的数F[n]，将原查找表扩展为长度为F[n](如果要补充元素，则补充重复最后一个元素，直到满足F[n]个元素)，\n完成后进行斐波那契分割，即F[n]个元素分割为前半部分F[n-1]个元素，后半部分F[n-2]个元素，\n找出要查找的元素在那一部分并递归，直到找到。")
            self.unableWidget()
            self.target = int(self.samplesLineEdit.text())
            
            self.timer.timeout.connect(self.update_gui_fibonacci)
            self.fibonacci_generator = self.fibonacciSearch()
            self.timer.start(500)
            
    def fibonacciSearch(self):
        fibMMm2 = 0
        fibMMm1 = 1
        fibM = fibMMm2 + fibMMm1
        
        while fibM < len(self.data):
            fibMMm2 = fibMMm1
            fibMMm1 = fibM
            fibM = fibMMm2 + fibMMm1
            
        offset = -1
        i = 0
        while fibM > 1:
            last_i = i
            i = min(offset+fibMMm2, len(self.data)-1)
            self.onClickedresetButton()
            self.grid.setArrowhead(last_i,False)
            self.grid.setArrowhead(i)
            self.gridColorSet(offset+1, i, "red")
            self.gridColorSet(i+1, i+fibMMm1, "green")
            yield
            
            if self.data[i] < self.target:   
                fibM = fibMMm1
                fibMMm1 = fibMMm2
                fibMMm2 = fibM - fibMMm1
                offset = i
                
            elif self.data[i] > self.target:
                fibM = fibMMm2
                fibMMm1 = fibMMm1 - fibMMm2
                fibMMm2 = fibM - fibMMm1
                
            else:
                self.showMessageBox("查找成功","数字"+str(self.target)+"在第"+str(offset+2)+"个位置")
                return
            
        if fibMMm1 and self.data[offset+1] == self.target:
            self.showMessageBox("查找成功","数字"+str(self.target)+"在第"+str(offset+2)+"个位置")
            return
        
        self.showMessageBox("查找失败","所要找的数不在列表中")
    
    def gridColorSet(self, left, right, color):
        for i in range(left, right+1):
            self.grid.setButtonColor(i, color)
    
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
            self.showMessageBox("哈希查找","是通过计算数据元素的存储地址进行查找的一种方法，解决冲突方法有开放地址法、链地址法等。")
            self.showMessageBox("哈希查找","是哈希查找的操作步骤：\n1:用给定的哈希函数构造哈希表；\n2:根据选择的冲突处理方法解决地址冲突；\n3:在哈希表的基础上执行哈希查找。")
            self.unableWidget()
            self.target = int(self.samplesLineEdit.text())
            
            self.timer.timeout.connect(self.update_gui_hash)
            self.hash_generator = self.hashSearch()
            self.timer.start(500)
            
    def hashSearch(self):
        hash_table = {value: index for index, value in enumerate(self.data)}
        for i in range(len(self.data)):
            try:
                self.grid.setArrowhead(hash_table[self.target])
                self.showMessageBox("查找成功","数字"+str(self.target)+"在第"+str(hash_table[self.target]+1)+"个位置")
                yield
                return
            except KeyError:
                self.showMessageBox("查找失败","所要找的数不在列表中")
                return
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