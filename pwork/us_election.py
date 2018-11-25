import pandas as pd
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import svm


df = pd.read_csv("house-votes-84.csv")

#print(df.head())

#print(df.describe())

df.replace(['y','n','?'], [0,1,2], inplace=True)

y = df.values[:, 0]

X = df.values[:, 1:]

#print(X.shape)

#print(X)

enc = preprocessing.OneHotEncoder()
X = enc.fit_transform(X)

#print(X)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.5, random_state=42)

param_grid = [
    {'C':[1.0, 10.0, 100.0], 'kernel':['linear']}
]

clf = model_selection.GridSearchCV(
    svm.SVC(),
    param_grid,
    n_jobs=-1
)

clf.fit(X_train, y_train)

test_score = clf.score(X_test, y_test)

print(test_score)

means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']

for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r" %(mean, std * 2, params))
