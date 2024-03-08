# Introduction:
Welcome to Group 4's ECE 143 final project. Here is a collection of code dedicated to plotting sea temperature data at various geographic locations as well as depth profiles.

## File Descriptions:

1. correlation_heatmap.py - correlation heatmap of parameters
2. currents.py - global current vectors from buoy dispalcement (small time scale)
3. global_temp.py - SST around the globe
4. temp_vs_depth.py - normalized temp vs depth plots (similar to latitude plot, split into latitude bins first and normalize each bin to remove latitude dependency)
5. temp_vs_latitude - normalized temp vs latitude plots (normalized wrt longitude, maybe average the temp across each line of latitude? i.e. splitinto 180 latitude bins and average each bin before normalizing)
6. temp_vs_time - CA coast temp vs time plots


## Getting Started


### Dependencies:

1. [argopy](https://github.com/euroargodev/argopy) - can be installed with "pip install argopy" or conda
2. [matplotlib](https://matplotlib.org/) - can be installed with "pip install matplotlib" or conda
3. [numpy](https://numpy.org/) - can be installed with "pip install numpy" or conda
4. [cartopy](https://scitools.org.uk/cartopy/docs/latest/) - can be installed with "pip install cartopy" or conda
5. [Ipython](https://ipython.org/) - can be installed with "pip install Ipython" or conda
6. Python3.9.x

### Installation

_Getting the code on your machine can be done in one step._

1. Clone the repo
   ```sh
   git clone https://github.com/falkhazam/ece143_final_project.git
   ```


## Usage

_All the files are run in a similar manner._

- To generate the sea surface temperature plots on a global scale run:
    ```
    python global_temp.py
    ```


## Resources:

1. [Euro-Argo Github Page](https://github.com/euroargodev)
2. [Matplotlib Documentation](https://matplotlib.org/stable/users/index)
3. [Argopy Documentation](https://argopy.readthedocs.io/en/latest/)

## Data:
1. [Argo](https://argo.ucsd.edu/data/)
2. [CDIP](https://cdip.ucsd.edu/themes/cdip?zoom=auto&tz=UTC&ll_fmt=dm&numcolorbands=10&palette=cdip_classic&high=6.096&r=999&un=1&pb=1&d2=p70)



## Tasks:

### Week 1
- [x] Make private Github repository for easy group work
- [x] Figure out which modules would help us the most
- [X] Data allocation (select datasets, write code to import data into best format to work with)

### Week 2
- [x] Visualize data, look for trends
- [x] Find best sections of data to focus on for the presentation

### Week 3
- [x] Plot global temperature at various depths
- [x] Plot average temperature vs latitude
- [x] Plot average temperature vs depth
- [x] Plot temperature vs time on the California Coast
- [x] Plot interpolation of currents from buoy displacement
- [x] Plot correlation heatmap
- [x] Make presentation
