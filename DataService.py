import numpy as np


def concat_year(data_arr):
    """
        data_arr: numpy array of data in [year x [lon x col]]

        concatenate n year of [row x col]
        to
        [row x col] but each col element is [data_y1, data_y2 ...]
    """
    concat_year = []
    for row in range(int(data_arr.shape[1])):
        row_data = []
        for col in range(int(data_arr.shape[2])):
            row_data.append(data_arr[:, row, col])
        concat_year.append(row_data)
    return np.array(concat_year)


def count_available_data(concat_data, nan_data=-99.9):
    """
        count available data of each element in concatenated data

        return: np array of available data count
    """
    count_available = []
    for row in concat_data:
        row_count = []
        for col in row:
            # -99.9 -> data is not available
            count = np.count_nonzero(~np.equal(nan_data, col))
            row_count.append(count)
        count_available.append(row_count)
    return np.array(count_available)
