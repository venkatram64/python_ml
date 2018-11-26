import tensorflow as tf
import google.datalab.ml as ml
"""
Linear Regression:
An analysis on the relationship between 2 variables where one variable is taken
to be independent and the other a dependent.

y = mx + c

The linear regression could be thought as cause and effect, or a lock and key scenario

This could be plotted in a form of graph taking X on the X-axis and Y on the Y-axis

How is this done practically?

We estimate initial values of m & c.
Find the error with these values.
Feedback error values to get better values of M & C

Y = Wx + b
"""
# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b

y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]


# training loop
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(1000):
        sess.run(train, {x: x_train, y: y_train})

    #Evaluate training accuracy
    curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})

    print("W: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss))

