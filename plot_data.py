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
    ax.plot(data.index, index, '.', data=data)
    ax.plot(data.index, index, data=data, alpha=0.3)
    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    years_fmt = mdates.DateFormatter('%Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)
    fig.autofmt_xdate()
    plt.title(f'Annual plot: {index}')
    plt.grid(True, alpha=0.5)
    plt.show()

def monthly_plot(data, index):
    fig, ax = plt.subplots()
    ax.plot(data.index, index, '.', data=data)
    ax.plot(data.index, index, data=data, alpha=0.3)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.5)
    plt.title(f'Monthly plot: {index}')
    plt.show()

def histplot(data, index):
    sns.distplot(data[index], kde=False)
    plt.title(f'Histogramplot plot: {index}')
    plt.show()



index = 'PRCP'
annual_data = df.select_annual(index)
annual_plot(annual_data, index)
histplot(annual_data, index)


index = 'TMAX'
month_data = df.select_month(index, 2001, 4)
month_data[index] = (month_data[index]-32)*5/9
histplot(month_data, index)
monthly_plot(month_data, index)