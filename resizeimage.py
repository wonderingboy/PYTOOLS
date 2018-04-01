import sys
import os
import cv2
def resizeimage(imagename,width.height):
    if not (imagename.endswith('.jpg') or imagename.endswith('.png')):
        print ('image name is invalid')
        exit()
    ori_image=cv2.imread(imagename)
    return cv2.resize(ori_image,)
