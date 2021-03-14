# -*- coding: utf-8 -*-
"""test.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eoxErxux3tz9fQ9Z2Cbjkl5k7pHemXa8
"""

import tensorflow as tf
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

tf.executing_eagerly()
x = tf.keras.Input(shape=(30, 30, 3))
layer1 = tf.keras.layers.Conv2D(54, (3, 3), activation='relu', padding='valid')
y = layer1(x)
model = tf.keras.Model(inputs=x, outputs=y)