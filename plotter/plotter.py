
import sys
from typing import List
from PySide2 import QtWidgets
from PySide2.QtGui import QIntValidator
from PySide2.QtWidgets import QDialog, QApplication, QLabel, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
# for metigating the notfounderror
try:
    from plotter.utils import GetAllowedChars, ErrorDialog, GetNumberInput, AddWidgetsToLayout, EvaluateExpression
except ModuleNotFoundError:
    from utils import GetAllowedChars, ErrorDialog, GetNumberInput, AddWidgetsToLayout, EvaluateExpression


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.allowedChars = GetAllowedChars()
        self.set_ui()

    def set_ui(self):
        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.btnPlot = QPushButton('Plot')
        self.btnPlot.setToolTip('press <b>Plot</b> to plot the function')
        self.btnPlot.clicked.connect(self.plot)

        self.lblMin = QLabel("enter min value")
        self.txtMin = GetNumberInput(0)

        self.lblMax = QLabel("enter max value: ")
        self.txtMax = GetNumberInput(100)

        self.lblEquation = QLabel("enter expression like x^2+3*x-5 : ")
        self.txtEquation = QLineEdit("x^2")

        # set the layout
        layout = AddWidgetsToLayout([self.lblMin,
                                     self.txtMin,
                                     self.lblMax,
                                     self.txtMax,
                                     self.lblEquation,
                                     self.txtEquation,
                                     self.btnPlot,
                                     self.canvas,
                                     self.toolbar], QVBoxLayout())
        self.setLayout(layout)
        self.setWindowTitle("function plotter")
        # print(" figure before", self.figure)
        # print(" self.before after  ", self.canvas)

    def plot(self):
        ''' plot the expression '''
        # random data

        rangeMin = int(self.txtMin.displayText().rstrip())
        rangeMax = int(self.txtMax.displayText().rstrip())
        expression = self.txtEquation.displayText()
        expression = expression.lower()
        for index, char in enumerate(expression):
            if char not in self.allowedChars:
                ErrorDialog({'title': 'expression syntax error',
                             'info': "character {} at index {} of expression isn't allowed ".format(char, index),
                             'detail': "there is a syntax error please recheck your expression and make sure you expression is valid like x^2+2*x+3",
                             })
                # print(
                #     "character {} at index {} of expression isn't allowed ".format(char, index))

        expression = expression.replace('^', '**')
        # check the expression
        try:
            data = EvaluateExpression(expression, rangeMin, rangeMax)
        except SyntaxError as se:
            ErrorDialog({'title': 'expression syntax error',
                         'info': "there is a syntax error",
                         'detail': "there is a syntax error please recheck your expression and make sure you expression is valid like x^2+2*x+3",
                         })
            return
        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")

        self.ax.plot(np.arange(rangeMin, rangeMax+1), data)
        self.ax.grid(True, which="both")
        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
