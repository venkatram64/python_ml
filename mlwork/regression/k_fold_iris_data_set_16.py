"""
Bias and Variance:
Bias is how far removed the mean of your predicted values is from
the "real" answer.
Variance is how scattered your predicted values are from the "real"
answer
Describe the bias and variance of these four cases(assuming the
center is the correct result)

But what you really care about is error.
Bias and variance both contribute to the error.

Error = Bias^2 + Variance

But it's error you want to minimize, not bias or variance specifically.
A complex model will have high variance and low bias
A too-simple model will have low variance and high bias
But both may have the same error the optional complexity is in the middle.

eg:
Tying it to earlier lessons:
Increasing K in K Nearest Neighbours decreases variance and increases
bias(by averaging together more neighbours)
A single decision tree is prone to overfitting high variance
But a random forest decreases that variance.

K Fold Cross Validation:
One way to further protect against overfitting is k-fold cross validation.
Sounds complicated. But it's a simple idea.
split your data into k randomly assigned segments.
Reserve one segment as your test data
Train on each of the remaining k-1 segments and measure their performance against the
test set.
Take the average of the k-1 r-squared scores
prevents you from over fitting to a single train/test split.

Using K-Fold Cross Validation.
Scikit learn makes this really easy.  Even easier than just a single
tain/test split.
In practice, you need to try different variations of your model and
measure the mean accuracy using K-Fold Cross Validation until you find
a sweet spot

Let's Play:
Use K-Fold Cross Validation with a SVC(Single Value compression) model of Iris classification.
We will see that without K-Fold, we could overfit the model.

"""

from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm


def process():
    iris = datasets.load_iris()
    # Split the iris data into train/test data sets with 40% reserved for testing
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

    print("***********Kernal=linear************")
    # Build an SVC model for predicting iris classifications using training data
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)

    # Now measure its performance with the test data
    res = clf.score(X_test, y_test)

    print(res)

    # We give cross_val_score a model, the entire data set and its "real" values, and the number of folds:
    scores = cross_val_score(clf, iris.data, iris.target, cv=5)

    # Print the accuracy for each fold:
    print(scores)
    # And the mean accuracy of all 5 folds:
    print(scores.mean())

    print("**************Kernal=poly************")

    clf = svm.SVC(kernel='poly', C=1).fit(X_train, y_train)
    scores = cross_val_score(clf, iris.data, iris.target, cv=5)
    print(scores)
    print(scores.mean())
    print("*************")

    # Build an SVC model for predicting iris classifications using training data
    clf = svm.SVC(kernel='poly', C=1).fit(X_train, y_train)

    # Now measure its performance with the test data
    res = clf.score(X_test, y_test)
    print(res)


if __name__ == '__main__':
    process()

















