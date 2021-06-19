'''
It is used to calculate the intersection and union ratio between the density partition graph and the actual position
The parameters are truth image path and binary image path
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

from . import cut, martix, matsave
from .cut import cut_image
from .martix import convert, get_binary_martix, get_martix
from .matsave import matsave


def get_iou(th_path,bw_path):

    th = Image.open(th_path)
    bw = Image.open(bw_path)

    th = th.convert('L')
    bw = bw.convert('L')
    th_np = np.asarray(th)
    bw_np = np.asarray(bw)

    th_np = np.where(th_np>60,1,0)
    bw_np = np.where(bw_np>60,1,0)

    com = th_np + bw_np
    xiangjiao = np.where(com>1,1,0)
    xianghuo = np.where(com>0,1,0)

    and_sum = np.sum(xiangjiao) - 100000
    or_sum = np.sum(xianghuo) - 100000

    return (and_sum/or_sum)





