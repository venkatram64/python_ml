
from pandas_datareader import data
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2018, 1, 1)
end = datetime.date.today()

s = "MSFT"
df = data.DataReader(s, "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()
plt.show()

