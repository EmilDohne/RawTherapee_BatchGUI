'''
Logs information to the Window through the UIs sysOutLabel
'''
import src.gui.window as main_window

def log_info(input: str):
    if main_window.UI_INST:
        main_window.UI_INST.ui.sysOutLabel.setStyleSheet(r"QLabel {font: 8pt 'Consolas'; color: rgb(201, 201, 201)}")
        main_window.UI_INST.ui.sysOutLabel.setText(str(input))

def log_warning(input: str):
    if main_window.UI_INST:
        main_window.UI_INST.ui.sysOutLabel.setStyleSheet(r"QLabel {font: 8pt 'Consolas'; color: rgb(255, 165, 0)}")
        main_window.UI_INST.ui.sysOutLabel.setText(str(input))

def log_error(input: str):
    if main_window.UI_INST:
        main_window.UI_INST.ui.sysOutLabel.setStyleSheet(r"QLabel {font: 8pt 'Consolas'; color: rgb(255, 0, 0)}")
        main_window.UI_INST.ui.sysOutLabel.setText(str(input))

def log_success(input: str):
    if main_window.UI_INST:
        main_window.UI_INST.ui.sysOutLabel.setStyleSheet(r"QLabel {font: 8pt 'Consolas'; color: rgb(0, 255, 0)}")
        main_window.UI_INST.ui.sysOutLabel.setText(str(input))
