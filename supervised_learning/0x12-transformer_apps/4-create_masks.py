#!/usr/bin/env python3
"""module"""

import tensorflow.compat.v2 as tf


def create_masks(inputs, target):
    """function"""
    encoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    encoder_mask = encoder_mask[:, tf.newaxis, tf.newaxis, :]
    decoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    decoder_mask = decoder_mask[:, tf.newaxis, tf.newaxis, :]
    batch_size, seq_len_out = target.shape
    look_ahead_mask = tf.linalg.band_part(tf.ones(
        (seq_len_out, seq_len_out)), -1, 0)
    look_ahead_mask = 1 - look_ahead_mask
    padding_mask = tf.cast(tf.math.equal(target, 0), tf.float32)
    padding_mask = padding_mask[:, tf.newaxis, tf.newaxis, :]
    combined_mask = tf.maximum(look_ahead_mask, padding_mask)
    return encoder_mask, combined_mask, decoder_mask
