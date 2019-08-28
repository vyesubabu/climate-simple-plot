import pandas as pd
import numpy as np

df = pd.read_csv('./1951-2019.csv')
stations = df['STATION'].drop_duplicates()

print(f'number of stations = {len(stations)}')

cnt = 0
for station_id in stations:
    station_data = df[df['STATION'] == station_id]
    station_name = np.array(station_data['NAME'])[0]
    # edit station name for use as file name
    station_name = station_name.split(', ')
    station_name = station_name[0].replace(
        ' ', '_') + '_' + station_name[1]
    station_data.to_csv(
        f'../station_data/{station_name}_1951-2019.csv', index=False)
    print(cnt, station_name)
    cnt += 1
