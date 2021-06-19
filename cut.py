'''
The module is used to cut the image to different sizes
'''

from PIL import Image
import sys

def cut_image(image,crop_size):
    width,height=image.size
    crop_width = int(width/crop_size) + 1
    crop_height = int(height/crop_size) + 1
    item_width=int(crop_size)
    box_list=[]
    count=0
    for j in range(0,crop_height):
        for i in range(0,crop_width):
            count+=1
            box=(i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width)
            box_list.append(box)
    print('total crop counts are {} iamges'.format(count))
    image_list=[image.crop(box) for box in box_list]
    return image_list

def save_images(image_list):
    index=1
    for image in image_list:
        image.save('split/cutimage'+str(index)+'.jpg')
        index+=1

__all__ = ['cut_image', 'save_images']



