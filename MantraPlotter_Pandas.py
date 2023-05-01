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

inputfile = os.path.join ("transient_lightcurves.csv")

light_curves = reader.read_light_curve_data(inputfile)

# Access a specific light curve data by object ID
example_object_id = 1409030010044114444
object = light_curves[light_curves['ID'] == example_object_id]


MJD = object ['MJD'].values
mag = object ['mag'].values

plt.plot (MJD, mag, '-ok', markersize=4)


outputfile = 'mantra_plot.png'
plt.savefig (outputfile, format = 'png', dpi = 300)
plt.close ()
