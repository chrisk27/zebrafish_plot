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

    # Get information for importing
    basepath = '/home/chris/projects/growdifgrow/csvOutputs/'
    img_list = importers.pull_images(basepath)
    final_img = importers.import_csv(basepath + img_list[-1])
    final_size = final_img.shape

    # Create output directory
    if not os.path.exists('/home/chris/projects/growdifgrow/csvOutputs/Images/'):
        os.mkdir('/home/chris/projects/growdifgrow/csvOutputs/Images/')
    
    # Fill output directory with images
    for item in img_list:
        sim_array = importers.import_csv(basepath + item)
        image = plotters.plot_to_size(sim_array, final_size)
        save_name = item.replace('.csv', '.png')
        save_name = '/home/chris/projects/growdifgrow/csvOutputs/Images/' + save_name
        plt.figure()
        plt.axes(frameon=False)
        ax = plt.subplot(111)
        ax.imshow(image)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.tick_params(bottom="off", left='off')
        plt.savefig(save_name, bbox_inches='tight')
        plt.close()
















