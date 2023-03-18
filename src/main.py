import os
import sys
from PySide6 import QtWidgets

import gui.window

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui.window.UI_INST = gui.window.MainUI()
    gui.window.UI_INST.show()
    app.exec()
