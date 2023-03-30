import pandas as pd

def read_light_curve_data(file_path):
    # Define the column names
    column_names = ['ID', 'observation_id', 'mag', 'magerr', 'MJD']

    # Read CSV file into a DataFrame
    data = pd.read_csv(file_path, sep=',', header=None, names=column_names, comment='#')

    # Organize the data by object ID
    organized_data = data.groupby('ID')

    return organized_data
