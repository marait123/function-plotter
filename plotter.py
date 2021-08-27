
import sys
from typing import List
from PySide2 import QtWidgets
from PySide2.QtGui import QIntValidator
from PySide2.QtWidgets import QDialog, QApplication, QLabel, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np


def getAllowedChars() -> List:
    """

    Returns
    -------
    list
        a list of characters that are allowed to exist in the expression

    """
    allowedChars = [str(i) for i in range(10)]
    for char in ["x", "-", "+", "*", "/", "^", " "]:
        allowedChars.append(char)
    return allowedChars


def errorDialog(message) -> int:
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(message['info'])
    msg.setWindowTitle(message['title'])
    msg.setDetailedText(message['detail'])
    msg.setStandardButtons(QMessageBox.Cancel)

    return msg.exec_()


def GetNumberInput(defaultValue) -> QLineEdit:
    input = QLineEdit(str(defaultValue))
    input.setValidator(QIntValidator())
    return input


def PrepareLayout(widgets: List, layout: QtWidgets.QBoxLayout) -> QtWidgets.QBoxLayout:
    for widget in widgets:
        layout.addWidget(widget)
    return layout


def EvaluateExpression(expression: str, rangeMin: int, rangeMax: int, step: float = 1) -> List:
    """
    Summary:
        this function applies the expression on every value in the range [rangeMin, rangeMax] withe step=step
    Parameters
    ----------
    expression : str
        the expression you want to apply on value in the range
    rangeMin : str
        the minimum value to start from in the arange
    rangeMax : int
        the maximum value to end at in the arange 
    step : int optional
        this is the range step default is 1
    """
    data = [eval(expression) for x in np.arange(rangeMin, rangeMax+step, step)]
    return data


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.allowedChars = getAllowedChars()
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

        lblMin = QLabel("enter min value")
        self.txtMin = GetNumberInput(0)

        lblMax = QLabel("enter max value: ")
        self.txtMax = GetNumberInput(100)

        lblEquation = QLabel("enter expression like x^2+3*x-5 : ")
        self.txtEquation = QLineEdit("x^2")

        # set the layout
        layout = PrepareLayout([lblMin,
                                self.txtMin,
                                lblMax,
                                self.txtMax,
                                lblEquation,
                                self.txtEquation,
                                self.btnPlot,
                                self.canvas,
                                self.toolbar], QVBoxLayout())
        self.setLayout(layout)
        self.setWindowTitle("function plotter")

    def plot(self):
        ''' plot some random stuff '''
        # random data

        rangeMin = int(self.txtMin.displayText().rstrip())
        rangeMax = int(self.txtMax.displayText().rstrip())
        expression = self.txtEquation.displayText()
        expression = expression.lower()
        for index, char in enumerate(expression):
            # print(char)
            if char not in self.allowedChars:
                # print("error allowed characters are ", self.allowedChars)
                errorDialog({'title': 'expression syntax error',
                             'info': "character {} at index {} of expression isn't allowed ".format(char, index),
                             'detail': "there is a syntax error please recheck your expression and make sure you expression is valid like x^2+2*x+3",
                             })
                print(
                    "character {} at index {} of expression isn't allowed ".format(char, index))

        expression = expression.replace('^', '**')
        # check the expression
        try:
            data = EvaluateExpression(expression, rangeMin, rangeMax)
        except SyntaxError as se:
            print("there is a syntax errors")
            print(se)
            errorDialog({'title': 'expression syntax error',
                         'info': "there is a syntax error",
                         'detail': "there is a syntax error please recheck your expression and make sure you expression is valid like x^2+2*x+3",
                         })
            return
        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        ax.plot(data)
        ax.grid(True, which="both")
        # refresh canvas
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
