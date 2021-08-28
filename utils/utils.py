
import sys
from typing import List
from PySide2 import QtWidgets
from PySide2.QtGui import QIntValidator
from PySide2.QtWidgets import QDialog, QApplication, QLabel, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np


def GetAllowedChars() -> List:
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


def ErrorDialog(message) -> int:
    """
    Parameters
    ----------
    message : dict
        the message object you want to display in the form as below
        {
            'title':"<title>",
            'info':'<info>',
            'detail':'<detail>'
        }

    Returns
    -------
    int
        the integer represents the exit state of the message box 
        you can check the integer validity by comparing it to QMessageBox.Cancel
    """

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(message['info'])
    msg.setWindowTitle(message['title'])
    msg.setDetailedText(message['detail'])
    msg.setStandardButtons(QMessageBox.Cancel)

    return msg.exec_()


def GetNumberInput(defaultValue) -> QLineEdit:
    """
    Parameters
    ----------
    defaultValue : int
        the value that is displayed on the input initially

    Returns
    -------
    QLineEdit
        the the QLineEdit that only accepts numbers as input
    """

    input = QLineEdit(str(defaultValue))
    input.setValidator(QIntValidator())
    return input


def AddWidgetsToLayout(widgets: List, layout: QtWidgets.QBoxLayout) -> QtWidgets.QBoxLayout:

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
