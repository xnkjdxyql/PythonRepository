import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.show()

app =QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()

