import argopy
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import pandas as pd
from datetime import datetime
import time

if __name__ == "__main__":
    # if getting the data from a csv file, uncomment the following 1 line :
    try:
        df_raw = pd.read_csv('data_CA_2015.csv')
    except:
        print("Importing data...")
        t0 = time.time()
        ArgoSet = argopy.DataFetcher().region([-124, -116, 32, 42, 0, 5, '2015-01', '2015-12'])
        print("Time to import : ", time.time() - t0)
        ds = ArgoSet.data.argo.point2profile().to_dataframe()
        print("Time to get data from DataFetcher : ", time.time() - t0)
        ds.to_csv('data_CA_2015.csv')
        df_raw = pd.read_csv('data_CA_2015.csv')

    # Remove rows where temp is None

    df = df_raw.dropna(subset=['TEMP'])

    # Define the variables to work with:
    temp = np.array(df['TEMP'])
    time_strings = np.array(df['TIME'])

    time = np.array([datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S') for time_string in time_strings])
    plt.grid(True)

    plt.title('Temperature Vs. Time (2015)')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B'))

    plt.scatter(time, temp, s=1)
    plt.grid(True)

    # Adding labels to the axes
    plt.xlabel('Month')
    plt.ylabel('Temperature')

    plt.savefig('figures/temp_vs_timeCA.png')
    plt.show()
