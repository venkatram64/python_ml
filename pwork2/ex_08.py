import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt

#api_key = "********************"

#df = quandl.get('FMAC/HPI_AR', authtoken=api_key)

#df = pd.read_csv('FMAC-HPI_AR.csv', index_col=0)


#print(df.head(100))
#df['NSA Value'].plot()
#plt.show()


states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(states[0][1])

for abbrv in states[0][1][1:]:
    print("FMAC/HPI_" + str(abbrv))
