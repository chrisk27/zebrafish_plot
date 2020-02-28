"""
This module contains all of the functions for plotting the zebrafish experiments.
It contains simple plotters that will work for one array at a time, and more complex ones that will allow for size adjustment.
The more complex ones should be allowed for us to make animations.
"""


import numpy as np
import matplotlib.pyplot as plt
import math


def sim_to_plot(sim_array):
    """This function outputs an array of the correct size to work with matplotlib.pyplot's imshow"""
    twoDshape = sim_array.shape
    imgDims = (twoDshape[0], twoDshape[1], 3)
    return np.zeros(imgDims, dtype=np.float32)


def simple_plotter(sim_array, plot_array):
    """
    This function fills the plot array with values (0-1) for the coloring of the different chromaphores.

    For the simple case, the following is observed:
        White pixels are empty nodes ('S' in original paper, 0 in sim_array)
        Yellow pixels are xanthophores ('X' in original paper, 1 in sim_array)
        Black pixels are melanophores ('M' in original paper, 2 in sim_array)
    """
    if (sim_array.shape[0] == plot_array.shape[0]) & (sim_array.shape[1] == plot_array.shape[1]):
        plot_array[sim_array == 0, :] = [1, 1, 1]
        plot_array[sim_array == 1, :] = [1, 1, 0]
        plot_array[sim_array == 2, :] = [0, 0, 0]
        return plot_array
    else:
        print("Error: plot and simulation dimensions do not match")
        return


def plot_to_size(sim_array, final_size):
    """
    This function preallocates an array of size final_size (should be a tuple) and fills it with the appropriate pixel values.
    For the pixels that are actually in the sim_array, will follow color scheme listed in simple_plotter.
    For pixels that are outside of the realm of the sim_array, they will be plotted in blue.
    """
    plot_array = np.zeros((final_size[0], final_size[1], 3))
    plot_array[:, :, 2] = np.ones(final_size)  # makes everything blue (will overlay later)
    sim_size = sim_array.shape

    if sim_array.ndim == 0 :  # If just one value
        if sim_array == np.array(0):
            plot_array[0, 0, :] = [1, 1, 1]
        elif sim_array == np.array(1):
            plot_array[0, 0, :] = [1, 1, 0]
        elif sim_array == np.array(2):
            plot_array[0, 0, :] = [0, 0, 0]
        return plot_array
    
    elif ((sim_array.ndim == 1) & (len(sim_array) <= final_size[0])) :  # If just a shorter vector
        for i in range(len(sim_array)):
            if sim_array[i] == 0:
                plot_array[i, 0, :] = [1, 1, 1]
            elif sim_array[i] == 1:
                plot_array[i, 0, :] = [1, 1, 0]
            elif sim_array[i] == 2:
                plot_array[i, 0, :] = [0, 0, 0]
        return plot_array
  

    elif ((sim_array.ndim == 1) & (len(sim_array) > final_size[0])) :
        print("Error: wrong final dimension size chosen")
        return

    elif (final_size[0] < sim_size[0]) | (final_size[1] < sim_size[1]) :
        print("Error: wrong final dimension size chosen")
        return

    else:
        for i in range(sim_size[0]):
            for j in range(sim_size[1]):
                if sim_array[i, j] == 0:
                    plot_array[i, j, :] = [1, 1, 1]
                elif sim_array[i, j] == 1:
                    plot_array[i, j, :] = [1, 1, 0]
                elif sim_array[i, j] == 2:
                    plot_array[i, j, :] = [0, 0, 0]
        return plot_array


def plot_centering(sim_array, final_size):
    """
    This function will plot the sim_array into a matrix of size final_size. It will be plotted into the center of the final matrix.
    Then, just as normal plotting, it will color the output matrix in accordance with the simple_plotter function.
    sim_array should be a 2D array, and final_size should be a tuple. The output will be a 3D RGB array.
    """

    plot_array = np.zeros((final_size[0], final_size[1], 3))
    plot_array[:, :, 2] = np.ones(final_size) # makes everything blue, will overlay later
    sim_size = sim_array.shape
    final_center = [np.floor((final_size[0] -1) / 2), np.floor((final_size[1] - 1) / 2)]
    
    #  Here is where we figure out the centering
    if sim_array.ndim ==0:
        row_shift = final_center[0]
        col_shift = final_center[1]
    elif len(sim_array.shape) == 1:  # If a 1D column
        row_shift = final_center[0]
        col_shift = final_center[1] - np.floor((sim_size[0] - 1) / 2)
    elif sim_array.ndim == 2:  # If either a 1D row or a 2D array
        row_shift = final_center[0] - np.floor((sim_array.shape[0] - 1) / 2)
        col_shift = final_center[1] - np.floor((sim_array.shape[1] - 1) / 2)
    else:
        print("Error on sizing")
        return
    
    #  Now, fill in the plot as needed
    if sim_array.ndim == 0:
        if sim_array == np.array(0):
            plot_array[int(row_shift), int(col_shift), :] = [1, 1, 1]
        elif sim_array == np.array(1):
            plot_array[int(row_shift), int(col_shift), :] = [1, 1, 0]
        elif sim_array == np.array(2):
            plot_array[int(row_shift), int(col_shift), :] = [0, 0, 0]
        return plot_array

    elif ((sim_array.ndim == 1) & (len(sim_array) <= final_size[0])) :  # If just a shorter vector
        for i in range(len(sim_array)):
            if sim_array[i] == 0:
                plot_array[int(i + row_shift), int(col_shift), :] = [1, 1, 1]
            elif sim_array[i] == 1:
                plot_array[int(i + row_shift), int(col_shift), :] = [1, 1, 0]
            elif sim_array[i] == 2:
                plot_array[int(i + row_shift), int(col_shift), :] = [0, 0, 0]
        return plot_array
    
    elif ((sim_array.ndim == 1) & (len(sim_array) > final_size[0])) :
        print("Error: wrong final dimension size chosen")
        return

    elif (final_size[0] < sim_size[0]) | (final_size[1] < sim_size[1]) :
        print("Error: wrong final dimension size chosen")
        return

    else:
        for i in range(sim_size[0]):
            for j in range(sim_size[1]):
                if sim_array[i, j] == 0:
                    plot_array[int(i + row_shift), int(j + col_shift), :] = [1, 1, 1]
                elif sim_array[i, j] == 1:
                    plot_array[int(i + row_shift), int(j + col_shift), :] = [1, 1, 0]
                elif sim_array[i, j] == 2:
                    plot_array[int(i + row_shift), int(j + col_shift), :] = [0, 0, 0]
        return plot_array
    

def plot_grow2D_right(sim_array, final_size):
    """
    This function will plot the sim_array into a matrix of size final_size. It will be plotted into the center of the rows, but the left column will be
    on the left of the domain, so it's always growing on one side.
    Then, just as normal plotting, it will color the output matrix in accordance with the simple_plotter function.
    sim_array should be a 2D array, and final_size should be a tuple. The output will be a 3D RGB array.
    """

    plot_array = np.zeros((final_size[0], final_size[1], 3))
    plot_array[:, :, 2] = np.ones(final_size) # makes everything blue, will overlay later
    sim_size = sim_array.shape
    row_center = np.floor((final_size[0] -1) / 2)
    
    #  Here is where we figure out the centering
    if sim_array.ndim ==0:
        row_shift = row_center
    elif len(sim_array.shape) == 1:  # If a 1D column
        row_shift = row_center - np.floor((sim_size[0] - 1) / 2)
    elif sim_array.ndim == 2:  # If either a 1D row or a 2D array
        row_shift = row_center - np.floor((sim_size[0] - 1) / 2)
    else:
        print("Error on sizing")
        return

    #  Now, fill in the plot as needed
    if sim_array.ndim == 0:
        if sim_array == np.array(0):
            plot_array[int(row_shift), 0, :] = [1, 1, 1]
        elif sim_array == np.array(1):
            plot_array[int(row_shift), 0, :] = [1, 1, 0]
        elif sim_array == np.array(2):
            plot_array[int(row_shift), 0, :] = [0, 0, 0]
        return plot_array

    elif ((sim_array.ndim == 1) & (len(sim_array) <= final_size[0])) :  # If just a shorter vector
        for i in range(len(sim_array)):
            if sim_array[i] == 0:
                plot_array[int(i + row_shift), 0, :] = [1, 1, 1]
            elif sim_array[i] == 1:
                plot_array[int(i + row_shift), 0, :] = [1, 1, 0]
            elif sim_array[i] == 2:
                plot_array[int(i + row_shift), 0, :] = [0, 0, 0]
        return plot_array
    
    elif ((sim_array.ndim == 1) & (len(sim_array) > final_size[0])) :
        print("Error: wrong final dimension size chosen")
        return

    elif (final_size[0] < sim_size[0]) | (final_size[1] < sim_size[1]) :
        print("Error: wrong final dimension size chosen")
        return

    else:
        for i in range(sim_size[0]):
            for j in range(sim_size[1]):
                if sim_array[i, j] == 0:
                    plot_array[int(i + row_shift), j, :] = [1, 1, 1]
                elif sim_array[i, j] == 1:
                    plot_array[int(i + row_shift), j, :] = [1, 1, 0]
                elif sim_array[i, j] == 2:
                    plot_array[int(i + row_shift), j, :] = [0, 0, 0]
        return plot_array


def plot_grow2D_left(sim_array, final_size):
    """
    This function will plot the sim_array into a matrix of size final_size. It will be plotted into the center of the rows, but the right column will be
    on the right of the domain, so it's always growing on one side. It's basically the other-side alternate to the above function.
    Then, just as normal plotting, it will color the output matrix in accordance with the simple_plotter function.
    sim_array should be a 2D array, and final_size should be a tuple. The output will be a 3D RGB array.
    """

    plot_array = np.zeros((final_size[0], final_size[1], 3))
    plot_array[:, :, 2] = np.ones(final_size) # makes everything blue, will overlay later
    sim_size = sim_array.shape
    row_center = np.floor((final_size[0] -1) / 2)
    
    #  Here is where we figure out the centering
    if sim_array.ndim ==0:
        row_shift = row_center
    elif len(sim_array.shape) == 1:  # If a 1D column
        row_shift = row_center - np.floor((sim_size[0] -1) / 2)
    elif sim_array.ndim == 2:  # If either a 1D row or a 2D array
        row_shift = row_center - np.floor((sim_size[0] - 1) / 2)
    else:
        print("Error on sizing")
        return

    #  Now, fill in the plot as needed
    if sim_array.ndim == 0:
        if sim_array == np.array(0):
            plot_array[int(row_shift), -1, :] = [1, 1, 1]
        elif sim_array == np.array(1):
            plot_array[int(row_shift), -1, :] = [1, 1, 0]
        elif sim_array == np.array(2):
            plot_array[int(row_shift), -1, :] = [0, 0, 0]
        return plot_array

    elif ((sim_array.ndim == 1) & (len(sim_array) <= final_size[0])) :  # If just a shorter vector
        for i in range(len(sim_array)):
            if sim_array[i] == 0:
                plot_array[int(i + row_shift), -1, :] = [1, 1, 1]
            elif sim_array[i] == 1:
                plot_array[int(i + row_shift), -1, :] = [1, 1, 0]
            elif sim_array[i] == 2:
                plot_array[int(i + row_shift), -1, :] = [0, 0, 0]
        return plot_array
    
    elif ((sim_array.ndim == 1) & (len(sim_array) > final_size[0])) :
        print("Error: wrong final dimension size chosen")
        return

    elif (final_size[0] < sim_size[0]) | (final_size[1] < sim_size[1]) :
        print("Error: wrong final dimension size chosen")
        return

    else:
        offset = final_size[1] - sim_size[1]
        for i in range(sim_size[0]):
            for j in range(sim_size[1]):
                if sim_array[i, j] == 0:
                    plot_array[int(i + row_shift), offset + j, :] = [1, 1, 1]
                elif sim_array[i, j] == 1:
                    plot_array[int(i + row_shift), offset + j, :] = [1, 1, 0]
                elif sim_array[i, j] == 2:
                    plot_array[int(i + row_shift), offset + j, :] = [0, 0, 0]
        return plot_array