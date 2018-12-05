import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt

api_key = "******"

#df = quandl.get('FMAC/HPI_AR', authtoken=api_key)

states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(states[0][1])

for abbrv in states[0][1][1:]:
    print("FMAC/HPI_" + str(abbrv))


df1 = pd.DataFrame({'Year': [2001, 2002, 2003, 2004],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]})


df3 = pd.DataFrame({'Year': [2001, 2003, 2004, 2005],
                    'Unemployment': [7, 8, 9, 4],
                    'Low_tier_HPI': [50, 52, 50, 53]})

#merged = pd.merge(df1, df3, on='Year')
#merged.set_index('Year', inplace=True)
#print(merged)

#merged = pd.merge(df1, df3, on='Year', how='left')
#merged.set_index('Year', inplace=True)
#print(merged)

merged = pd.merge(df1, df3, on='Year', how='right')
merged.set_index('Year', inplace=True)
print(merged)