'''
Copyright (c) 2023, Emil Dohne
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

import os

import src.util.logger as logger

def make_dir(directory: str, assert_is_empty = True):
    '''
    Convenience function for checking if a directory exists before creating it,
    if assert_is_empty is true an extra check is added that the directories are empty
    before trying to create them, raises a warning if the directories are not empty
    '''
    if not os.path.isdir(directory):
        # Error handling is done through os.mkdir itself
        os.mkdir(directory)

    if assert_is_empty:
        if not len(os.listdir(directory)) == 0:
            logger.log_warning("Directory {} is not empty, program will continue".format(directory))
            
    return directory
        

def crawl(directory: str, raw_extension: str) -> list[str]:
    '''
    Crawls an input directory and returns all folders that contain the specified raw extension
    '''
    if not os.path.isdir(directory):
        logger.log_error("directory {} is not a valid path".format(directory))
        return
    
    # List of all the paths that contain files with the raw_extension
    path_list = []

    # Recursively find folders that contain files which 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(raw_extension):
                path_list.append(root)
                break 
    
    return path_list


def create_output_map(directories: list[str], output_root: str, add_subfolder = False) -> dict[str]:
    '''
    Creates a mapping of a given input directory such that 
    {input_directory: output_directory,
    ...}, if any folders are missing they will be generated on the fly
    '''
    mapping_dict = {}
    for dir in directories:
        # Check if all the directories are still there
        if not os.path.isdir(dir):
            raise RuntimeError("Directory {} is not accessible, was it deleted or renamed?")
        
        # Get the actual folder name itself
        folder_name = os.path.basename(dir)

        # Make a directory at output_root/folder_name
        # if add_subfolder add another dir at output_root/folder_name/folder_name
        output_folder = make_dir(os.path.abspath(os.path.join(output_root, folder_name)))
        if add_subfolder:
            output_folder = make_dir(os.path.abspath(os.path.join(output_root, folder_name, folder_name)))
        
        mapping_dict[dir] = output_folder
    return mapping_dict
