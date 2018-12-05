import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('auston_hpi.csv', index_col=0)

df.set_index('Date', inplace=True)

df.columns = ['Austin_HPI']

df.to_csv('austin_hpi_2.csv')

df.to_csv('austin_hpi_3.csv', header=False)

print(df.head(100))
df['Austin_HPI'].plot()
plt.show()

