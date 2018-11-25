import pandas as pd
import numpy as np
from sklearn import model_selection, preprocessing
from sklearn import svm

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

linear_svc = svm.LinearSVC(random_state=42)
linear_svc.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'Linear SVC', linear_svc.score(X_train, y_train), linear_svc.score(X_test, y_test)
))

nu_svc = svm.NuSVC(random_state=42)
nu_svc.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'NuSVC', nu_svc.score(X_train, y_train), nu_svc.score(X_test, y_test)
))

svc = svm.SVC(random_state=42)
svc.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'svc', svc.score(X_train, y_train), svc.score(X_test, y_test)
))

#testing out svc kernels

print('testing out svc kernels')

svc = svm.SVC(kernel='linear', random_state=42)
svc.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'SVC', svc.score(X_train, y_train), svc.score(X_test, y_test)
))

sigmoid = svm.SVC(kernel='sigmoid', random_state=42)
sigmoid.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'sigmoid', sigmoid.score(X_train, y_train), sigmoid.score(X_test, y_test)
))

"""poly = svm.SVC(kernel='poly', random_state=42)

poly.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'poly', poly.score(X_train, y_train), poly.score(X_test, y_test)
))

print("Playing with the slack varible C")

svc_linear = svm.SVC(kernel='linear', C=50.0, random_state=42)

svc_linear.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'svc_linear', svc_linear.score(X_train, y_train), svc_linear.score(X_test, y_test)
))"""

print("Playing with Balance out classes")

svc_linear_balance = svm.SVC(kernel='linear', class_weight='balanced', random_state=42)

svc_linear_balance.fit(X_train, y_train)
print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'svc_linear_balance', svc_linear_balance.score(X_train, y_train), svc_linear_balance.score(X_test, y_test)
))

print("Playing with preprocessing")
scalar = preprocessing.StandardScaler().fit(X_train)
X_train_scaled = scalar.transform(X_train)

print(X_train[0])

svc = svm.SVC(kernel='linear', random_state=42)
svc.fit(X_train_scaled, y_train)
X_test_scaled = scalar.transform(X_test)

print('{}: Training error = {:.4f}, test error = {:.4f}'.format(
    'svc', svc.score(X_train_scaled, y_train), svc.score(X_test_scaled, y_test)
))


