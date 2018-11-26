import tensorflow as tf
import google.datalab.ml as ml


x = tf.constant([1000, 2000, 3000], name='x')
y = tf.constant([11, 222, 3333], name='y')

sum_x = tf.reduce_sum(x, name="sum_x")
prod_y = tf.reduce_prod(y, name="prod_y")

final_div = tf.div(sum_x, prod_y, name="final_div")

prod_y = tf.reduce_prod(y, name="prod_y")

final_div = tf.div(sum_x, prod_y, name="final_div")

final_mean = tf.reduce_mean([sum_x, prod_y], name="final_mean")

sess = tf.Session()

print("x: ", sess.run(x))
print("y: ", sess.run(y))

print("sum(x): ", sess.run(sum_x))
print("prod(y): ", sess.run(prod_y))
print("sum(x) / prod(y):", sess.run(final_div))
print("mean(sum(x), prod(y)):", sess.run(final_mean))

