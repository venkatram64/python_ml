import tensorflow as tf
import google.datalab.ml as ml

"""
Image processing in Tensor Flow:

what kind of Neural Network would we pick for this task?

Convolutional Neural Network

Represent images in the form of tensors, this leads to 
Image recognition.  Then we need to apply transform
function
This step is known as image processing.

Pixels of the input image are the feature vector.
The pixels of any image are tiny rectangular blocks that contain sub
features like edges, color and shape.

Image recognition using volume or a corpus of data.

It classifies or basically identifies any image that is fed as
input to it.

The input in step 1 is called Training data.
The input in step 2 is called Testing data.


"""
original_image_list = ["./images/dog.jpg","./images/cat.jpg"]

# Make a queue of file names including all the images specified.
filename_queue = tf.train.string_input_producer(original_image_list)

# Read an entire image file.
image_reader = tf.WholeFileReader()

with tf.Session() as sess:
    # Coordinate the loading of image files.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    image_list = []
    for i in range(len(original_image_list)):
        # Read a whole file from the queue, the first returned value in the tuple is the
        # filename which we are ignoring.
        _, image_file = image_reader.read(filename_queue)

        # Decode the image as a JPEG file, this will turn it into a Tensor which we can
        # then use in training.
        image = tf.image.decode_jpeg(image_file)

        # Get a tensor of resized images.
        image = tf.image.resize_images(image, [224, 224])
        image.set_shape((224, 224, 3))

        # Get an image tensor and print its value.
        image_array = sess.run(image)
        print(image_array.shape)

        # The expand_dims adds a new dimension
        image_list.append(tf.expand_dims(image_array, 0))

    # Finish off the filename queue coordinator.
    coord.request_stop()
    coord.join(threads)
    index = 0

    # Write image summary
    summary_writer = tf.summary.FileWriter('./ImageReadAndResizeWithCoordinator', graph=sess.graph)

    for image_tensor in image_list:
        summary_str = sess.run(tf.summary.image("image-" + str(index), image_tensor))
        summary_writer.add_summary(summary_str)
        index += 1

    summary_writer.close()

tensorboard_pid = ml.TensorBoard.start('./ImageReadAndResizeWithCoordinator')
ml.TensorBoard.stop(tensorboard_pid)