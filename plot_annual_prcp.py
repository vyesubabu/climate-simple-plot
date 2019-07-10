import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from FormatData import FormatData as FD

sns.set(style="whitegrid")
sns.set_context(font_scale=1.5)

data_file = './data/2000-2019.csv'
station = 'NAKHON SAWAN, TH'

df = FD(data_file, station)


def annual_plot(data, index):
    fig, ax = plt.subplots()
    ax.plot(data.index, index, data=data)
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    years_fmt = mdates.DateFormatter('%Y-%m')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)
    plt.xticks(rotation=90)
    ax.grid(True)
    plt.show()

def histplot(data, index):
    sns.distplot(data[index], kde=False)
    plt.show()


index = 'PRCP'
annual_data = df.select_annual(index)
annual_plot(annual_data, index)

histplot(annual_data, index)