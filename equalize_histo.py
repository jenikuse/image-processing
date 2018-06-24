#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage.io import imread, imshow, imsave
from skimage import data
import numpy as np
import cv2
from matplotlib import pyplot as plt

def equalize():
    img = cv2.imread('landscape.png',0)

    hist,bins = np.histogram(img.flatten(),256,[0,256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()


    #plot histogramm and cdf func
    '''
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()
    '''
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    img2 = cdf[img]

    #save processed image
    imsave('out_img.png', img2)

