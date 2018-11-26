# updating the variable with in a session

number = tf.Variable(10)
multiplier = tf.Variable(1)

init = tf.global_variables_initializer()

result = number.assign(tf.multiply(number, multiplier))


with tf.Session() as sess:
    sess.run(init)

    for i in range(5):
        print("Result number * multiplier = ", sess.run(result))
        print("Increment multiplier, new value = ", sess.run(multiplier.assign_add(1)))




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

