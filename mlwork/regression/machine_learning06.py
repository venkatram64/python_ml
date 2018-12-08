

"""
Algorithms that can learn form observational data,
and can make predictions based ont.

There are two types:
1. Supervised Learning:
In supervised learning, the data the algorithm "learns"
from comes with the "correct" answers
The model created is then used to predict the answers for new
unknown values.
Example: You can train a model for predicting car prices
based on car attributes using historical sales data. That model can then
predict the optimal price for new cars that have not been sold before.

Evaluating Supervised Learning:
If you have a set of training data that includes the value you are trying to
predict - you do not have to guess if the resulting model is good or not.
If you have enough training data, you can split it into two parts: a training
set and a test set.
You then train the model using only the training set
And then measure(using r-squared or some other metric) the model's accuracy by
asking it to predict values for the test set, and compare that to the
known, true values.

Train/Test in practice
Need to ensure bothe sets are large enough to contain representatives
of all the variations and outliers in the data you care about

The data sets must be slected randomly
Train/Test is a great way to guard against overfitting

Train/Test is not Infallible
Maybe your sample sizes are too small
Or due to random chance your train and test sets look remarkably similar
Overfitting can still happen

K-fold Cross Validation:
One way to further protect against overfitting is k-fold cross validation
Sounds complicated. But it is a simple idea:
Split your data into K randomly assigned segments
Reserve one segment as your test data
Train on each of the remaining K-1 segments and measure their performance against the test set
Take the average of the K-1, r-squared scores

2. Unsupervised Learning:
The model is not given any 'answers' to learn from, it must make
sense of the data just given the observations themselves.
eg: group(cluster) some objects together into 2 different sets.
but I do not tell you what the "right" set is for any obect ahead of time
"""