import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, shiftgrid
import time
from matplotlib import cm

def plot_map(
    data,
    lons,
    lats,
    color_map="RdYlBu_r",
    parallel_s=20,
    meridian_s=20,
    draw_graticule=False,
    save_file=False,
    figsize=(9, 7),
    dpi=200,
):
    fig = plt.figure(figsize=figsize, dpi=dpi)
        
    margin = 5
    m = Basemap(projection="cyl", resolution='i', area_thresh=5000, llcrnrlon=np.min(lons)-margin,llcrnrlat=np.min(lats)-margin, urcrnrlon=np.max(lons)+margin, urcrnrlat=np.max(lats)+margin)

    if draw_graticule:
        parallels = np.arange(-90, 90 + parallel_s, parallel_s)
        meridians = np.arange(-180, 180 + meridian_s, meridian_s)
        m.drawparallels(parallels, labels=[1, 0, 0, 0], color="#62757f", linewidth=0.05)
        m.drawmeridians(meridians, labels=[1, 0, 0, 1], color="#62757f", linewidth=0.05)

    m.drawcountries(linewidth=0.1)
    m.drawcoastlines(linewidth=0.1)

    x, y = m(*np.meshgrid(lons, lats))
    color_res = 20
    ticks = np.linspace(np.min(data), np.max(data), int(color_res/2)+1)
    viridis = cm.get_cmap('RdYlBu_r', color_res)
    color = m.pcolor(
        x, y, np.round(data.squeeze(), 2), cmap=viridis, edgecolors="k", linewidth=0.01, vmin=np.min(data), vmax=np.max(data)
    )
    color_bar = m.colorbar(color, location="bottom", pad="10%", ticks=np.round(ticks, 2))
    color_bar.ax.tick_params(labelsize=6) 
    if save_file:
        plt.savefig(f"result_{int(time.time())}.png", dpi=dpi * 5)

    plt.show()
