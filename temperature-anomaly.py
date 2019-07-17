import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pygal
from datetime import datetime

df = pd.read_csv('./data/1951-2019.csv')
df['DATE'] = pd.to_datetime(df['DATE'])

print(f'raw data head: \n{df.head()}\n')

# group by year
df1 = df.groupby(df['DATE'].dt.year)
df1 = df1.mean()

# select baseline 1961-1991
baseline = df1[11:42].mean()
print(f'baseline: \n{baseline}\n')

tavg_anomaly = df1['TAVG'] - baseline['TAVG']
print(f'anomaly head: \n{tavg_anomaly.head()}\n')

plt.title('AVG Temperature Anomaly, baseline: 1961-1991')
sns.lineplot(data=tavg_anomaly)
plt.grid(True, alpha=0.3)
plt.show()