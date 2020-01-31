from sys import argv
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Hello world!")

app = QApplication(argv)
window = MainWindow()
window.show()
app.exec_()
