# zebrafish_plot

Developed by Christopher Konow

This package will be used to visualize the results of discrete modelling of zebrafish simulations, such as the Differential Growth model. It is built using Python.

This package contains many functions that allows you to turn the .csv output of the MC_Simulation package into images and animations of the patterns developing and growing. The MC_Simulation package can also be found in the EpsteinLab Github page, but uses C++ instead of Python.

To use, run the main script "zebrafish_plot.py". It is critical to change the file name so that it points to the folder containing the .csv outputs.

When run, the script adds a subfolder to the folder containing the .csv files, and outputs the resulting images into this subfolder. The resulting images are .png files where the array values are converted into colored pixels with:

.csv array value --- color in .png file --- physical meaning
0 --- white --- empty cell (S)
1 --- yellow --- xanthophore (X)
2 --- black --- melanophore (M)
N/A --- blue --- Does not exist in current image, we fill in the difference between the current image and final image size as blue to allow for compilation into an animation

The zebrafish_plot.py script also has options to export animations compiling the .png image files into a .gif and form a space-time plot. In addition, there are many ways to plot and compile the images and animations. To see all options, look in the tools folder. Each function has a brief description of what it does.

If you have any questions on how the code contained within this package, please contact Chris Konow at ckonow@brandeis.edu