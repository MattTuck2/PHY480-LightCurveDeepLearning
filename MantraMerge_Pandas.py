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
example_object_id = 1409030010044114444
print(light_curves[light_curves['ID'] == example_object_id])

print ('Merging with transient labels.')

#
# read in the CSV file for transient labels
inputfile = os.path.join (directory, 'transient_labels.csv')

classifications = pd.read_csv(inputfile)

# rename columns
classifications.columns = ['Classification', 'TransientID']

# create a dictionary to search for Classification by TransientID
#transient_dict = classifications.to_dict ('records')

# example usage of the dictionary; classification should be a single 'SN?'
#transient_id =  1409030010044114444

# Search the dictionary for the matching Name entry
#matching_records = [record for record in transient_dict if record['TransientID'] == transient_id]

# Print the matching records
#print(matching_records)

#Merge the two dataframes on the 'TransientID' column
merged_df = pd.merge(light_curves, classifications, left_on='ID', right_on='TransientID', how='left')

# add a 'Classification' column to the existing dataframe
light_curves ['Classification']= merged_df ['Classification']

# write the updated dataframe to the existing CSV file
light_curves.to_csv('transient_lightcurves.csv', header = ['#ID','observation_id','mag','magerr','MJD','Classification'], index=False)


