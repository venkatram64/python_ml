from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


iris_data = load_iris()

#print(iris_data.DESCR)

all_iris = pd.DataFrame(iris_data.data)
all_iris.columns = iris_data.feature_names
all_iris['target'] = iris_data.target

print(all_iris)

X = iris_data.data
y = iris_data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train.shape)

print(X_test.shape)

model = LogisticRegression()
model.fit(X_train, y_train)
mp = model.predict([[4.0, 5.0, 2.0, 1.0]])

print(mp)

mp = model.predict([[6.2, 2.8, 4.8, 1.8]])

print(mp)

sc = model.score(X_train, y_train)

print(sc)

sc = model.score(X_test, y_test)

print(sc)