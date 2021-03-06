#!/usr/bin/env python3
"""module"""


import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """function"""
    weights = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    l2_reg = tf.contrib.layers.l2_regularizer(lambtha)
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=weights,
                            kernel_regularizer=l2_reg)
    return layer(prev)
