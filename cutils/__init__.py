''' Cv2 utility functions '''
import random

import cv2


def coor_offset(coor, offset, size):
    ''' Finds the offset of a coordinate '''
    h, w = size
    y = min(coor[1] + offset[1], h-1)
    x = min(coor[0] + offset[0], w-1)
    return (y, x)


def get_color_diff(color1, color2):
    ''' Finds the difference between 2 colors '''
    diff = [abs(int(color1[i])-int(color2[i])) for i in range(len(color1))]
    return sum(diff)


def humanize(coor, max_offset=5):
    ''' Humaizes a coordinate '''
    x, y = coor
    x = x + random.randint(-max_offset, max_offset)
    y = y + random.randint(-max_offset, max_offset)
    return (x, y)


def crop(img, rect):
    ''' Crops an cv2 image using coordinate and size '''
    return img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]


def find_center(rect):
    ''' Finds the center of the boundingRect value '''
    return (rect[1] + rect[3]//2, rect[0] + rect[2]//2)


def imshow(img):
    ''' Dispalys an image and waits for a key press '''
    cv2.imshow('', img)
    cv2.waitKey()
