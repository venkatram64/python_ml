import pandas as pd
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2018, 1, 1)
end = datetime.date.today()
df = pd.read_csv('auston_hpi.csv')

print(df.head(100))

df['Value'].plot()
plt.show()