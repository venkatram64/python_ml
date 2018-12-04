
import quandl
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2018, 1, 1)
end = datetime.date.today()

s = "MSFT"
df = quandl.get("WIKI/" + s, start_date=start, end_date=end)

print(df.head())

df['Adj. Close'].plot()
plt.show()

