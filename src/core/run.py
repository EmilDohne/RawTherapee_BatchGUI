'''
Logic for getting the latest version of RawTherapee and then running the cli version of it
'''
import subprocess
import os

import util.logger
import gui.window

RAWTHERAPEE_INSTALL_LOC = r"C:\Program Files\RawTherapee"
RAWTHERAPEE_CLI_EXECUTABLE = "rawtherapee-cli.exe"

def _find_latest_rawtherapee() -> str:
    '''
    Find the latest install of rawtherapee on the system (crude implementation)
    if the install location changes this must be reflected here
    '''
    # TODO this implementation can and should be made more robust for future proofness
    rawtherapee_versions = os.listdir(RAWTHERAPEE_INSTALL_LOC)
    latest_version = sorted(rawtherapee_versions)[-1]
    return os.path.join(RAWTHERAPEE_INSTALL_LOC, latest_version, RAWTHERAPEE_CLI_EXECUTABLE)


def rawtherapee_cli(path_map: dict[str], processing_profile: str):
    # TODO run this in a seperate QThread to not block the UI completely
    # TODO this does not actually only process raw files, but all supported files
    '''
    Initiates a subprocess for each path pair in path_map with the processing profile if valid.
    Currently only writes out as zip compressed 16bit Tiffs, 
    #TODO add the ability to modify this
    '''
    has_processing_profile = True
    if not processing_profile.endswith(".pp3") or not os.path.isfile(processing_profile):
        util.logger.log_warning("Processing profile {} is not a valid profile file".format(processing_profile))
        has_processing_profile = False

    rawtherapee_install = _find_latest_rawtherapee().removesuffix(".exe")
    for key in path_map:
        util.logger.log_info("Began working on directory {}".format(key))
        if has_processing_profile:
            subprocess_call_list = [rawtherapee_install,
                                    "-o",
                                    path_map[key],
                                    "-p",
                                    processing_profile,
                                    "-tz",
                                    "-Y",
                                    "-f",
                                    "-c",
                                    key]
        else:
            subprocess_call_list = [rawtherapee_install,
                                    "-o",
                                    path_map[key],
                                    "-tz",
                                    "-Y",
                                    "-f",
                                    "-c",
                                    key]
        subprocess.call(subprocess_call_list)
        gui.window.UI_INST.increment_progress_bar()