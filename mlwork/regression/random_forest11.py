import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def processData():
    input_file = "PastHires.csv"
    df = pd.read_csv(input_file, header=0)
    print(df.head())
    d = {'Y': 1, 'N': 0}
    df['Hired'] = df['Hired'].map(d)
    df['Employed?'] = df['Employed?'].map(d)
    df['Top-tier school'] = df['Top-tier school'].map(d)
    df['Interned'] = df['Interned'].map(d)
    d = {'BS': 0, 'MS': 1, 'PhD': 2}
    df['Level of Education'] = df['Level of Education'].map(d)

    print(df.head())

    features = list(df.columns[:6])
    print(features)

    y = df['Hired']
    X = df[features]
    clf = RandomForestClassifier(n_estimators=10)
    clf = clf.fit(X, y)

    # Predict employment of an employed 10-year veteran
    print(clf.predict([[10, 1, 4, 0, 0, 0]]))
    # ...and an unemployed 10-year veteran
    print(clf.predict([[10, 0, 4, 0, 0, 0]]))



if __name__ == '__main__':
    processData()
