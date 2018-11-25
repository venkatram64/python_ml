import pandas as pd
import numpy as np
from sklearn import model_selection, linear_model

titanic_data = pd.read_csv('titanic2.csv')

#print(titanic_data)
#print(titanic_data.describe())
#print(titanic_data.info())
#print(titanic_data['name'].sample(25))
#print(titanic_data['home.dest'].sample(25))
#print(titanic_data['body'][pd.notna(titanic_data['body'])].sample(25))
#print(titanic_data[pd.notna(titanic_data['body'])].describe())

#Fixing the data problems

#print(titanic_data.info())

titanic_data.dropna(how='all', inplace=True)
#print(titanic_data.info())
#print(titanic_data['age'].fillna(titanic_data.mean()['age']))

titanic_data['age'] = titanic_data['age'].fillna(titanic_data.mean()['age'])

#print(titanic_data.info())

#print(titanic_data['name'].sample(25))

#print(titanic_data['name'].str.contains(',').value_counts())

#print(titanic_data['name'].str.contains('.').value_counts())

titanic_data['last_name'] = titanic_data['name'].str.split(',', expand=True)[0]
first_names = titanic_data['name'].str.split(',', expand=True)[1]
titanic_data['title'] = first_names.str.split('.', expand=True)[0]
titanic_data['first_names'] = first_names.str.split('.', expand=True)[1]

#print(titanic_data[['name', 'title', 'last_name', 'first_names']].sample(10))

#print(titanic_data['title'].value_counts())

df = titanic_data.drop('home.dest', axis=1)
#print(df.head())

#print(pd.notna(df['body']).value_counts())

df = df[~pd.notna(df['body'])]
#print(pd.notna(df['body']).value_counts())

title_onehot = pd.get_dummies(df['title'])
gender_onehot = pd.get_dummies(df['sex'])

y = np.array(df['survived'])

#print(df.info())

X = np.array(df[['pclass', 'age', 'sibsp', 'parch', 'fare']])

np.hstack([X, title_onehot, gender_onehot]).shape

#print(X.shape)
#print(title_onehot.shape)
#print(gender_onehot.shape)

X = np.hstack([X, title_onehot, gender_onehot])

#print(y.shape)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

#print(X_train.shape)
#print(y_train.shape)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

sc_train = model.score(X_train, y_train)

print(sc_train)

sc_test = model.score(X_test, y_test)

print(sc_test)

