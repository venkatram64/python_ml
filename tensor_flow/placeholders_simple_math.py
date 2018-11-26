import tensorflow as tf

x = tf.placeholder(tf.int32, shape=[3], name='x')
y = tf.placeholder(tf.int32, shape=[3], name='y')

sum_x = tf.reduce_sum(x, name="sum_x")
prod_y = tf.reduce_prod(y, name="prod_y")

final_div = tf.div(sum_x, prod_y, name="final_div")

with tf.Session() as session:
    print("Sum(x) : ", session.run(sum_x, feed_dict={x: [100, 200, 300]}))
    print("prod(y): ", session.run(prod_y, feed_dict={y: [11, 22, 33]}))
    print("Sum(x)/prod(y) :", session.run(final_div, feed_dict={x: [100, 200, 300], y: [1, 2, 3]}))


