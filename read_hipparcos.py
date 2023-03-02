#!/usr/bin/python

#----------------------------------------------------------------------
#
# MANTRA Reader
#
# Takes Extended Hipparcos data (XHIP) directly input through an ASCII
#  text file, and processes it. Data source located at :
#     http://cdsarc.u-strasbg.fr/viz-bin/Cat?V/137D
#
# 
#
#----------------------------------------------------------------------

#import string
import numpy as np
import matplotlib.pyplot as plt
import pylab as p
import math

# Short routine to determine whether an input string is either a number 
#  or not -- true or false. We use this to eliminate empty or bad data
#  values from the input file.

def is_number (s):
    try:
        float (s)
        return True
    except ValueError:
        return False


inputfile = 'C:\Users\MattT\Downloads\MANTRA-master.zip\MANTRA-master\data\lightcurves'
#outputfile = 'plot.pdf'

#def generate_plot (inputfile, outputfile, plot_color):

# Flag to indicate verboity of output (0 non-verbose, 1 verbose)

verbose = 0

# Open data file for reading

f = open (inputfile, 'r')

# Inititalize data lists

id_list = []
obid_list = []
mag_list = []
magerr = []
mjd = []

# Read data in line by line

for line in f:

        if line.startswith("#") :
           if (verbose == 1) :
              print (line),
        else :

             lst = line.split ('|')

             #if (len (lst) > 37) :

                idstr = lst [0]
                obidstr = lst [1]
                magstr = lst [2]
                magerrstr = lst [3]
                mjdstr = lst [4]

# Reject non-numerical entries - typically blank in Hipparcos

                if is_number (obidstr) and is_number (magstr) and is_number (magerrstr) and is_number (mjdstr) ):

                   u = float (ustr)
                   v = float (vstr)
                   w = float (wstr)
                   age = float (agestr)
                   metal = float (metalstr)

                   u_list.append (u)
                   v_list.append (v)
                   w_list.append (w)
                   age_list.append (age)
                   metallicity_list.append (metal)

# Convert to numpy arrays from python lists.

u_velocity = np.array (u_list)
v_velocity = np.array (v_list)
w_velocity = np.array (w_list)

stellar_age = np.array (age_list)

metallicity = np.array (metallicity_list)

# Generate plot.

#   plt.plot (bminusv, MV, 'ko', markersize = 1)
plt.ylabel ('Metallicity [Fe/H]')
plt.xlabel ("Stellar Age")
ax = plt.gca()
#ax.set_yscale ('log')

plt.plot (stellar_age, metallicity, 'ko', markersize = 1)

plt.savefig (outputfile, format = 'pdf')
plt.close ()
