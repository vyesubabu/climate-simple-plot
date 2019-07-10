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
annual_data = df.select_annual('PRCP')


years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y-%m')

fig, ax = plt.subplots()
ax.plot(annual_data.index, 'PRCP', 'b.', data=annual_data)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

plt.xticks(rotation=90)
ax.grid(True)
plt.show()