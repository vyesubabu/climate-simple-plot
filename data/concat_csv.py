import numpy as np
import pandas as pd

files = ['1951-1959', '1960-1969', '1970-1979', '1980-1989', '1990-1999', '2000-2009', '2010-2019']

concatenated = pd.concat([pd.read_csv(f+'.csv') for f in files])

print(concatenated.shape)

print(concatenated.head())

concatenated.to_csv('1951-2019.csv', index=False)