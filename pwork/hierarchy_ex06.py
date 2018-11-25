import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Directly with MultiIndex
midx = pd.MultiIndex([['a', 'b'], ['alpha', 'beta'], [1, 2]],
                     [[0, 0, 0, 0, 1, 1, 1, 1],
                      [0, 0, 1, 1, 0, 0, 1, 1],
                      [0, 1, 0, 1, 0, 1, 0, 1]])
srs2 = Series(np.arange(8), index=midx)

print(srs2)


# In the Series creation
srs = Series(np.arange(8),
             index=[['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                    ['alpha', 'alpha', 'beta', 'beta',
                     'alpha', 'alpha', 'beta', 'beta'],
                    [1, 2, 1, 2, 1, 2, 1, 2]])
print(srs)

print(srs.loc['b'])

print(srs.loc['b', 'alpha'])

print(srs.loc['b', 'alpha', 1])

print(srs.loc['a', :, 1])

#Now we look at managing a hierarchical index attached to a DataFrame.
df = DataFrame(np.random.randn(8, 3), index=midx,
               columns=['AAA', 'BBB', 'CCC'])
df.loc['b']

ret = df.loc[('b', 'alpha')]    # Must use a tuple here

print(ret)

ret = df.loc[('b', 'alpha', 1)]

print(ret)

ret = df.loc[('b', slice(None), 1), :]    # Don't treat : as optional

print(ret)

ret = df.loc[(slice(None, 'b'), slice(None), 1), ['AAA', 'BBB']]    # :'b'

print(ret)

ret = df.loc[(slice(None), slice(None), 1), 'CCC']

print(ret)