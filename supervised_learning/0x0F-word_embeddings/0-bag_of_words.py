#!/usr/bin/env python3
"""module"""


import numpy as np
import sklearn.feature_extraction as sk


def bag_of_words(sentences, vocab=None):
    """function"""

    vector = sk.text.CountVectorizer(vocabulary=vocab)
    emb = vector.fit_transform(sentences)
    embeddings = emb.toarray()
    features = vector.get_feature_names()
    return embeddings, features
