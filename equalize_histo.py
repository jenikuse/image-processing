#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage.io import imread, imshow, imsave
import cv2
import numpy as np
from matplotlib import pyplot as plt

def equalize():

    img = cv2.imread('landscape.png', 0)

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()

    #plot histogram
    '''
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()
    '''

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[img]

    #save img
    #imsave('out_img.png', img2)

    #show image
    imshow(img2)
    plt.show()