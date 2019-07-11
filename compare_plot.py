import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from FormatData import FormatData as FD

sns.set(style="whitegrid")
sns.set_context(font_scale=1.5)

to_celcius = lambda x: (x-32)*5/9



def multiple_line(data, label, index):
    fig, ax = plt.subplots()
    for i in range(len(data)):
        d = data[i]
        ax.plot(d.index, index, data=d, label=label[i])

    years = mdates.YearLocator()
    months = mdates.MonthLocator()
    years_fmt = mdates.DateFormatter('%Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)
    fig.autofmt_xdate()
    plt.title(f'Annual plot: {index}')
    plt.grid(True, alpha=0.5)
    plt.legend()
    plt.show()



data_file = './data/2000-2019.csv'
station1 = 'NAKHON SAWAN, TH'
station2 = 'BANGKOK METROPOLIS, TH'

ns_df = FD(data_file, station1)
bk_df = FD(data_file, station2)

index = 'TAVG'
ns_annual = ns_df.select_annual(index)
bk_annual = bk_df.select_annual(index)
ns_annual[index] = to_celcius(ns_annual[index])
bk_annual[index] = to_celcius(bk_annual[index])

multiple_line([ns_annual, bk_annual], ["NAKHON SAWAN", "BANGKOK METROPOLIS"], index)