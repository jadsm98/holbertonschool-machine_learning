#!/usr/bin/env python3
"""module"""


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """function"""
    prediction = tf.math.argmax(y_pred, axis=1)
    equality = tf.math.equal(prediction, y_pred)
    accuracy = tf.math.reduce_mean(tf.cast(equality, tf.float32))
    return accuracy
