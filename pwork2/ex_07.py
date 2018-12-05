import pandas as pd
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('austin_hpi_3.csv', names=['Date', 'Austin_HPI'], index_col=0)


print(df.head(100))
df['Austin_HPI'].plot()
plt.show()

