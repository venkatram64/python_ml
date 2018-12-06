import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')



df = pd.read_csv('AAPL2.csv', parse_dates=['Date'], index_col="Date")
print(df.head())

#print(type(df.Date[0]))

#print(df.index)

mean_monthly_df = df.Close.resample('M').mean()

print(mean_monthly_df)

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))
mean_monthly_df.plot(ax=ax1, label='Monthly')
plt.show()