#!/usr/bin/env python3
"""module"""


import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """function"""
    m, h, w, c = images.shape
    kh, kw = kernels.shape[0], kernels.shape[1]
    nc = kernels.shape[3]
    sh, sw = stride
    if padding == 'valid':
        out_h = (h - kh + 1) // sh
        out_w = (w - kw + 1) // sw
    elif padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
        out_h = (h + 2*ph - kh + 1) // sh
        out_w = (w + 2*pw - kw + 1) // sw
        im_padded = np.pad(images, [(0, 0), (ph, ph), (pw, pw), (0, 0)])
    else:
        ph, pw = padding
        out_h = (h + 2*ph - kh + 1) // sh
        out_w = (w + 2*pw - kw + 1) // sw
        im_padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                           'constant', constant_values=(0, 0))
    output = np.zeros((m, out_h, out_w, nc))
    for k in range(nc):
        for i in range(out_h):
            for j in range(out_w):
                if padding == 'valid':
                    im_slice = images[:, i*sh: i*sh + kh,
                                      j*sw: j*sw + kw, :]
                else:
                    im_slice = im_padded[:, i * sh: i * sh + kh,
                                         j * sw: j * sw + kw, :]
                output[:, i, j, k] = np.sum(im_slice * kernels[:, :, :, k],
                                            axis=(1, 2, 3))
    return output
