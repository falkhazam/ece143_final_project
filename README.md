# File Descriptions:

1. correlation_heatmap.py - correlation heatmap of parameters
2. currents.py - global current vectors from buoy dispalcement (small time scale)
3. global_temp.py - SST around the globe
4. temp_vs_depth.py - normalized temp vs depth plots (similar to latitude plot, split into latitude bins first and normalize each bin to remove latitude dependency)
5. temp_vs_latitude - normalized temp vs latitude plots (normalized wrt longitude, maybe average the temp across each line of latitude? i.e. splitinto 180 latitude bins and average each bin before normalizing)
6. temp_vs_time - CA coast temp vs time plots


## Dependencies:

1. [argopy](https://github.com/euroargodev/argopy) - can be installed with "pip install argopy" or conda
2. [matplotlib](https://matplotlib.org/) - can be installed with "pip install matplotlib" or conda
3. [numpy](https://numpy.org/) - can be installed with "pip install numpy" or conda
4. [cartopy](https://scitools.org.uk/cartopy/docs/latest/) - can be installed with "pip install cartopy" or conda
5. [Ipython](https://ipython.org/) - can be installed with "pip install Ipython" or conda


## Resources:

1. [Euro-Argo Github Page](https://github.com/euroargodev)
2. [Matplotlib Documentation](https://matplotlib.org/stable/users/index)
3. [Argopy Documentation](https://argopy.readthedocs.io/en/latest/)

## Data:
1. [CDIP](https://cdip.ucsd.edu/themes/cdip?zoom=auto&tz=UTC&ll_fmt=dm&numcolorbands=10&palette=cdip_classic&high=6.096&r=999&un=1&pb=1&d2=p70)
2. [Argo](https://argo.ucsd.edu/data/)

## Notes:
I recommend we just stick to Argo Float data. There's a whole python library dedicated to using and visualizing the data, and CDIP is not as well documented and has weird file formats. -Gabriel

## Tasks:

### Week 1
- [x] Make private Github repository for easy group work
- [x] Figure out which modules would help us the most
- [X] Data allocation (select datasets, write code to import data into best format to work with)

### Week 2
- [x] Visualize data, look for trends
- [x] Find best sections of data to focus on for the presentation

### Week 3
- [ ] Plot global temperature at various depths
- [ ] Plot average temperature vs latitude
- [ ] Plot average temperature vs depth
- [ ] Plot temperature vs time on the California Coast
- [ ] Plot interpolation of currents from buoy displacement
- [ ] Plot correlation heatmap
- [ ] Make presentation
