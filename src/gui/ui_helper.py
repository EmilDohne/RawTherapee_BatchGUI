'''
Helper file for packing the .ui files into the executable using pyinstaller --onefile
'''
import sys, os, time

# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

