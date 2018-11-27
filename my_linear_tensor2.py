import tensorflow as tf
import google.datalab.ml as ml

"""
Placeholders:
Placeholders are mechanism in Tensor Flow to define inputs into a graph.
What are Variables?
Variables are parameters of a machine learning model.

AX + B

here A, B are variables
Placeholders and variables have fundamentally different functions.

What are Variables?
Variables are a Tensorflow construct, which are required for the training
process. The Machine Learning algorithm iterates to get closer to the solution,
and hence, the model should have the ability to hold constantly changing values of 
its parameters.

Placeholders: Value is assigned once and does not change afterwards.
Variables: Values are constantly recompute.

Variables are mutable values, but they hold their values across multiple calls to
Session.run().

In a Tensor Flow program to learn linear regression, the parameters we choose are nothing 
but variables.

Linear Regression:
Linear regression is never carried on trending data.
we should use data frames to convert prices into returns
before we perform regression.

Steps:
1. Write a simple python code
2. Define a computation graph
3. Specify the cost function.
4. Instantiate an optimizer
5. Invoke optimizer to carry out training.
6. Obtain a converged model.

Pandas for data frame and numpy are very useful libraries.
Stat model is a statistical took kit used for linear and logistic
regression.
Mat plot library helps in plotting the regression.

Linear regression is called simple regression, when we have 1 dependent variable.
where we have multiple independent variables and single dependent
variable we call it as multple regression.

There are two optimizers:
1. Gradient descent
2. FTRL

The least value of MSE is called the Global Minimum, and , it's 
corresponding values of 'w' and 'b' are taken as best fit
values. These values are used in new predictions. This process is iterative.
Each step is termed as Epoch, and number of steps they take
is called Learning Rate.




"""
# y = Wx + b
W = tf.Variable([2.5, 4.0], tf.float32, name='var_W')

x = tf.placeholder(tf.float32, name='x')
b = tf.Variable([5.0, 10.0], tf.float32, name='var_b')

y = W * x + b

# Initialize all variables defined
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    print("Final result: Wx + b = ", sess.run(y, feed_dict={x: [10, 100]}))


"""init = tf.variables_initializer([W]) # this is not work, b/c variable is not initialized

with tf.Session() as sess:
    sess.run(init)

    print("Final result: Wx + b = ", sess.run(y, feed_dict={x: [10, 100]}))"""

