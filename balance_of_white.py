#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import *
from matplotlib import pyplot as plt

def balance():
    img = imread('railroad.png')
    #1
    img_f = img_as_float(img)

    #2
    r = img_f[:, :, 0].sum()
    g = img_f[:, :, 1].sum()
    b = img_f[:, :, 2].sum()

    r /= len(img_f[:, :, 0])
    g /= len(img_f[:, :, 1])
    b /= len(img_f[:, :, 2])

    avg = (r + g + b) / 3

    rw = img_f[:, :, 0] * avg / r
    gw = img_f[:, :, 1] * avg / g
    bw = img_f[:, :, 2] * avg / b


    img_f[:, :, 0] = rw
    img_f[:, :, 1] = gw
    img_f[:, :, 2] = bw

    #4
    out = clip(img_f, 0, 1)

    #save img
    #imsave('out_img2.png', out)

    #show img
    imshow(out)
    plt.show()