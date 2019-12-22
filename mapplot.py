import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap, shiftgrid
import time


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
    m = Basemap(projection="cyl")

    if draw_graticule:
        parallels = np.arange(-90, 90 + parallel_s, parallel_s)
        meridians = np.arange(-180, 180 + meridian_s, meridian_s)
        m.drawparallels(parallels, labels=[1, 0, 0, 0], color="#62757f", linewidth=0.5)
        m.drawmeridians(meridians, labels=[1, 0, 0, 1], color="#62757f", linewidth=0.5)

    m.drawcountries()
    m.drawcoastlines()

    x, y = m(*np.meshgrid(lons, lats))
    color = m.pcolor(
        x, y, data.squeeze(), cmap="RdYlBu_r", edgecolors="k", linewidth=0.01
    )
    m.colorbar(color, location="bottom", pad="10%")

    if save_file:
        plt.savefig(f"result_{int(time.time())}.png", dpi=dpi * 1.5)

    plt.show()
