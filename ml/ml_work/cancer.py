import pandas as pd
from sklearn import preprocessing
import numpy
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from sklearn import tree
#from pydotplus import graph_from_dot_data
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn import neighbors
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression


masses_data = pd.read_csv('mammographic_masses.data.txt')
print(masses_data.head())

names = ['BI-RADS', 'age', 'shape', 'margin', 'density', 'severity']

masses_data = pd.read_csv('mammographic_masses.data.txt', na_values=['?'], names=names)
print(masses_data.head())

#Evaluate whether the data needs cleaning; your model is only as good as the data it's given

print(masses_data.describe())

masses_data.loc[(masses_data['age'].isnull()) |
                  (masses_data['shape'].isnull()) |
                  (masses_data['margin'].isnull()) |
                  (masses_data['density'].isnull())]

masses_data.dropna(inplace=True)
print(masses_data.describe())

all_features = masses_data[['age', 'shape', 'margin', 'density']].values

all_classes = masses_data['severity'].values

feature_names = ['age', 'shape', 'margin', 'density']

print(all_features)

scalar = preprocessing.StandardScaler()
all_features_scaled = scalar.fit_transform(all_features)

print(all_features_scaled)

#Decision Tree

def withDecisionTree():
    numpy.random.seed(1234)
    (training_inputs, testing_inputs, training_classes, testing_classes) = \
                train_test_split(all_features_scaled, all_classes, train_size=0.75, random_state=1)

    clf = DecisionTreeClassifier(random_state=1)
    #train the classifier on the training set
    clf.fit(training_inputs, training_classes)
    score = clf.score(testing_inputs, testing_classes)
    print("Decision Tree: ")
    print(score)

    clf = DecisionTreeClassifier(random_state=1)
    cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
    print(cv_scores.mean())

withDecisionTree()

def withSVM():
    C = 1.0
    print("SVM: <linear> ")
    svc = svm.SVC(kernel='linear', C=C)
    cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
    print(cv_scores.mean())

    print("SVM: <rbf>")
    svc = svm.SVC(kernel='rbf', C=C)
    cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
    print(cv_scores.mean())

    print("SVM: <sigmoid>")
    svc = svm.SVC(kernel='sigmoid', C=C)
    cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
    print(cv_scores.mean())

    print("SVM: <poly>")
    svc = svm.SVC(kernel='poly', C=C)
    cv_scores = cross_val_score(svc, all_features_scaled, all_classes, cv=10)
    print(cv_scores.mean())


withSVM()

def withKNN():
    clf = neighbors.KNeighborsClassifier(n_neighbors=10)
    cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
    print("KNN: ")
    print(cv_scores.mean())

    for n in range(1, 50):
        clf = neighbors.KNeighborsClassifier(n_neighbors=n)
        cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
        print(cv_scores)


withKNN()

def withNaiveBayes():
    scaler = preprocessing.MinMaxScaler()
    all_features_minmax = scaler.fit_transform(all_features)

    clf = MultinomialNB()
    print("NaiveByes: ")
    cv_scores = cross_val_score(clf, all_features_minmax, all_classes, cv=10)
    print(cv_scores.mean())

withNaiveBayes()


def withLogisticRegression():
    clf = LogisticRegression()
    cv_scores = cross_val_score(clf, all_features_scaled, all_classes, cv=10)
    print("LogisticRegression: ")
    print(cv_scores.mean())

withLogisticRegression()
