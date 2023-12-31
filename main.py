import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from interfaces.main_window import mainWindow

if __name__ == '__main__':
    
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    mainWindow()
    
    app.exec_()