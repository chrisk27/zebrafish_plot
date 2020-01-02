"""
This module contains all of the functions for plotting the zebrafish experiments.
It contains simple plotters that will work for one array at a time, and more complex ones that will allow for size adjustment.
The more complex ones should be allowed for us to make animations.
"""


import numpy as np
import matplotlib.pyplot as plt


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
    if (final_size[0] < sim_size[0]) | (final_size[1] < sim_size[1]) :
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

