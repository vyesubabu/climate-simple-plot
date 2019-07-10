import numpy as np
import pandas as pd

class FormatData:
    def __init__(self, data_file, station):
        self.df = pd.read_csv(data_file)
        self.station = station
        # select data by station
        self.df = self.df[self.df['NAME'] == self.station]
        # format date column
        self.df['DATE'] = pd.to_datetime(self.df['DATE'])

    def select_annual(self, index):
        # select index data and drop null value
        data = self.df[self.df[index].notnull()]
        # set date as index
        data.index = data['DATE']
        # group data by month and drop null data
        annual_data = data.resample('M').mean()
        annual_data = annual_data[annual_data[index].notnull()]

        return annual_data

if __name__ == "__main__":
    data_file = './data/2000-2019.csv'
    station = 'NAKHON SAWAN, TH'
    df = FormatData(data_file, station)
    prcp = df.select_annual('PRCP')