#!/usr/bin/env python3
"""module"""


import numpy as np


def uni_bleu(references, sentence):
    """calculates the unigram BLEU score for a sentence"""
    len_sen = len(sentence)
    min = max(len_sen, max(len(i) for i in references))
    sum_count_clip = 0
    added = []
    for word in sentence:
        count_clip = 0
        for ref in references:
            if ref.count(word) > count_clip:
                count_clip = ref.count(word)
            if abs(len(ref) - len_sen) < min:
                min = abs(len(ref) - len_sen)
                closest_len = len(ref)
        if word not in added:
            sum_count_clip += count_clip
        added.append(word)
    bp = np.exp(1 - closest_len / len_sen)
    if len_sen > closest_len:
        bp = 1
    return bp * sum_count_clip / len_sen
