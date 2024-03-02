import numpy as np
import argopy as argo

def get_argo() :
    '''
    currently just implements the first code in the argo docs to make sure it works
    :param : None
    '''
    f = argo.DataFetcher() #.region([-75, -45, 20, 30, 0, 100, '2011-01', '2011-06']).to_xarray()



    return


if __name__ == "__main__" :

    argo.set_options(src='erddap', dataset='phy', mode='standard')
    print(get_argo())

    print(argo.status())