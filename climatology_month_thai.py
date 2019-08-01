import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pygal
from datetime import datetime
from sklearn.linear_model import LinearRegression
sns.set_style("whitegrid")
paired_color = sns.color_palette("Paired")
sns.set_palette("Paired")
sns.set_context('notebook', font_scale=1, rc={"lines.linewidth": 3})

df = pd.read_csv('./data/1951-2019.csv')
df['DATE'] = pd.to_datetime(df['DATE'])

df2 = df
df2.index = df2['DATE']
annual_mean = df2.resample('M').mean()

# divide 1951 to 2019 into 2 parts
before = annual_mean[annual_mean.index < '1985-01-31']
after = annual_mean[annual_mean.index >= '1985-01-31']

# group by month in 1..12
before_m = before.groupby(before.index.month).mean()
after_m = after.groupby(after.index.month).mean()

x = before_m.index
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
              'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fig = plt.figure(figsize=(9, 6))
sns.lineplot(x, before_m['TAVG'], label='TAVG 1951-1984')
sns.lineplot(x, after_m['TAVG'], label='TAVG 1985-2019')
sns.lineplot(x, before_m['TMIN'], label='TMIN 1951-1984')
sns.lineplot(x, after_m['TMIN'], label='TMIN 1985-2019')
sns.lineplot(x, before_m['TMAX'], label='TMAX 1951-1984')
sns.lineplot(x, after_m['TMAX'], label='TMAX 1985-2019')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.xticks(list(range(1, 13)), month_list)
plt.savefig('monthly-climatology.png', dpi=150)
plt.show()

print('before avg DTR')
print(np.mean(before['TMAX'] - before['TMIN']))
print('after avg DTR')
print(np.mean(after['TMAX'] - after['TMIN']))


sns.lineplot(x, before_m['PRCP'], label='PRCP 1951-1984')
sns.lineplot(x, after_m['PRCP'], label='PRCP 1985-2019')
plt.xlabel('Month')
plt.ylabel('PRCP')
plt.xticks(list(range(1, 13)), month_list)
plt.show()
