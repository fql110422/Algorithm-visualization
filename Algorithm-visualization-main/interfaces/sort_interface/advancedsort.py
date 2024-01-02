from time import sleep
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from qfluentwidgets import (BodyLabel, PushButton, TitleLabel,BodyLabel,TitleLabel,SimpleCardWidget,LineEdit, MessageBox)

from interfaces.sort_interface.matplotlibfigure import MatplotlibFigure

class AdvancedSort(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('AdvancedSort')
        self.Layout = QVBoxLayout()
        self.setLayout(self.Layout)
        #初始化数据
        self.data = []
        self.lastdata = []
        self.color = []
        self.sleeptime = 0
        #标题及按钮实例化
        self.Label = TitleLabel("进阶排序")
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
        
        self.quickSortButton = PushButton("快速排序")
        self.mergeSortButton = PushButton("归并排序")
        self.heapSortButton = PushButton("堆排序")
        #布局
        self.hBoxLayout = QHBoxLayout()
        self.ButtonvBoxLayout = QVBoxLayout()
        self.samplesLabelhBoxLayout = QHBoxLayout()
        self.sleeptimeLabelhBoxLayout = QHBoxLayout()
        #实例化画布
        self.canvas = MatplotlibFigure(width=5, heigh=4, dpi=100)
        #按钮信号与槽
        self.RandomButton.clicked.connect(self.onClickedRandomButton)
        self.backDataButton.clicked.connect(self.onClickedBackDataButton)
        self.quickSortButton.clicked.connect(self.onClickedQuickSortButton)
        self.mergeSortButton.clicked.connect(self.onClickedMergeSortButton)
        self.heapSortButton.clicked.connect(self.onClickedHeapSortButton)
        
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
        self.ButtonvBoxLayout.addWidget(self.quickSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.mergeSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.heapSortButton,0,Qt.AlignTop)
        self.ButtonvBoxLayout.addStretch(1)
    
    def initStyle(self):
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
        
    def onClickedBackDataButton(self):
        #回退数据
        self.color = ['darkviolet']*len(self.data)
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.lastdata)),self.lastdata,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        self.data = self.lastdata.copy()
        
    def prohibitWidget(self):
        #禁用按钮
        self.RandomButton.setEnabled(False)
        self.quickSortButton.setEnabled(False)
        self.mergeSortButton.setEnabled(False)
        self.heapSortButton.setEnabled(False)
        self.backDataButton.setEnabled(False)
        
    def enableWidget(self):
        #启用按钮
        self.darwEvent() #还原颜色
        self.RandomButton.setEnabled(True)
        self.quickSortButton.setEnabled(True)
        self.mergeSortButton.setEnabled(True)
        self.heapSortButton.setEnabled(True)
        self.backDataButton.setEnabled(True)
        
    def darwEvent(self,changeColorDir={}):
        #根据传入的字典改变颜色并刷新画布
        self.color = ['darkviolet']*len(self.data)
        for i in changeColorDir.keys():
            self.color[i] = changeColorDir[i]
        
        self.canvas.axes.clear()
        self.canvas.axes.bar(range(len(self.data)),self.data,color=self.color)
        self.canvas.draw()
        self.canvas.flush_events()
        sleep(self.sleeptime)
        
    def onClickedQuickSortButton(self):
        self.showMessageBox('快速排序','快速排序是一种不稳定的排序算法。\n它的评价时间复杂度为O(nlogn)，请耐心等待')
        self.showMessageBox('快速排序', '快速排序分为三个过程：\n1:将数列划分为两部分（要求保证相对大小关系）\n2:递归到两个子序列中分别进行快速排序；\n3:不用合并，因为此时数列已经完全有序。')
        self.prohibitWidget()
        self.sleeptime = float(self.sleeptimeLineEdit.text())
        #快速排序
        self.quick_sort(0,len(self.data)-1)
        self.enableWidget()
        
    def onClickedMergeSortButton(self):
        self.showMessageBox('归并排序','归并排序是基于比较的稳定排序算法。\n它的时间复杂度为O(nlogn)，请耐心等待')
        self.showMessageBox('归并排序', '归并排序最核心的部分是合并（merge）过程：\n1:将两个有序的数组 a[i] 和 b[j] 合并为一个有序数组 c[k]。\n2:从左往右枚举 a[i] 和 b[j]，找出最小的值并放入数组 c[k]；\n3:重复上述过程直到 a[i] 和 b[j] 有一个为空时，将另一个数组剩下的元素放入 c[k]。')
        self.prohibitWidget()
        self.sleeptime = float(self.sleeptimeLineEdit.text())
        #归并排序
        self.merge_sort(0,len(self.data))
        self.enableWidget()
    
    def onClickedHeapSortButton(self):
        self.showMessageBox('堆排序','堆排序是利用二叉堆这种数据结构所设计的一种排序算法。其时间复杂度为O(nlogn)，请耐心等待')
        self.showMessageBox('堆排序','1:首先建立大顶堆，然后将堆顶的元素取出，作为最大值，与数组尾部的元素交换，并维持残余堆的性质；\n2:之后将堆顶的元素取出，作为次大值，与数组倒数第二位元素交换，并维持残余堆的性质；\n3:以此类推，在第 n-1 次操作后，整个数组就完成了排序。')
        self.prohibitWidget()
        self.sleeptime = float(self.sleeptimeLineEdit.text())
        self.heap_sort()
        #堆排序

        self.enableWidget()
        
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        while not w.exec():
            pass
        
    def merge_sort(self,left,right):
        #归并排序
        ll = left
        rr = right
        if rr-ll<=1:
            return
        mid = (ll+rr)//2
        self.merge_sort(ll,mid)
        self.merge_sort(mid,rr)
        self.darwEvent({ll:'green',rr-1:'red'})
        self.data[ll:rr] = self.merge_(self.data[ll:mid],self.data[mid:rr])
        self.darwEvent({ll:'red',rr-1:'green'})
        
        
    def merge_(self,a,b):
        i,j = 0,0
        c = []
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        c.extend(a[i:])
        c.extend(b[j:])
        return c

    def sift_down(self,arr, start, end):
        # 计算父结点和子结点的下标
        parent = int(start)
        child = int(parent * 2 + 1)
        while child <= end:  # 限制子结点下标在范围内
            # 比较两个子结点大小，选择最大的

            if child + 1 <= end and arr[child] < arr[child + 1]:
                self.darwEvent({child + 1: 'green', child: 'red'})
                child += 1
            # 父结点比子结点大，代表调整完毕，直接跳出函数
            if arr[parent] >= arr[child]:
                self.darwEvent({parent: 'green', child: 'red'})
                return
            else:  # 交换父子内容，子结点再和孙结点比较
                arr[parent], arr[child] = arr[child], arr[parent]
                self.darwEvent({parent: 'red', child: 'green'})
                parent = child
                child = int(parent * 2 + 1)


    def heap_sort(self):

        leng=len(self.data)
        # 从最后一个节点的父节点开始 sift down
        i = (leng - 1 - 1) / 2
        while (i >= 0):
            self.sift_down(self.data, i, leng - 1)
            i -= 1

        # 先将第一个元素和已经排好的元素前一位做交换，再重新调整，直到排序完毕
        i = leng - 1
        while (i > 0):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.sift_down(self.data, 0, i - 1)
            i -= 1

    def quick_sort(self, first, last):


        if first >= last:
            return
        mid_value = self.data[first]
        low = first
        high = last
        while low < high:
            self.darwEvent({low: 'red', high: 'green'})

            while low < high and self.data[high] >= mid_value:
                high -= 1

            self.data[low] = self.data[high]
            while low < high and self.data[low] < mid_value:
                low += 1

            self.data[high] = self.data[low]
        self.data[low] = mid_value
        self.quick_sort(first, low - 1)
        self.quick_sort(low + 1, last)