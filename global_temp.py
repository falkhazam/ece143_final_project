import argopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time
import cartopy.crs as ccrs



# define parameters :

dates_list = [['2015-01', '2015-01'], ['2015-04', '2015-05'], ['2015-07', '2015-08'], ['2015-10', '2015-11']]
argopy.set_options(src='erddap', dataset='phy', mode='standard')

if __name__ == "__main__" :

    for i, dates in enumerate(dates_list) :

        file = 'data'+str(i)+'.csv'

        try :
            df = pd.read_csv(file)
        except :
            print("Importing data...")
            t0 = time.time()
            ArgoSet = argopy.DataFetcher().region([-180,180,-90,90, 0, 5] + dates)
            print("Time to import : ", time.time()-t0)
            ds = ArgoSet.data.argo.point2profile()
            print("Time to get data from DataFetcher : ", time.time()-t0)
            df = ds.to_dataframe()
            print("Time to convert : ", time.time()-t0)
            df.to_csv(file) 

        # Define the variables to work with:
        temp = np.array(df['TEMP'])
        lat = np.array(df['LATITUDE'])
        long = np.array(df['LONGITUDE'])

        print("Plotting data...")

        fig = plt.figure()
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.coastlines()
        global_temp = ax.scatter(long, lat, c=temp)

        # title and label :
        cbar = fig.colorbar(global_temp, location='bottom')
        cbar.set_label('Celsius')
        ax.set_title('Sea Surface Temperature' + ' ' + dates[0] + ' to ' + dates[1])
        gridlines = ax.gridlines(draw_labels=True) # shows lat/long
        
        plt.savefig('figures/global_temp' + str(i) + '.png')
        plt.show()