import tensorflow as tf
import google.datalab.ml as ml
"""
Tensors:

1. Building a graph
2. Running a graph

Tensor could be defined as a central unit of data in tensor flow.

A Tensor consists of a set of primitive values shaped into an array of any
number of dimensions. 

Ho do we represent data in tensors?

If data is Scalar no bracket will be used.

If it is a one dimensional vector one square bracket is used on each end.(ex: [11,2,3])

Case of 2-D vector (matrix), use two square brackets. (eg: [[1,2,3][1,11,123]]

N-D vector would have N- brackets.

Important characteristics of Tensor.

Rank: The number of dimensions in a tensor, define it's Rank.

Shape: The number of elements in each dimension defines the Shape.

Data Type: The Data Type of tensor, depends on data type of tis elements.
"""

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
