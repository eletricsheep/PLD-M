'''
The module is used to obtain the pixel area of the target part of the binary image
'''
import os
import os.path
import re

import cv2
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image

from . import martix, matsave
from .martix import convert, get_binary_martix, get_martix
from .matsave import matsave

def letterbox_image(image, size):
    iw, ih = image.size
    w, h = size
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)

    image = image.resize((nw,nh), Image.BICUBIC)
    new_image = Image.new('RGB', size, (255,255,255))
    new_image.paste(image, ((w-nw)//2, (h-nh)//2))
    return new_image

def get_area(th_path,bw_path):

    th = Image.open(th_path)
    bw = Image.open(bw_path)

    size = th.size
    bw = letterbox_image(bw,size)

    th = th.convert('L')
    bw = bw.convert('L')
    th_np = np.asarray(th)
    bw_np = np.asarray(bw)

    th_np = np.where(th_np>60,1,0)
    bw_np = np.where(bw_np>60,1,0)

    bw_sum = np.sum(bw_np) - 130000
    th_sum = np.sum(th_np) - 130000

    return bw_sum,th_sum

__all__ = ['letterbox_image', 'get_area']

                

