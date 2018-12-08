from numpy import random
import matplotlib.pyplot as plt

"""
Linear Regression: 
Fit a line to a data set of observations.
Use this line to predict unobserved values.
I do not know why they call it "regression."
it is really misleading. you can use it ot 
predict points in the future, the past whatever.
In fact time usually has nothing to do with it.
"""

"""
Linear Regression: How does it work?
Usually using "least squares"
Minimizes the squared error between each point and the line
Remember the slope intercept equation of a line? y = mx + b
The slope is the correlation between the two varaibles times the 
standard deviation in Y, all divided by the standard deviation in X.
Neat how standard deviation how some real mathematical meaning, eh?
The intercept is the mean of Y minus the slope times the mean of X
But Python will do all that for you.

Least squares minimizes the sum of squared errors.
This is the same as maximizing the likelihood of the observed data if you
start thinking of the problem in terms of probabilities and probability
distribution functions.
This is sometimes called "maximum likelihood estimation"

Gradient Descent is an alternate method to least squares.
Basically iterates to find the line that best follows the contours defined by the data
Easy to try in Python and just compare the results to least squares.
But usually least squares is perfectly good choice.

Measuring error with r-squared:
How do we measure how well our line fits our data?
R-squared(aka coefficient of determination)measures:
The fraction of the total variation in Y that is
captured by the model.

R-squred = 1.0 - (sum of squared errors)/(some of squared variation from mean)

Interpreting r-squared
Ranges from 0 to 1
- 0 is bad(none of the variance is captured)
- 1 is good(all of the variance is captured)
"""


