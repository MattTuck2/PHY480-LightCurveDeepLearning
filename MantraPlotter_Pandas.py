#!/usr/bin/python

#----------------------------------------------------------------------
#
# Many ANnotated TRAnsients (MANTRA) Reader. See paper for more 
#  (DOI 10.3847/1538-4365/aba267).
#
# Read in MANTRA transient light curve data.
#
#  Matt Tuck, Vangjel Kutella, and Robert Fisher, 3/27/23
#
#----------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import os # use os library to specify machine-independent paths
import pandas as pd
import reader

# Read in the MANTRA dataset in CSV format, store in a Pandas DataFrame.
inputfile = os.path.join ("transient_lightcurves.csv")
light_curves = reader.read_light_curve_data(inputfile)

# Access the DataFrame a specific light curve data by object ID. The returned object will consist of all rows in the DataFrame matching the object ID.
example_object_id = 1409030010044114444
object = light_curves[light_curves['ID'] == example_object_id]

# Convert the MJD and mag columns into numpy arrays.

MJD = object ['MJD'].values
mag = object ['mag'].values

# Plot the magnitude and date.

plt.plot (MJD, mag, '-ok', markersize=4)

plt.xlabel ('MJD')
plt.ylabel ('Magnitude')

plt.title ('Magnitude versus MJD for MANTRA ID ' + str (example_object_id) )
outputfile = 'mantra_plot.png'
plt.savefig (outputfile, format = 'png', dpi = 300)
plt.close ()
