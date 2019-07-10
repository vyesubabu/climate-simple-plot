import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
sns.set_context(font_scale=1.5)

data_file = './data/2000-2009.csv'
df = pd.read_csv(data_file, sep=',')
df = df.loc[df['NAME'] == "NAKHON SAWAN, TH"]
date = df['DATE']
tmax = df['TMAX'].fillna(-99.9)

tmax = tmax[tmax > -90]
tmax = round((tmax-32) * 5/9, 2)

fig = plt.figure(figsize=(9, 7))
sns.distplot(tmax, kde=False)
plt.show()