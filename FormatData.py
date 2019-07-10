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
        '''
            index: data index to format

            output: return formatted format dataframe
                - use <var>.index as date in x-axis
                - user 'INDEX' as value in y-axis
        '''
        # select index data and drop null value
        data = self.df[self.df[index].notnull()]
        # set date as index
        data.index = data['DATE']
        # group data by month and drop null data
        annual_data = data.resample('M').mean()
        annual_data = annual_data[annual_data[index].notnull()]

        return annual_data
    
    def select_month(self, index, year, month):
        data = self.df.loc[(self.df['DATE'].dt.month == month) & (self.df['DATE'].dt.year == year)]
        data = data[data[index].notnull()]
        data.index = data['DATE']

        return data


if __name__ == "__main__":
    data_file = './data/2000-2019.csv'
    station = 'NAKHON SAWAN, TH'
    df = FormatData(data_file, station)
    prcp = df.select_annual('PRCP')