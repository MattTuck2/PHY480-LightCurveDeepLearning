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

directory = os.path.join ("MANTRA", "data", "lightcurves")
inputfile = os.path.join (directory, "transient_lightcurves.csv")

light_curves = reader.read_light_curve_data(inputfile)

# Access a specific light curve data by object ID
example_object_id = 'TranID1409030010044114444'
light_curve_data = light_curves.get_group(example_object_id)

selected_data = light_curve_data[['observation_id', 'mag']]

print(selected_data)


# Add labels and a legend to the plot
#plt.xlabel('ObjID')
#plt.ylabel('Magnitude')
#plt.legend()

# Show the plot
#plt.show()

#outputfile = 'mantra_plot.png'
#plt.savefig (outputfile, format = 'png', dpi = 300)
#plt.close ()
