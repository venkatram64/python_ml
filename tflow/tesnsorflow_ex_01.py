import tensorflow as tf


a = tf.Variable(1, name="a")
b = tf.Variable(2, name="b")
f = a + b

init = tf.global_variables_initializer()
with tf.Session() as session:
    init.run()
    print(f.eval())


