import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, shiftgrid

df = pd.read_csv('./data/1951-2019.csv')
stations = df[['NAME', 'LATITUDE', 'LONGITUDE']].drop_duplicates()

stations_lat = np.array(stations['LATITUDE'][:])
stations_lon = np.array(stations['LONGITUDE'][:])
stations_name = np.array(stations['NAME'][:])


ds = Dataset('./data/T2m_pr_day_MPI-ESM-MR_historical.197001.nc')
lats = ds['lat'][:]
lons = ds['lon'][:]


lats_step = 180/len(lats)
lons_step = 360/len(lons)

# Shift lon from 0..360 to -180..180
# data is arrange at 0..360 so need to shift data too
lons = np.roll(lons, int(len(lons)/2))
lons[:int(len(lons)/2)] -= 360
data = ds['tas'][0][:] - 273
data = np.roll(data, int(len(lons)/2), axis=1)

lons += lons_step
lats += lats_step

fig = plt.figure(figsize=(9, 7))
m = Basemap(projection='cyl')

parallel_grid_res = 10
meridians_grid_res = 10
parallels = np.arange(-90, 90+parallel_grid_res, parallel_grid_res)
meridians = np.arange(-180, 180+meridians_grid_res, meridians_grid_res)
m.drawparallels(parallels,
                labels=[1, 0, 0, 0], color="#62757f", linewidth=0.5)
m.drawmeridians(meridians,
                labels=[1, 0, 0, 1], color="#62757f", linewidth=0.5)
m.drawcountries()
m.drawcoastlines()

x, y = m(*np.meshgrid(lons, lats))
sx, sy = m(stations_lon, stations_lat)
color_map = 'RdYlBu_r'
color = m.pcolor(x, y, data.squeeze(), cmap='RdYlBu_r',
                 edgecolors='k', linewidths=0.2, alpha=0.5)
m.colorbar(color, location='bottom', pad='10%')


for i in range(len(sx)):
    plt.scatter(sx[i], sy[i], 20, marker='o')

# plot interest station loc
s_name = 'CHIANG MAI, TH'
s = stations[stations['NAME'] == s_name]
s_x, s_y = m(s['LONGITUDE'], s['LATITUDE'])
plt.scatter(s_x, s_y, 50, marker='X', label=s_name)

plt.legend()
plt.show()
