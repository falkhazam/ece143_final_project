from argopy import ArgoIndex  #  This is the class to work with Argo index content
from argopy import ArgoNVSReferenceTables  # This is the class to retrieve data from Argo reference tables
from argopy.plot import scatter_map  # This is a function to easily make maps 
import argopy
import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__" :

    argopy.set_options(src='erddap', dataset='phy', mode='standard')

    ArgoSet = argopy.DataFetcher().region([-180,180,-90,90, 0, 10, '2011-01', '2011-06'])
    ds = ArgoSet.data.argo.point2profile().to_dataframe()
    df = ArgoSet.index

    # Define a parameter to work with:
    param = 'TEMP'
    # print(len(ds[param]))
    fig, ax = scatter_map(ds,
                          hue=param,
                          figsize=(10,6),
                          set_global=True,
                          traj=False,
                          markersize=2,
                          markeredgecolor=None,
                          legend_title='Temp'
                   )
    plt.show()


# # Get more verbose information about this parameter (usefull for plot titles):
# reftbl = ArgoNVSReferenceTables().tbl('R03')
# param_info = reftbl[reftbl['altLabel']==param].iloc[0]

# # Export search results to a dataframe:
# df = idx.to_dataframe()

# # To make the scatter map, we need to have the data mode available in one DataFrame column
# # so we need to add a new column with the DATA_MODE of the PARAMETER:
# df["variables"] = df["parameters"].apply(lambda x: x.split())
# df["%s_DM" % param] = df.apply(lambda x: x['parameter_data_mode'][x['variables'].index(param)] if param in x['variables'] else '', axis=1)


# # Finally plot the map:
# fig, ax = scatter_map(df,
#                       hue="%s_DM" % param,
#                       cmap="data_mode",
#                       figsize=(10,6),
#                       markersize=2,
#                       markeredgecolor=None,
#                       traj=False,
#                       set_global=False,
#                       legend_title='%s data mode' % param
#                     )
# ax.set_title("Data mode for '%s' (%s)\n%s profiles from the %s" % (param_info['prefLabel'], 
#                                                                    param, 
#                                                                    "{:,}", 
#                                                                    idx.convention_title)
#             )
# plt.show()