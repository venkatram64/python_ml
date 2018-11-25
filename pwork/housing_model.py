from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import make_scorer

import matplotlib.pyplot as plt
import seaborn as sns


boston_data = load_boston()

X = boston_data.data
y = boston_data.target

X_df = pd.DataFrame(X, columns=boston_data.feature_names)

print(X_df.head(5))

print(boston_data.DESCR)
print(len(y))

print(np.average(y))

#sns.distplot(y)

gs_params = {
    'fit_intercept': [True, False],
    'normalize': [True, False]
}

mse_scorer = make_scorer(mean_squared_error)

clf = model_selection.GridSearchCV(
    LinearRegression(),
    gs_params,

    scoring=mse_scorer
)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33, random_state=42)

clf.fit(X_train, y_train)

clf.best_params_

#Grid scores

means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']

for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"  % (mean, std * 2, params))


model = LinearRegression(fit_intercept=True, normalize=True)
model.fit(X_train, y_train)
y_pred_ml = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred_ml)

print(mse)