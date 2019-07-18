import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pygal
from datetime import datetime
from sklearn.linear_model import LinearRegression
sns.set_style("whitegrid")
sns.set_palette("bright")
sns.set_context('notebook', font_scale=1.25, rc={"lines.linewidth": 3})

df = pd.read_csv('./data/1951-2019.csv')
df['DATE'] = pd.to_datetime(df['DATE'])

df2 = df
df2.index = df2['DATE']
annual_mean = df2.resample('M').mean()
# divide 1951 to 2019 into 2 parts
before = annual_mean[annual_mean.index < '1985-01-31']
after = annual_mean[annual_mean.index >= '1985-01-31']

sns.distplot(before['TAVG'], label='1951-1984')
sns.distplot(after['TAVG'], label='1985-2019')
plt.legend()
plt.show()