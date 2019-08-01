import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.linear_model import LinearRegression
from scipy import stats
from HypothesisTesting import significance_t_test as sig_t_test
sns.set_style("whitegrid")
sns.set_palette("muted")
sns.set_context('notebook', font_scale=1.25, rc={"lines.linewidth": 2})


df = pd.read_csv('./data/1951-2019.csv')
df['DATE'] = pd.to_datetime(df['DATE'])

# group by year
df1 = df.groupby(df['DATE'].dt.year).mean()

# select baseline 1961-1991
start_year = 1961
end_year = 1991
mask = (df1.index >= start_year) & (df1.index <= end_year)
baseline = df1.loc[mask]
baseline_mean = baseline.mean()
baseline_std = baseline.std()
print(f'baseline mean: \n{baseline_mean}\n')

climate_index = 'TAVG'

# anomaly
anomaly = df1 - baseline_mean

lr = LinearRegression()
model_x = np.array(df1.index).reshape(-1, 1)
model = lr.fit(model_x, df1[climate_index])
predict_x = np.arange(1940, 2040)
predicted_y = model.predict(predict_x.reshape(-1, 1))

model = lr.fit(model_x, anomaly[climate_index])
predict_anomaly_y = model.predict(predict_x.reshape(-1, 1))


fig, axes = plt.subplots(1, 2, figsize=(9, 5))
# actual data plot
sns.lineplot(df1.index, df1[climate_index], alpha=0.75, ax=axes[0])
sns.scatterplot(
    baseline.index, baseline[climate_index], label='Baseline', ax=axes[0])
sns.lineplot(predict_x, predicted_y, label='Linear Trend', ax=axes[0])
axes[0].title.set_text(f'Annual {climate_index}')

# anomaly plot
sns.lineplot(df1.index, anomaly[climate_index], alpha=0.75, ax=axes[1])
sns.lineplot(predict_x, predict_anomaly_y, label='Linear Trend', ax=axes[1])
axes[1].title.set_text(f'Annual {climate_index} Anomaly')
plt.show()

interest_data = df1[df1.index >= 2000]
interest_anomaly = anomaly[anomaly.index >= 2000]

# confidence interval
ci = 0.9
baseline_ci = stats.norm.interval(
    ci, baseline_mean[climate_index],
    baseline_std[climate_index]/len(baseline))
print(f'baseline {ci*100}% CI: {baseline_ci}')

interest_data_ci = stats.norm.interval(
    ci, interest_data.mean()[climate_index],
    interest_data.std()[climate_index]/len(interest_data)
)
print(f'baseline {ci*100}% CI: {interest_data_ci}')

x_ = np.arange(25, 30, 0.001)
baseline_ci_curve = stats.norm.pdf(
    x_, baseline_mean[climate_index], baseline_std[climate_index]/len(baseline))
interest_data_ci_curve = stats.norm.pdf(
    x_, interest_data.mean()[climate_index], interest_data.std()[climate_index]/len(interest_data))


sns.lineplot(x_, baseline_ci_curve, label='baseline confidence interval')
sns.lineplot(x_, interest_data_ci_curve,
             label='interested data confidence interval')
plt.show()

print('Significant Test of interested data and baseline data: ')
sig_res = sig_t_test(baseline[climate_index], interest_data[climate_index])
print(sig_res)
