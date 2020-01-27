"""
This script creates plots to visualize the results of simulations of the differential growth model.
Later on, it will also be used to visualize other models that work with discrete systems.

This script starts by importing a csv file of the results, creates a plot, shows it, and then exports it as a png to the same folder it started in.
Ideally, I would love to add a file search GUI, but I'm not sure if I'll get there.
Will later add in support for visualizing where the iridophores were located, making spacetime plots, and making animations (once I add growth).
"""

import numpy as np
import math
import os
import imageio
import matplotlib.pyplot as plt

from tools import importers, plotters, STPlotter

if __name__ == '__main__':

    # Get information for importing
    sims2itOver = []  # Will store path to directories I need to plot in here
    basepath = '/home/chris/projects/difgrow_mc_sims/'
    datepath = '20_01_25/'  # For now I'll have to change this manually. Will iterate through each sim run per day though
    dirPath = basepath + datepath
    for item in os.listdir(dirPath):
        fullSimPath = dirPath + item
        if os.path.isdir(fullSimPath):
            sims2itOver.append(fullSimPath + "/")


    # Loop over every simulation you want to analyze
    for sim in sims2itOver:

        # Create output directory
        imgDir = sim + '/Images/'
        if not os.path.exists(imgDir):
            os.mkdir(imgDir)
            img_list = importers.pull_images(sim)
            final_img = importers.import_csv(sim + img_list[-1])
            final_size = final_img.shape

            # Initialize ST plot
            rowCutSize = final_size[1]
            rowCutLoc = int(math.ceil(final_size[0] / 2))
            colCounter = 0
            space_time = STPlotter.stPlotEmptyTemplate(rdim = rowCutSize, cdim = len(img_list))

            # Initialize animation
            animatedList = []

            # Fill output directory with images
            for item in img_list:

                # Import proper plot
                sim_array = importers.import_csv(sim + item)
                
                # Add to Space-Time plot
                if sim_array.ndim == 2:
                    cut = sim_array[rowCutLoc, :]
                elif sim_array.ndim ==1:
                    cut = np.array([sim_array[rowCutLoc]])
                else:
                    cut = np.array([0])
                filledCut = STPlotter.fillSlice(cut, desired_size=rowCutSize)
                space_time[:, colCounter] = filledCut
                colCounter += 1

                # Save as its own figure
                image = plotters.plot_to_size(sim_array, final_size)
                save_name = item.replace('.csv', '.png')
                save_name = imgDir + save_name
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

                # Add to list of images for animation
                animatedList.append(imageio.imread(save_name))

            # Process ST plot
            finalST = STPlotter.plotST(space_time)
            STName = imgDir + '/SpaceTimePlot.png'
            plt.figure()
            plt.axes(frameon=False)
            ax = plt.subplot(111)
            ax.set_ylabel('Space')
            ax.set_xlabel('Time')
            ax.imshow(finalST)
            plt.savefig(STName, bbox_inches='tight')
            plt.close()

            # Make animations
            animName = imgDir + '/Animation.gif'
            imageio.mimsave(animName, animatedList, fps = 50)

        
        
        
















