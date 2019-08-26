import numpy as np


class MannKendallTest:
    def __init__(self, data_arr):
        """
            data_arr: 1d numpy array of data
        """
        self.data = data_arr
        self.mk_s = 0
        self.mk_var = 0
        self.mk_z = 0
        self.cal_mk_s()
        self.cal_mk_var()
        self.cal_mk_z()

    def sign(self, x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1

    def cal_mk_s(self):
        mk_sum = 0
        for i in range(len(self.data)):
            for j in range(0, i):
                # x_i (occur after x_j)
                # for all  x_j that occur before x_i
                # x_i - x_j
                mk_sum += self.sign(self.data[i] - self.data[j])
        self.mk_s = mk_sum

    def cal_mk_var(self):
        # group/ties data and count frequency
        unique, counts = np.unique(self.data, return_counts=True)
        group = dict(zip(unique, counts))
        n = len(self.data)

        group_sum = 0
        for key, val in group.items():
            group_sum += val*(val-1)*(2*val+5)

        variance = (1/18)*(n*(n-1)*(2*n+5) - group_sum)
        self.mk_var = variance

    def cal_mk_z(self):
        if self.mk_s > 0:
            self.mk_z = (self.mk_s-1)/np.sqrt(self.mk_var)
        elif self.mk_s == 0:
            self.mk_z = 0
        else:
            self.mk_z = (self.mk_s+1)/np.sqrt(self.mk_var)


if __name__ == "__main__":
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    df = pd.read_csv('./data/1951-2019.csv')
    df['DATE'] = pd.to_datetime(df['DATE'])
    df = df.groupby(df['DATE'].dt.year).mean()

    round_digit = 2
    index = 'TAVG'
    temperature = np.round(np.array(df[index]), round_digit)
    year = np.array(df.index)
    lr = LinearRegression()
    lr = lr.fit(year.reshape(-1, 1), temperature)
    print(f'linear regression: coef={lr.coef_}, intercept={lr.intercept_}')

    mkt = MannKendallTest(temperature)
    print(f':: Mann-Kendall Test ::')
    print(f'S = {round(mkt.mk_s, 3)}')
    print(f'variance = {round(mkt.mk_var, 3)}')
    print(f'z = {round(mkt.mk_z, 3)}')
