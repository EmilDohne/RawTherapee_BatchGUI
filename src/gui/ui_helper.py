'''
Copyright (c) 2023, Emil Dohne
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''
'''
Helper file for packing the .ui files into the executable using pyinstaller --onefile
'''
import sys, os

# Define function to import external files when using PyInstaller.
# Credit to giran from this thread
# https://stackoverflow.com/questions/37888581/pyinstaller-ui-files-filenotfounderror-errno-2-no-such-file-or-directory
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

