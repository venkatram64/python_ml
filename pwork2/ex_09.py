import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt

api_key = "*****d"

#df = quandl.get('FMAC/HPI_AR', authtoken=api_key)

states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(states[0][1])

for abbrv in states[0][1][1:]:
    print("FMAC/HPI_" + str(abbrv))


df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index={2001, 2002, 2003, 2004})

df2 = pd.DataFrame({'HPI':[80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index={2005, 2006, 2007, 2008})

df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Unemployment': [7, 8, 9, 4],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index={2001, 2002, 2003, 2004})

#concat = pd.concat([df1, df2, df3])
#print(concat)

#print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))

df1.set_index('HPI', inplace=True)

df3.set_index('HPI', inplace=True)

print(df1.join(df3))


