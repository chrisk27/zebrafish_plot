"""
This script creates plots to visualize the results of simulations of the differential growth model.
Later on, it will also be used to visualize other models that work with discrete systems.

This script starts by importing a csv file of the results, creates a plot, shows it, and then exports it as a png to the same folder it started in.
Ideally, I would love to add a file search GUI, but I'm not sure if I'll get there.
Will later add in support for visualizing where the iridophores were located, making spacetime plots, and making animations (once I add growth).
"""

import numpy as np
import os.path
from os import path
import matplotlib.pyplot as plt


def import_csv(filepath):  # Imports array from csv
    """This function imports the .csv file into a numpy array"""
    if not(isinstance(filepath, str)):  # Checks for string input
        print("Error: Invalid filepath type")
        return

    elif not(path.isfile(filepath)):  # Check if it's a file (will use different functions for animations)
        print("Error: No such file exists")
        return
    
    else:
        return np.genfromtxt(filepath, delimiter = ',')


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


if __name__ == '__main__':
    filename = '/home/chris/projects/basedifgrow/tmpOutput.csv'
    simulation = import_csv(filename)
    base = sim_to_plot(simulation)
    base_img = simple_plotter(simulation, base)
    plt.imshow(base_img)
    plt.show()














