import tensorflow as tf
import google.datalab.ml as ml


a = tf.constant(6.5, name='constant_a')
b = tf.constant(3.4, name='constant_b')
c = tf.constant(3.0, name='constant_c')
d = tf.constant(100.2, name='constant_d')

add = tf.add(a, b, name='add_ab')
substract = tf.subtract(b, c, name="substract_bc")
square = tf.square(d, name="square_d")

final_sum = tf.add_n([add, substract, square], name="final_sum")

with tf.Session() as session:

    print("a + b: ", session.run(add))
    print("b -c: ", session.run(substract))
    print("Suare of d: ", session.run(square))
    print("Final of d :" + str(session.run(final_sum)))

    another_sum = tf.add_n([a, b, c, d, square], name="another_sum")
    print("Another sum ", str(session.run(another_sum)))


    writer = tf.summary.FileWriter("./SimpleMath", session.graph)
    writer.close()

tensorboard_pid = ml.TensorBoard.start("./SimpleMath")


ml.TensorBoard.stop(tensorboard_pid)
