import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import time
import argopy

def plot_temp_vs_latitude():

    try :
        df_raw = pd.read_csv('data.csv')
    except :
        print("Importing data...")
        t0 = time.time()
        ArgoSet = argopy.DataFetcher().region([-180,180,-90,90, 0, 5, '2015-01', '2015-02'])
        print("Time to import : ", time.time()-t0)
        ds = ArgoSet.data.argo.point2profile().to_dataframe()
        print("Time to get data from DataFetcher : ", time.time()-t0)
        ds.to_csv('data.csv')

    # Remove rows where temp is None

    df = df_raw.dropna(subset=['TEMP'])

    # Define the variables to work with:
    temp = np.array(df['TEMP'])
    lat = np.array(df['LATITUDE'])

    plt.scatter(lat, temp, s=1)
    plt.grid(True)

    plt.title('Temperature Vs. Latitude')

    # Adding labels to the axes
    plt.xlabel('Latitude')
    plt.ylabel('Temperature')

    plt.savefig('figures/temp_vs_latitude.png')
    plt.show()


if __name__ == "__main__":
    plot_temp_vs_latitude()