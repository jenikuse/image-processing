#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage.io import imread, imshow, imsave
import numpy as np

def image_histogram_equalization(image, number_bins=256):
    # from http://www.janeriksolem.net/2009/06/histogram-equalization-with-python-and.html

    # get image histogram
    image_histogram, bins = np.histogram(image.flatten(), number_bins, normed=True)
    cdf = image_histogram.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize

    # use linear interpolation of cdf to find new pixel values
    image_equalized = np.interp(image.flatten(), bins[:-1], cdf)

    return image_equalized.reshape(image.shape), cdf

#if __name__ == '__main__':
def equa():
    # generate some test data with shape 1000, 1, 96, 96
    data = np.random.rand(1000, 1, 96, 96)
    #data = imread('landscape.png')

    # loop over them
    data_equalized = np.zeros(data.shape)
    for i in range(data.shape[0]):
        image = data[i, 0, :, :]
        data_equalized[i, 0, :, :] = image_histogram_equalization(image)[0]

    print (data_equalized)
    #imsave('out_img.png', data_equalized)



def min_not_null(list):
    list_min = min(list)
    for i in range(len(list)):
        if (list[i] > list_min) & (list[i] != 0):
            return list[i]

def equalize():
    img = imread('landscape.png')

    h, w = img.shape[0], img.shape[1]
    total_pix = h * w

    hist, bin_edges = np.histogram(img, bins=range(257))
    print hist[145]

    cdf = np.cumsum(hist)
    cdf_min = min_not_null(cdf)
    print hist

    f = []
    #for x in range(len(cdf)):
    
    #    el = np.round(255 * (cdf[x] - cdf_min) / (total_pix -1))
        #f.append(el)

    cdf = cdf.tolist()
    j = 0

    for pixh in range(h):
        for pixw in range(w):

            x = img[pixh, pixw] #значение pix
            #print x
            #ind = cdf.index(x) #index этого эл-та
            #print ind
            #elem = (np.round(255 * (cdf[ind] - cdf_min) / (total_pix - 1)))
            #img[pixh,pixw] = elem

            j += 1
            #print j

    imsave('out_img.png', img)