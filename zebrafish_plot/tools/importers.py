"""
This module holds all of the importing functions, from a single import all the way into the directory import.
Hopefully this works in the long run.
"""

import os
import fnmatch
import numpy as np

def import_csv(filepath):  # Imports array from csv
    """This function imports the .csv file into a numpy array"""
    if not(isinstance(filepath, str)):  # Checks for string input
        print("Error: Invalid filepath type")
        return

    elif not(os.path.isfile(filepath)):  # Check if it's a file (will use different functions for animations)
        print("Error: No such file exists")
        return
    
    else:
        return np.genfromtxt(filepath, delimiter = ',')


def pull_images(basepath):  # Pulls a list of all file names that fit the criteria of "img_xxxx.csv"
    """This function outputs a list of the files we want to import from the directory 'basepath'"""
    file_list = []
    for file_name in os.listdir(basepath):
        if fnmatch.fnmatch(file_name, 'img*.csv'):
            file_list.append(file_name)
    file_list.sort()
    return file_list




