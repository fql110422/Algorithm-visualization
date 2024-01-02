import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class MatplotlibFigure(FigureCanvas):
    def __init__(self, width=10, heigh=10, dpi=100):
        plt.rcParams['figure.facecolor'] = 'w' # 设置窗体颜色
        plt.rcParams['axes.facecolor'] = 'w' # 设置绘图区颜色
        self.figs = Figure(figsize=(width, heigh), dpi=dpi)
        super(MatplotlibFigure, self).__init__(self.figs) # 在父类种激活self.fig， 否则不能显示图像
        self.axes = self.figs.add_subplot(111)