"""
This module holds functions that will generate space-time plots, both from a 3D array (overlaying all of the 2D arrays into 1 large array)
or from a bunch of 2D arrays directly (add data one at a time). It will also contain a typical plotting function, to view at the end.
"""

import numpy as np
import math
import matplotlib.pyplot as plt


def stPlotFrom3Dmat(array3D, rowChoice = None, colChoice = None):
    """
    This function creates a 2D space-time plot (needs to be colored later) from a 3D matrix.
    Will return error if input matrix is not 3D.

    Allows user to specify rowChoice or colChoice for the slicing.
    If neither rowChoice or colChoice is selected, will default to middle row.
    If both contain values, will default to rowChoice (essentially ignores colChoice).
    """

    if array3D.ndim != 3:  # If not a 3D array
        print("Error: input array is not 3 dimensional")
        return
    
    if not (rowChoice or colChoice):  # If neither are given values, go with middle row
        rowChoice = int(math.ceil(array3D.shape[0] / 2))

    if not rowChoice:  # If colChoice is selected
        return array3D[:, colChoice, :]

    else: 
        return array3D[rowChoice, :, :]


def stPlotEmptyTemplate(rdim, cdim):
    """Creates a blank (filled with 10s for coloring) array to fill in STplot Data"""
    return 10 * np.ones((rdim, cdim))


def fillSlice(cut, desired_size = None):
    """This function fills a slice of a matrix to an appropriate size, so it can be plugged into an ST plot"""
    if not desired_size:
        return cut
    elif len(cut) == 1:
        out = 10 * np.ones(desired_size)
        out[0] = cut
        return out
    elif len(cut) <= desired_size:
        out = 10 * np.ones(desired_size)
        out[0:len(cut)] = cut
        return out
    else:
        return cut[0:desired_size]


def plotST(STarray):
    """
    This function plots a space-time plot-converting the 2D STarray into a 3D RGB array.
    
    Colors are as follows:
    White indicates empty/dead cells (S in model)
    Yellow indicates xanthophores (X in model)
    Black indicates melanophores (M in model)
    Blue indicates empty space, that isn't any sort of cell.
    """

    outArray = np.zeros((STarray.shape[0], STarray.shape[1], 3))
    outArray[:,:,2] = np.ones((STarray.shape[0], STarray.shape[1]))  # defaults all values to blue ([0, 0, 1])
    outArray[STarray == 0, :] = [1, 1, 1]  # White for dead/empty cells
    outArray[STarray == 1, :] = [1, 1, 0]  # Yellow for xanthophores
    outArray[STarray == 2, :] = [0, 0, 0]  # Black for melanophores

    return outArray


        


