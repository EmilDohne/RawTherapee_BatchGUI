import os
import sys
from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui

import core.generate_directories as crawl_dir
import core.run
import util.logger as logger

# Holds a reference to the main UI instance
UI_INST = None

class MainUI(QtWidgets.QWidget):

    def __init__(self, parent=None, ui_file=None):
        super().__init__(parent)
        self.setWindowTitle("Raw Therapee Batch GUI")
        self.setGeometry(0, 0, 600, 500)

        self._input_folder: str = ""
        self._output_folder: str = ""
        self._create_subfolder: bool = False
        self._processing_profile: str = ""
        self._raw_file_format: str = "3FR"

        self.ui_file = ui_file
        self.init_ui(ui_file)
        self.create_layout()
        self.create_connections()
        self.center_ui()

    # --------------------------------------------------------------------------------
    # Qt Signal setters
    # --------------------------------------------------------------------------------
    '''
    Validation of inputs is not handled here but in the functions called themselves
    '''

    def set_input_folder(self):
        value = self.ui.inputLineEdit.text()
        self._input_folder = str(value).strip()
    
    def set_output_folder(self):
        value = self.ui.outputLineEdit.text()
        self._output_folder = str(value).strip()

    def set_create_subfolder(self):
        value = self.ui.addFolderCheckBox.isChecked()
        self._create_subfolder = bool(value)

    def set_processing_profile(self):
        value = self.ui.processingProfileLineEdit.text()
        self._processing_profile = str(value).strip()

    def set_raw_file_format(self, index: int):
        value = self.ui.rawFormatComboBox.itemText(index)
        self._raw_file_format = str(value).strip()
        
    # --------------------------------------------------------------------------------
    # UI Init
    # --------------------------------------------------------------------------------

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

    def create_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)

    def create_connections(self):
        self.ui.inputLineEdit.editingFinished.connect(self.set_input_folder)
        self.ui.outputLineEdit.editingFinished.connect(self.set_output_folder)
        self.ui.addFolderCheckBox.stateChanged.connect(self.set_create_subfolder)
        self.ui.processingProfileLineEdit.editingFinished.connect(self.set_processing_profile)
        self.ui.rawFormatComboBox.currentIndexChanged.connect(self.set_raw_file_format)

        self.ui.runPushButton.pressed.connect(self.run)

    def center_ui(self):
        screenGeometry = QtGui.QGuiApplication.screens()[0].availableGeometry()
        x = (screenGeometry.width() - self.width()) / 2
        y = (screenGeometry.height() - self.height()) / 2
        self.move(x,y)


    # --------------------------------------------------------------------------------
    # UI funcs
    # --------------------------------------------------------------------------------
    
    def increment_progress_bar(self):
        '''
        Increments the UIs progress bar as well as its adjacent QLabel
        '''

        # Get the progress Label to the right of the progress bar
        progress_str:str = self.ui.progressLabel.text()
        progress_lst = progress_str.split("/")
        # Increment value
        curr_value = int(progress_lst[0]) + 1
        self.ui.progressBar.setValue(curr_value)
        # set the Label to the updated value
        progress_lst[0] = str(curr_value)
        progress_str = "/".join(progress_lst)
        self.ui.progressLabel.setText(progress_str)


    def run(self):
        crawled_dirs = crawl_dir.crawl(self._input_folder, self._raw_file_format)
        dir_mapping = crawl_dir.create_output_map(crawled_dirs, self._output_folder, self._create_subfolder)
        # Update progress bar
        self.ui.progressLabel.setText("0/{}".format(len(dir_mapping)))
        self.ui.progressBar.setMaximum(len(dir_mapping))
        self.ui.progressBar.setValue(0)

        core.run.rawtherapee_cli(dir_mapping, self._processing_profile)
