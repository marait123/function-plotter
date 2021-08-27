
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QPixmap


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("qt_designer.ui", self)
        self.btnPlot.clicked.connect(self.hello)

    def hello(self):
        print("hello world")


app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
