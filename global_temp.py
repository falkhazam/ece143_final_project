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

    # Define a parameters to work with:
    param = 'TEMP'
    lat = 'LATITUDE'
    long = 'LONGITUDE'

    print("data available: ", df.columns)

    print("Plotting data...")

    # print(list(ds[long]))
    # print(ds[lat])
    # print(ds[param])

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.scatter(list(df[long]), list(df[lat]), c=list(df[param]))
    
    plt.savefig('plot.png')
    plt.show()