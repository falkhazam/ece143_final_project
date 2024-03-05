import argopy
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

if __name__ == "__main__":
    # if getting the data from a csv file, uncomment the following 1 line :
    df_raw = pd.read_csv('data.csv')

    # Remove rows where temp is None

    df = df_raw.dropna(subset=['TEMP'])

    # Define the variables to work with:
    temp = np.array(df['TEMP'])
    lat = np.array(df['LATITUDE'])

    abs_lat = np.abs(lat)

    plt.scatter(abs_lat, temp, s=1)
    plt.grid(True)

    plt.title('Temperature Vs. Absolute Value of Latitude')

    # Adding labels to the axes
    plt.xlabel('|Latitude|')
    plt.ylabel('Temperature')

    plt.savefig('figures/temp_vs_abs(latitude).png')
    plt.show()


