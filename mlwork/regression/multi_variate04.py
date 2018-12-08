import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

"""
Multivariate regresion(Multiple Regression)
What if more than one variable influences the one you are interested in?
Eg: predicting a price for a car based on its many attributes
(body style, brand, mileage, etc.)
Still uses least squres
We just end up with coefficients for each factor.
for eg: price = alpha + beta1(mileage) + beta2(age) + beta3(doors)
These coefficients imply how important each factor 
is(if the data is all normalized)
Get rid of ones that do not matter
Can still measure fit with r-squared
Need to assume the different factors are not
themselves dependent on each other
"""

df = pd.read_excel('cars.xls')
print(df.head())
scale = StandardScaler()
X = df[['Mileage', "Cylinder", 'Doors']]
y = df['Price']

X[['Mileage', "Cylinder", 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].as_matrix())
print(X)

est = sm.OLS(y, X).fit()
print("*********** Summary **********")
print(est.summary())

print("*********Mean for doors ************")
print(y.groupby(df.Doors).mean())
