
#!/usr/bin/env python3


import tensorflow as tf


def calculate_accuracy(y, y_pred):
  
    y_m = tf.argmax(y, axis=1)
    yp_m = tf.argmax(y_pred, axis=1)
    return tf.reduce_mean(tf.cast(tf.equal(y_m, yp_m), 'float32'))
