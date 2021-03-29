#!/usr/bin/env python3

def create_placeholders(nx, classes):
  x = tf.placeholder(tf.float32, shape=[,nx])
  y = tf.placeholder(tf.float32, shape=[,classes)
  return x, y


