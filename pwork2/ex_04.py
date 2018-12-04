import pandas as pd
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2018, 1, 1)
end = datetime.date.today()

#df = pd.read_csv('https://www.quandl.com/api/v3/datasets/ZILLOW/Z77060_ZRISFRR.csv?api_key=**********&start_date='+ str(start)+'&end_date=' + str(end))
df = pd.read_csv('https://www.quandl.com/api/v3/datasets/ZILLOW/Z77060_ZRISFRR.csv?api_key=**********')


print(df.head(100))

df.to_csv('auston_hpi.csv')

df = pd.read_csv("auston_hpi.csv")

df['Value'].plot()
plt.show()