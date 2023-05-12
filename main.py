import sys

from PyQt5.QtWidgets import *
import PyQt5.QtGui as gui


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(500, 200, 300, 600)
        self.setWindowTitle("Calculator")
    


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(my_app.exec_())
