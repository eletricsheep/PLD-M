'''
The module is used to generate 2D and 3D gradient maps
'''

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import re
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

def matsave(list, image_path, crop_size, defaults_name = "-NaN-", normalize = True):

    image = Image.open(image_path)
    width,height=image.size
    crop_width = int(width/crop_size) + 1
    crop_height = int(height/crop_size) + 1
    data = np.array(list)
    if normalize:
        data = data / max(data)
        data = data.reshape(crop_height,crop_width)
        image_name = re.sub('img/',"",image_path) + defaults_name
        plt.matshow(data)
        plt.savefig('matsave/' + str(crop_size) + image_name +'.jpg')
    else:
        data = data.reshape(crop_height,crop_width)
        
        image_name = re.sub('img/',"",image_path) + defaults_name
        plt.matshow(data)
        plt.savefig('matsave/binary/' + str(crop_size) + '/' +str(crop_size) + image_name +'.jpg')

def save3D(X,Y,Z,angle,num):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.view_init(angle[0],angle[1])
    ax.plot_surface(X,Y,Z,rstride = 1, cstride = 1, cmap = 'rainbow', alpha = 0.5)
    ax.set_zlim(-2, 1.5)
    ax.contour(X, Y, Z, zdir = 'z', offset = -2, cmap = plt.get_cmap('rainbow'))
    #plt.show()
    plt.savefig('matsave/3D-{}.jpg'.format(num))

def mat3dsave(array, angle, num):
    x = np.linspace(0 ,array.shape[1] ,array.shape[1])
    y = np.linspace(0 ,array.shape[0] ,array.shape[0])

    X, Y= np.meshgrid(x,y)
    print(X.shape)
    save3D(X, Y, array, angle, num)