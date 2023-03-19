'''
Copyright (c) 2023, Emil Dohne
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

'''
Logic for getting the latest version of RawTherapee and then running the cli executable in it with the appropriate arguments
'''
import subprocess
import os
from PySide6 import QtCore

import src.util.logger as logger
import src.gui.window as main_window


RAWTHERAPEE_INSTALL_LOC = r"C:\Program Files\RawTherapee"
RAWTHERAPEE_CLI_EXECUTABLE = "rawtherapee-cli.exe"

class RawtherapeeWorker(QtCore.QThread):

    def __init__(self, parent,
                 path_map: dict[str], 
                 processing_profile: str,
                 has_processing_profile: bool,
                 rawtherapee_install: str) -> None:
        super().__init__(parent)
        self.path_map = path_map
        self.processing_profile = processing_profile
        self.has_processing_profile = has_processing_profile
        self.rawtherapee_install = rawtherapee_install

    def run(self):
        for key in self.path_map:
            logger.log_info("Began working on directory {}".format(key))
            if self.has_processing_profile:
                subprocess_call_list = [self.rawtherapee_install,
                                        "-o",
                                        self.path_map[key],
                                        "-p",
                                        self.processing_profile,
                                        "-t",
                                        "-Y",
                                        "-f",
                                        "-c",
                                        key]
            else:
                subprocess_call_list = [self.rawtherapee_install,
                                        "-o",
                                        self.path_map[key],
                                        "-t",
                                        "-Y",
                                        "-f",
                                        "-c",
                                        key]
            subprocess.call(subprocess_call_list)
            main_window.UI_INST.increment_progress_bar()
        logger.log_success("Finished computing")


def _find_latest_rawtherapee() -> str:
    '''
    Find the latest install of rawtherapee on the system (crude implementation)
    if the install location changes this must be reflected here
    '''
    # TODO this implementation can and should be made more robust for future proofness
    rawtherapee_versions = os.listdir(RAWTHERAPEE_INSTALL_LOC)
    latest_version = sorted(rawtherapee_versions)[-1]
    return os.path.join(RAWTHERAPEE_INSTALL_LOC, latest_version, RAWTHERAPEE_CLI_EXECUTABLE)


def rawtherapee_cli(path_map: dict[str], processing_profile: str) -> RawtherapeeWorker:
    # TODO this does not actually only process raw files, but all supported files
    '''
    Initiates a subprocess for each path pair in path_map with the processing profile if valid.
    Currently only writes out as uncompressed 16bit Tiffs, 
    #TODO add the ability to modify this
    '''
    has_processing_profile = True
    if processing_profile != "":
        if not processing_profile.endswith(".pp3") or not os.path.isfile(processing_profile):
            logger.log_warning("Processing profile {} is not a valid profile file".format(processing_profile))
            return
    else:
        has_processing_profile = False

    rawtherapee_install = _find_latest_rawtherapee().removesuffix(".exe")

    # Initialize a new QThread for the blocking operation and execute the code there,
    # no return is necessary
    worker_thread = RawtherapeeWorker(None, path_map, processing_profile, has_processing_profile, rawtherapee_install)
    worker_thread.finished.connect(worker_thread.deleteLater)
    worker_thread.start()

    return worker_thread