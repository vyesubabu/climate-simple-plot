import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

sns.set(style="whitegrid")
sns.set_context(font_scale=1.5)

data_file = './data/2000-2019.csv'
station = 'NAKHON SAWAN, TH'

df = pd.read_csv(data_file)
df = df[df['NAME'] == station]
df['DATE'] = pd.to_datetime(df['DATE'])


# drop prcp = null/nan
prcp_data = df[df['PRCP'].notnull()]

# set date as index
prcp_data.index = prcp_data['DATE']

# group prcp data by month, and drop null data
annual_prcp = prcp_data.resample('M').mean()
annual_prcp = annual_prcp[annual_prcp['PRCP'].notnull()]


years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y-%m')

fig, ax = plt.subplots()
ax.plot(annual_prcp.index, 'PRCP', 'b.', data=annual_prcp)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

plt.xticks(rotation=90)
ax.grid(True)
plt.show()