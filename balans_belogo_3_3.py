#!/usr/bin/env python
# -*- coding: utf-8 -*-

from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import *
'''
Прочитайте изображение из файла img.png. 

Примените к нему выравнивание гистограммы по алгоритму, 
описанному в слайдах и видео. 

Работать достаточно в целых числах, помещающихся в байт 
(т.е. изображение конвертировать не нужно). 

Результат сохраните в файл out_img.png.
'''
def balans():
    img = imread('railroad.png')
    #1
    img_f = img_as_float(img)

    #2
    r = img_f[:, :, 0].sum()
    g = img_f[:, :, 1].sum()
    b = img_f[:, :, 2].sum()

    r /= len(img_f[:, :, 0])
    #b /= len(b)
    print (r)

    #Avg = ( ~R + ~G + ~B ) / 3
    avg = (r + g + b) / 3
    # avg = (img_f[:, :, 0] + img_f[:, :, 1] + img_f[:, :, 2]) / 3

    #rw = ~R / Avg
    rw = img_f[:, :, 0] / avg
    gw = img_f[:, :, 1] / avg
    bw = img_f[:, :, 2] / avg

    #3 R = R/rw
    img_f[:, :, 0] /= rw
    img_f[:, :, 1] /= gw
    img_f[:, :, 2] /= bw

    #4
    out = clip(img_f, 0, 1)
    #out = img_as_ubyte(img_f)

    imsave('out_img2.png', out)