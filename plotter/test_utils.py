from PySide2.QtWidgets import QLineEdit
import pytest
import utils.utils as utils


def test_GetAllowedChars():
    assert 'x' in utils.GetAllowedChars()
    assert 'k' not in utils.GetAllowedChars()


# def test_GetNumberInput():
#     print(utils.GetNumberInput(400))
#     assert True
    # assert isinstance(utils.GetNumberInput(400), QLineEdit)


def test_EvaluateExpression():
    arr = utils.EvaluateExpression("x**2", 0, 2)
    assert arr[2] == 4
