import sys
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication
import pytest

from pytestqt.qt_compat import qt_api

from . import plotter


@pytest.fixture
def dialog(qtbot):
    window = plotter.Window()
    window.show()
    qtbot.addWidget(window)
    return window


def test_plot_button(qtbot, dialog):
    assert not hasattr(dialog, 'ax')
    qtbot.mouseClick(dialog.btnPlot, QtCore.Qt.LeftButton)
    # qt_api.qWarning(str("warning "))
    assert dialog.ax.has_data()


def test_labels(qtbot, dialog):
    assert dialog.lblMin.text() == "enter min value"
    assert dialog.lblMax.text() == "enter max value: "
