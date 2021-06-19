'''
The module is used to obtain the matrix of different sampling size 
and the matrix of different threshold level under the sampling size
'''
import re

import numpy as np
from PIL import Image

from . import cut
from .cut import cut_image


def get_martix(image_path,crop_size, array = False):
    image = Image.open(image_path)
    image = image.convert('L')
    image_list = cut_image(image,crop_size)

    image_martix = []
    for i in range(0,len(image_list)):
        x = np.array(image_list[i])
        rate = (np.sum(x>30))/(crop_size*crop_size)
        image_martix.append(rate)
    if array:
        width,height=image.size
        crop_width = int(width/crop_size) + 1
        crop_height = int(height/crop_size) + 1
        image_martix = np.asarray(image_martix)
        image_martix = image_martix.reshape(crop_height,crop_width)
        return image_martix  
    else:
        return image_martix

def get_binary_martix(image_path,crop_size,mid = 3, array = False):
    image = Image.open(image_path)
    image = image.convert('L')
    image_list = cut_image(image,crop_size)

    image_martix = []
    for i in range(0,len(image_list)):
        x = np.array(image_list[i])
        rate = (np.sum(x>30))/(crop_size*crop_size)
        image_martix.append(rate)
    max_rate = max(image_martix)
    min_rate = min(image_martix)
    mid_rate = (max_rate + min_rate)/mid
    print(max_rate,mid_rate,min_rate)
    image_binary_martix = []
    for j in image_martix:
        if j < mid_rate:
            ppi = 0
        else:
            ppi = 1
        image_binary_martix.append(ppi)
    if array:
        width,height=image.size
        crop_width = int(width/crop_size) + 1
        crop_height = int(height/crop_size) + 1
        image_binary_martix = np.asarray(image_binary_martix)
        image_binary_martix = image_binary_martix.reshape(crop_height,crop_width)
        return image_binary_martix   
    else:
        return image_binary_martix
    

def convert(image_path):
    image = Image.open(image_path)
    image = image.convert('L')
    img = np.asarray(image)
    img = np.int64(img>70)
    return img

