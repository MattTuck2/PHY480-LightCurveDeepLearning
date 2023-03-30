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

#import string
import numpy as np
import matplotlib.pyplot as plt
import pylab as p
import math
import os # use os library to specify machine-independent paths

# Short routine to determine whether an input string is either a number 
#  or not -- true or false. We use this to eliminate empty or bad data
#  values from the input file.

def is_number (s):
    try:
        float (s)
        return True
    except ValueError:
        return False


directory = os.path.join ("MANTRA", "data", "lightcurves")
inputfile  = os.path.join (directory, "transient_lightcurves.csv")

# Flag to indicate verbosity of output (0 non-verbose, 1 verbose)

verbose = 0

# Open data file for reading

f = open (inputfile, 'r')

# Inititalize data lists

id_list = []
obid_list = []
mag_list = []
magerr_list = []
mjd_list = []

# Read data in line by line

for line in f:

        if (verbose == 1) :
           print (line),

        if line.startswith("#") :
           pass # do nothing
        else :

           lst = line.split (',')

           idstr = lst [0]
           obidstr = lst [1]
           magstr = lst [2]
           magerrstr = lst [3]
           mjdstr = lst [4]

# Reject non-numerical entries - typically blank in Hipparcos

           if is_number (obidstr) and is_number (magstr) and is_number (magerrstr) and is_number (mjdstr):

             #id = float (idstr)
             objd = float (obidstr)
             mag = float (magstr)
             magerr = float (magerrstr)
             mjd = float (mjdstr)
            

             id_list.append (idstr)
             obid_list.append (objd)
             mag_list.append (mag)
             magerr_list.append (magerrstr)
             mjd_list.append (mjdstr)

# Convert to numpy arrays from python lists.

idno = np.array (id_list)
objd = np.array (obid_list)
mag = np.array (mag_list)
magerr = np.array (magerr_list)
mjd = np.array (mjd_list)

# Generate plot.

plt.ylabel ('Magnitude')
plt.xlabel ('Object Identification Number')
ax = plt.gca()

plt.plot (obid_list, mag, 'ko', markersize = 1)

outputfile = 'mantra_plot.png'
plt.savefig (outputfile, format = 'png', dpi = 300)
plt.close ()
