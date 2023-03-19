'''
Main application entry point
'''

import sys
from PySide6 import QtWidgets

import src.gui.window

VERSION = "0.1.0"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    src.gui.window.UI_INST = src.gui.window.MainUI()
    src.gui.window.UI_INST.show()
    app.exec()
