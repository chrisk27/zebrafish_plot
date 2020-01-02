"""
This script creates plots to visualize the results of simulations of the differential growth model.
Later on, it will also be used to visualize other models that work with discrete systems.

This script starts by importing a csv file of the results, creates a plot, shows it, and then exports it as a png to the same folder it started in.
Ideally, I would love to add a file search GUI, but I'm not sure if I'll get there.
Will later add in support for visualizing where the iridophores were located, making spacetime plots, and making animations (once I add growth).
"""

import numpy as np
import os
import matplotlib.pyplot as plt

from tools import importers, plotters

if __name__ == '__main__':
    filename = '/home/chris/projects/growdifgrow/csvOutputs/img_0001.csv'
    simulation = importers.import_csv(filename)
    base_img = plotters.plot_to_size(simulation, (100, 100))
    plt.imshow(base_img)
    plt.show()














