#!/usr/bin/env python3



import tensorflow as tf


def create_layer(prev, n, activation):

    W = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    model = tf.layers.Dense(units=n, activation=activation,
                            name="layer", kernel_initializer=W)
    return model(prev)
  
