import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid

# Monthly maximum value of daily minimum temperature
ds = Dataset(
    './data/GHCND_TNx_1951-2019_RegularGrid_global_2.5x2.5deg_LSmask.nc',
    'r')

# list of month Jan .. Dec
months = list(ds.variables.keys())[3:-1]

# base line
baseline_start = 1961
baseline_end = 1991
start_year = 1951
end_year = 2019
start_index = baseline_start - start_year
end_index = baseline_end - start_year
num_baseline_year = baseline_end - baseline_start

# calculate baseline
baseline = 0
for m in months:
    baseline += np.nansum(ds[m][start_index:end_index], axis=0)
# mean of 12 month * num_baseline_year
baseline = baseline/(num_baseline_year*12)
print(f'baseline shape: {baseline.shape}')

# calculate mean of data
data = 0
for m in months:
    data += np.nansum(ds[m][:], axis=0)
data = data/((end_year-start_year)*12)
print(f'data shape: {data.shape}')

# calculate anomaly
anomaly = data - baseline
print(f'anomaly shape: {anomaly.shape}')

# Visualize map
fig = plt.figure(figsize=(9, 5))
m = Basemap(projection='cyl')
lats = ds['lat']
lons = ds['lon']
# shifted lon
lons = np.arange(-180, 180, 2.5)
shifted_lon = np.roll(lons, 72)
graticule_res = 10
parallels = np.arange(min(lats), max(lats)+1, graticule_res)
meridians = np.arange(min(lons), max(lons)+1, graticule_res)
m.drawparallels(parallels,
                labels=[1, 0, 0, 0], color="#62757f", linewidth=0.5)
m.drawmeridians(meridians,
                labels=[1, 0, 0, 1], color="#62757f", linewidth=0.5)
m.drawcountries()
m.drawcoastlines()

x, y = m(*np.meshgrid(shifted_lon, lats))
color = m.pcolor(x, y, anomaly.squeeze(), cmap='RdYlBu_r')
m.colorbar(color, location='bottom', pad='10%')
plt.title('TNx Anomaly')
plt.show()
