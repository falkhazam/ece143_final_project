import numpy as np
import argopy as argo

def get_argo() :
    '''
    currently just implements the first code in the argo docs to make sure it works
    '''
    ds = argo.DataFetcher().region([-75, -45, 20, 30, 0, 100, '2011-01', '2011-06']).to_xarray()

    return ds


if __name__ == "__main__" :
    print(get_argo())