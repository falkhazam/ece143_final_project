import argopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time
import cartopy.crs as ccrs



if __name__ == "__main__" :

    argopy.set_options(src='erddap', dataset='phy', mode='standard')

    # if reading data for the first time, uncomment the following 7 lines :
    # print("Importing data...")
    # t0 = time.time()
    # ArgoSet = argopy.DataFetcher().region([-180,180,-90,90, 0, 5, '2015-01', '2015-02'])
    # print("Time to import : ", time.time()-t0)
    # ds = ArgoSet.data.argo.point2profile().to_dataframe()
    # print("Time to get data from DataFetcher : ", time.time()-t0)
    # ds.to_csv('data.csv')

    # if getting the data from a csv file, uncomment the following 1 line :
    df = pd.read_csv('data.csv')

    # Define the variables to work with:
    temp = np.array(df['TEMP'])
    lat = np.array(df['LATITUDE'])
    long = np.array(df['LONGITUDE'])

    # print("data available: ", df.columns)

    # print("Plotting data...")

    fig = plt.figure()
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    global_temp = ax.scatter(long, lat, c=temp)

    # levels = np.linspace(temp.min(), temp.max(), 20)
    # global_temp = ax.contourf(long, lat, temp, levels=levels)

    # title and label :
    cbar = fig.colorbar(global_temp, location='bottom')
    cbar.set_label('Celsius')
    ax.set_title('Sea Surface Temperature')
    gridlines = ax.gridlines(draw_labels=True)
    
    plt.savefig('figures/global_temp.png')
    plt.show()
