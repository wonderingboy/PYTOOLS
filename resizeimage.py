import sys
import os
import cv2
def resizeimage(imagename,width,height):
    '''origin image, width, height '''
    if not os.path.exists(imagename):
        print('image does not exist')
        return
    if not (imagename.endswith('.jpg') or imagename.endswith('.png')):
        print ('image name is invalid')
        return
    ori_image=cv2.imread(imagename)
    size=ori_image.shape
    if int(width)<0 or int(height)<0:
        print('invalid width or height' )
        return  
    return cv2.resize(ori_image,(height,width),interpolation=cv2.INTER_CUBIC)
if __name__=='__main__': 
    resized_img=resizeimage(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
    try:
        cv2.imshow('resized_img',resized_img) 
        cv2.waitKey(-1)
    except:
        print('failed to process')
