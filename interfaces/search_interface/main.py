from collections import deque
from time import sleep
from PyQt5.QtCore import Qt, QThread, pyqtSignal,QTimer
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout
from qfluentwidgets import (FluentIcon,PushButton,FluentIcon,SimpleCardWidget,MessageBox)

from interfaces.gallery_interface.main import GalleryInterface
from interfaces.search_interface.grid import Grid

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
//                           23.12.29
'''



dir = [[-1,0],[0,-1],[1,0],[0,1]] # 上左下右
dir_icon = [FluentIcon.UP,FluentIcon.LEFT_ARROW,FluentIcon.DOWN,FluentIcon.RIGHT_ARROW]

class SearchInterface(GalleryInterface):
    def __init__(self, parent=None):
        super().__init__(title="搜索算法",subtitle="Search",parent=parent)
        self.setObjectName('SearchInterface')
        self.view = QWidget()
        
        self.grid = Grid(self)
        self.cardWidget = SimpleCardWidget(self)
        self.hBoxLayout = QHBoxLayout()
        self.ButtonvBoxLayout = QVBoxLayout()

        self.resetGridButton = PushButton("重置网格")
        self.resetStartAndEndButton = PushButton("重置起点和终点")
        self.BFSButton = PushButton("广度优先搜索(BFS)")
        self.DFSButton = PushButton("深度优先搜索(DFS)")
        
        self.resetGridButton.clicked.connect(self.grid.resetGridItem)
        self.resetStartAndEndButton.clicked.connect(self.grid.resetStartAndEnd)
        self.BFSButton.clicked.connect(self.onclickedBFS)
        self.DFSButton.clicked.connect(self.onclickedDFS)
        
        self.initWidget()
        self.initLayout()
        self.initStyle()
        
    def initWidget(self):
        pass
    
    def initLayout(self):
        self.vBoxLayout.addWidget(self.cardWidget)
        self.cardWidget.setLayout(self.hBoxLayout)
        self.hBoxLayout.addWidget(self.grid, 0, Qt.AlignLeft)
        self.hBoxLayout.addLayout(self.ButtonvBoxLayout)
        
        self.ButtonvBoxLayout.addWidget(self.resetGridButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.resetStartAndEndButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.BFSButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addWidget(self.DFSButton, 0, Qt.AlignTop)
        self.ButtonvBoxLayout.addStretch(1)
    
    def initStyle(self):
        self.setStyleSheet(
            "border: none; "
            "background-color: transparent;"
        )
       
#------------------------------DFS----------------------------------------------------       
 
    def onclickedDFS(self):
        #深度优先搜索
        self.grid.resetPassedWay()
        self.list = self.grid.getlist() #获取网格迷宫
        self.vis = [[False for _ in range(len(self.list))] for _ in range(len(self.list))]
        if self.checkifin(2) and self.checkifin(3): #检查是否设置了起点和终点
            self.showMessageBox("深度优先搜索", "DFS即深度优先搜索，是最基础、最重要的搜索算法之一。")
            self.showMessageBox("深度优先搜索", "所谓深度优先，就是说每次都尝试向更深的节点走。通常我们使用递归的方式来实现DFS\n其最显著的特征在于其递归调用自身。同时与 BFS 类似，DFS 会对其访问过的点打上访问标记，在遍历图时跳过已打过标记的点，以确保每个点仅访问一次。")
            #深度优先搜索代码
            self.unableWidget()
            start_i, start_j = self.findStart()
            end_i, end_j = self.findEnd()
            self.grid.setButtonText(start_i, start_j, "0")
            
            self.worker = DFSWorker(self.grid, self.list, start_i, start_j, end_i, end_j)
            self.worker.updateSignal_color.connect(self.update_gui_dfs_color)
            self.worker.updateSignal_text.connect(self.update_gui_dfs_text)
            # self.worker.updateSignal_icon.connect(self.update_gui_dfs_icon)
            self.worker.finished.connect(self.update_gui_dfs_end)
            
            self.worker.start()
            
        else:
            self.showMessageBox("错误", "请设置起点和终点")
    
    def update_gui_dfs_text(self, x, y, text):
        self.grid.setButtonText(x, y, text)
            
    def update_gui_dfs_color(self, x, y, color):
        if self.grid.getButtonColor(x, y) != "red" and self.grid.getButtonColor(x, y) != "green":
            self.grid.setButtonColor(x, y, color)
            
    def update_gui_dfs_icon(self, x, y, k):
        self.grid.setButtonIcon(x, y, dir_icon[k])
        
    def update_gui_dfs_end(self):
        if self.worker.is_sccuess:
            self.showMessageBox("成功", "已经走到终点")
        else:
            self.showMessageBox("失败","没有找到一条成功路径")
        self.enableWidget()
            
    '''def DFS(self, start_i, start_j, end_i, end_j):
        Q = deque()
        Q.append(Node(start_i, start_j, 0))
        
        while Q:
            now = Q.pop()
            for i in range(4):
                xx, yy = now.x, now.y
                while True:
                    xx += dir[i][0]
                    yy += dir[i][1]
                    if self.in_map(xx, yy):
                        if not self.vis[xx][yy] and self.list[xx][yy] != 1 and self.list:
                            self.vis[xx][yy] = True
                            now.step += 1
                            self.grid.setButtonText(xx, yy, str(now.step))
                            Q.append(Node(xx, yy, now.step))
                            if self.list[xx][yy] == 3:
                                self.showMessageBox("成功", "已经走到终点")
                                return
                            elif self.list[xx][yy] == 0:
                                self.grid.setButtonColor(xx, yy, "blue")
                                yield
                            self.grid.setButtonColor(xx,yy,"yellow")
                            yield
                            
                        else:
                            break
                    else:
                        break
        
            
        if not self.vis[end_i][end_j]:
            self.showMessageBox("失败","没有找到一条成功路径")'''
        
#--------------------------BFS----------------------------------------------

    def onclickedBFS(self):
        #广度优先搜索
        self.grid.resetPassedWay()
        self.list = self.grid.getlist()
        self.vis = [[False for _ in range(len(self.list))] for _ in range(len(self.list))]
        if self.checkifin(2) and self.checkifin(3):
            self.showMessageBox("广度优先搜索", "BFS即广度优先搜索，是最基础、最重要的搜索算法之一。")
            self.showMessageBox("广度优先搜索", "所谓广度优先。就是每次都尝试访问同一层的节点。 \n如果同一层都访问完了，再访问下一层。\n这样做的结果是，BFS 算法找到的路径是从起点开始的最短合法路径。\n在 BFS 结束时，每个节点都是通过从起点到该点的最短路径访问的。")
            pass
            self.unableWidget()
            start_i, start_j = self.findStart()
            end_i, end_j = self.findEnd()
            
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_gui_bfs)
            self.bfs_generator = self.BFS(start_i, start_j, end_i, end_j)
            self.timer.start(50)
            
        else:
            self.showMessageBox("错误", "请设置起点和终点")
    
    def update_gui_bfs(self):
        try:
            next(self.bfs_generator)
        except:
            self.timer.stop()
            self.enableWidget()
             
    def BFS(self, start_i, start_j, end_i, end_j):
        Q = deque()
        Q.append(Node(start_i, start_j, 0))
        self.vis[start_i][start_j] = True
        while Q:
            now = Q.popleft()
            #print(f"Step for node ({now.x}, {now.y}): {now.step}")
            x, y = now.x, now.y
            for i in range(4):
                xx, yy = x + dir[i][0], y + dir[i][1]
                if self.in_map(xx, yy):
                    if not self.vis[xx][yy] and self.list[xx][yy] != 1:
                        self.vis[xx][yy] = True
                        self.grid.setButtonText(xx, yy, str(now.step + 1))
                        if self.list[xx][yy] == 3:
                            self.showMessageBox("成功", "已经走到终点")
                            return
                        elif self.list[xx][yy] == 0:
                            self.grid.setButtonColor(xx, yy, "blue")
                        Q.append(Node(xx, yy, now.step + 1))
                        yield
                        self.grid.setButtonColor(xx,yy,"yellow")
                        yield
        if not self.vis[end_i][end_j]:
            self.showMessageBox("失败","没有找到一条成功路径")
                
    def in_map(self, x, y):
        return 0 <= x < len(self.list) and 0 <= y < len(self.list)
      
#--------------------------------------------------------------------------------  
            
    def unableWidget(self):
        self.resetGridButton.setEnabled(False)
        self.resetStartAndEndButton.setEnabled(False)
        self.BFSButton.setEnabled(False)
        self.DFSButton.setEnabled(False)
        
    def enableWidget(self):
        self.resetGridButton.setEnabled(True)
        self.resetStartAndEndButton.setEnabled(True)
        self.BFSButton.setEnabled(True)
        self.DFSButton.setEnabled(True)
    
    def checkifin(self, n):
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i][j] == n:
                    return True
    
    def showMessageBox(self,title,content):
        #显示消息框
        w = MessageBox(title, content, self.window())
        w.exec()
          
    def findStart(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i][j] == 2:
                    return i, j
                
    def findEnd(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i][j] == 3:
                    return i, j
            
class Node:
    def __init__(self, x=0, y=0, step=0):
        self.x = x
        self.y = y
        self.step = step
        
class DFSWorker(QThread):
    updateSignal_color = pyqtSignal(int, int, str)
    updateSignal_text = pyqtSignal(int, int, str)
    updateSignal_icon = pyqtSignal(int, int, int)
    updateSignal_end = pyqtSignal(bool)
    
    def __init__(self, grid, list, start_i, start_j, end_i, end_j):
        super().__init__()
        self.grid = grid
        self.list = list
        self.start_i = start_i
        self.start_j = start_j
        self.end_i = end_i
        self.end_j = end_j
        
        self.is_sccuess = False
        
    def DFS(self, i ,j, end_i, end_j):
        if i == end_i and j == end_j:
            self.is_sccuess = True
            return True
        for k in range(4):
            xx, yy = i + dir[k][0], j + dir[k][1]
            if self.in_map(xx, yy):
                if self.list[xx][yy] != 1 and self.list[xx][yy] != 2:
                    if self.grid.getButtonText(i, j).isdigit():
                        self.updateSignal_text.emit(xx, yy, str(int(self.grid.getButtonText(i, j)) + 1))
                    if self.list[xx][yy] == 0:
                        self.updateSignal_color.emit(xx, yy, "blue")
                        sleep(0.05)
                        self.updateSignal_color.emit(xx, yy, "yellow")
                    if self.list[xx][yy] != 3 and self.list[xx][yy] != 2:
                        self.list[xx][yy] = 1
                    if self.DFS(xx, yy, end_i, end_j):
                        if self.list[xx][yy] != 3:
                            self.updateSignal_color.emit(xx, yy, "pink")
                            self.updateSignal_icon.emit(xx, yy, k)
                            sleep(0.05)
                        return True
        
        self.updateSignal_color.emit(i, j, "blue")
        sleep(0.05)
        self.updateSignal_color.emit(i, j, "purple")
        self.updateSignal_text.emit(i, j, None)
        return False
    
    def in_map(self, x, y):
        return 0 <= x < len(self.list) and 0 <= y < len(self.list)
    
    def run(self) -> None:
        self.DFS(self.start_i, self.start_j, self.end_i, self.end_j)