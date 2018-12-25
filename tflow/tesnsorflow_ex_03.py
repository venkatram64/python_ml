import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import matplotlib.pyplot as plt
import numpy as np

session = tf.InteractiveSession()
mnist = input_data.read_data_sets("NNIST_data", one_hot=True)

images = mnist.train.images[0].reshape([1, 784])
for i in range(1, 500):
    images = np.concatenate((images, mnist.train.images[i].reshape([1, 784])))

plt.imshow(images, cmap=plt.get_cmap('gray_r'))
plt.show()