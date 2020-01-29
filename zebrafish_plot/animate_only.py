"""
This module is just to animate simulaitons that have already been perfomed and made images out of,
since animation has been added as a default to the main function.

This script reads in a bunch of files as .png, and then makes a gif out of them.

You will need to manually enter in the file path, as well as change any settings.
"""

import numpy as np
import math
import os
import imageio


if __name__ == '__main__':

    # Get information for importing
    sims2itOver = []  # Will store path to directories I need to plot in here
    basepath = '/home/chris/projects/difgrow_mc_sims/'
    datepath = '20_01_21/'  # For now I'll have to change this manually. Will iterate through each sim run per day though
    dirPath = basepath + datepath
    for item in os.listdir(dirPath):
        fullSimPath = dirPath + item
        if os.path.isdir(fullSimPath):
            sims2itOver.append(fullSimPath + "/")

    for sim in sims2itOver:
        
        # Check and then load Image directory
        imgDir = sim + 'Images/'
        if os.path.isdir(imgDir):
            animateList = []

            # Read in all of the images
            for img in sorted(os.listdir(imgDir)):
                if (img.endswith('png') and not img.startswith('SpaceTimePlot')):
                    imgPath = imgDir + img
                    animateList.append(imageio.imread(imgPath))
            
            # Make and save animation
            animFile = imgDir + 'Animation.gif'
            imageio.mimwrite(animFile, animateList, fps = 50)
        
        else:
            print("Failure: no image file exists. Use zebrafish_plot.py to create images")