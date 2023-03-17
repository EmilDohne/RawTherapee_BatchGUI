import os
import sys
from PySide6 import QtWidgets, QtCore, QtUiTools


class MainUI(QtWidgets.QWidget):

    def __init__(self, parent=None, ui_file=None):
        super().__init__(parent)
        self.setWindowTitle("Raw Therapee Batch GUI")
        self.setGeometry(0, 0, 600, 500)

        self.ui_file = ui_file

        self.init_ui(ui_file)


    def init_ui(self, ui_path: str) -> None:
        '''
        Loads a .ui file and parents it under the window
        '''
        if not ui_path:
            ui_path = "{0}/main.ui".format(os.path.dirname(__file__))

        file = QtCore.QFile(ui_path)
        file.open(QtCore.QFile.ReadOnly)
        file_loader = QtUiTools.QUiLoader()
        self.ui = file_loader.load(file, parentWidget=self)
        file.close()

if __name__ == "__main__":
    q_application = QtCore.QCoreApplication(sys.argv)
    ui = MainUI(None, os.path.join(os.getcwd(), "main.ui"))
    ui.show()
