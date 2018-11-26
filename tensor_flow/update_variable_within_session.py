import tensorflow as tf


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



