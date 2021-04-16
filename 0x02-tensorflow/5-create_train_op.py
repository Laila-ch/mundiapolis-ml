
#!/usr/bin/env python3
import tensorflow as tf


def create_train_op(loss, alpha):

    train = tf.train.GradientDescentOptimizer(alpha)
    grads_and_vars = train.compute_gradients(loss)
    return train.apply_gradients(grads_and_vars)
