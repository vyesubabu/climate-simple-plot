import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pygal
from datetime import datetime
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./data/1951-2019.csv')
df['DATE'] = pd.to_datetime(df['DATE'])

# fill null PRCP value with 0
df['PRCP'] = df['PRCP'].fillna(0)


print(f'raw data head: \n{df.head()}\n')

# group by year
df1 = df.groupby(df['DATE'].dt.year)
df1 = df1.mean()

# select baseline 1961-1991
start_year = 1961
end_year = 1991
mask = (df1.index >= start_year) & (df1.index <= end_year)
baseline = df1.loc[mask].mean()
print(f'baseline: \n{baseline}\n')

index = 'TAVG'
title = f'{index} Anomaly, baseline: {start_year}-{end_year}'

anomaly = df1[index] - baseline[index]
print(f'anomaly head: \n{anomaly.head()}\n')

plt.title(title)
sns.scatterplot(data=anomaly)
sns.lineplot(data=anomaly, alpha=0.5)
plt.grid(True, alpha=0.3)

x = np.array(anomaly.index).reshape(-1, 1)
y = np.array(anomaly)
regression = LinearRegression().fit(x, y)
plt.plot(x, x*regression.coef_+regression.intercept_)
print(f'{regression.coef_}*x + {regression.intercept_}')
plt.show()
