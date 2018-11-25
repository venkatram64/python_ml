import pandas as pd
from pandas import Series, DataFrame
import numpy as np

srs = Series(np.arange(5), index=["alpha", "beta", "gamma", "delta", "epsilon"])
print(srs)

print(srs[:2])