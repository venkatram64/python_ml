import numpy as np
import matplotlib.pyplot as plt

"""
Box & Whisker Plot
Useful for visualizing the spread & skew of data.
The red line represents the median of the data, and the box represents
the bounds of the 1st and 3rd quartiles.
So, half of the data exists within the box.
The dotted line "whisker" indicate the range of the data - except for outliers, 
which the plotted outside the whisker. Outliers are 1.5X or more the inter quartile range.
This example below creates uniformaly distributed random numbers between -40 and 60, plus
a few outliers above 100 and below -100:
"""

uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100

data = np.concatenate([uniformSkewed, high_outliers, low_outliers])
plt.boxplot(data)
plt.show()