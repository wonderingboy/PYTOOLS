import cv2
import sys
import os
def searchimage(pathname, imagename):
    ori_image=cv2.imread(imagename)
    candidatenames=os.listdir(pathname)
    if not len(candidatenames):
        print('provided path is empty')
        exit()
    for name in candidatenames:
        if not (name.endswith('.jpg') or name.endswith('.png')):
            continue
        if pathname.endswith('/'):
            cur_image=cv2.imread(pathname+name)
        else: 
            cur_image=cv2.imread(pathname+'/'+name)
        if not len(cur_image.shape)==len(ori_image.shape):
            continue
        samesize=True
        for i in range(0,len(cur_image.shape)):
            if cur_image.shape[i]!=ori_image.shape[i]:
                samesize=False
                break
        if samesize==False:
            continue
        com_result=(ori_image==cur_image)
        if com_result.all():
            return name
        else:
            continue
if __name__=='__main__':
    print(searchimage(sys.argv[1],sys.argv[2]))
