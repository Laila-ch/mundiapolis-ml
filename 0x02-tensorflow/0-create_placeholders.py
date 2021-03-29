#!/usr/bin/env python3

def create_placeholders(nx, classes):
  x = tf.placeholder(tf.float32)
  y = tf.placeholder(tf.float32)
  return x, y
