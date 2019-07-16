import numpy as np
import pandas as pd
from datetime import datetime
from FormatData import FormatData as FD

fd = FD('./data/1951-2019.csv', 'NAKHON SAWAN, TH')
t = fd.select_annual('TAVG')
base = fd.select_annual('TAVG')[76:364]

base_prcp = base.groupby(base.index.month)['PRCP'].mean()
base_tavg = base.groupby(base.index.month)['TAVG'].mean()
base_tmax = base.groupby(base.index.month)['TMAX'].mean()
base_tmin = base.groupby(base.index.month)['TMIN'].mean()

col_list = ['month', 'PRCP', 'TAVG', 'TMAX', 'TMIN']

df = pd.DataFrame({
    'month': base_prcp.index,
    'PRCP': base_prcp,
    'TAVG': base_tavg,
    'TMAX': base_tmax,
    'TMIN': base_tmin
}, columns=col_list)

print(df)

df.to_csv('./data/base_nakhon_sawan.csv', index=False, sep=',')