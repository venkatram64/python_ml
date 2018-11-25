import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Reading the data
data = pd.read_csv('winequality-white.csv', sep=';')

#print(data)

X = data.iloc[:, :-1]

#print(X)

y = data.iloc[:, -1]

#print(y)

# Adding extra Columnt
X = np.append(arr=np.ones((X.shape[0], 1)), values=X, axis=1)

#print(X)

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y)

#Scaling the data

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
#print(X_train)
X_test = scaler.transform(X_test)
#print(X_test)


# Linear regressiong
regressor = LinearRegression()
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)

print(predictions)

rs = r2_score(y_test, predictions)

print(rs)
