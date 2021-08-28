from PySide2.QtWidgets import QLineEdit
import pytest
import plotter.utils as utils


def test_GetAllowedChars():
    assert 'x' in utils.GetAllowedChars()
    assert 'k' not in utils.GetAllowedChars()


def test_EvaluateExpression():
    arr = utils.EvaluateExpression("x**2", 0, 2)
    assert arr[2] == 4
