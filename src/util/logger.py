'''
Logs information to the Window through the UIs sysOutLabel
'''
import gui.window

def log_info(input: str):
    if gui.window.UI_INST:
        gui.window.UI_INST.ui.sysOutLabel.setStyleSheet(r"QLabel {background-color: rgb(30, 30, 30); color: rgb(201, 201, 201)}")
        gui.window.UI_INST.ui.sysOutLabel.setText(str(input))

def log_warning(input: str):
    if gui.window.UI_INST:
        gui.window.UI_INST.ui.sysOutLabel.setStyleSheet(r"QLabel {background-color: rgb(30, 30, 30); color: rgb(255, 165, 0)}")
        gui.window.UI_INST.ui.sysOutLabel.setText(str(input))

def log_error(input: str):
    if gui.window.UI_INST:
        gui.window.UI_INST.ui.sysOutLabel.setStyleSheet(r"QLabel {background-color: rgb(30, 30, 30); color: rgb(255, 0, 0)}")
        gui.window.UI_INST.ui.sysOutLabel.setText(str(input))