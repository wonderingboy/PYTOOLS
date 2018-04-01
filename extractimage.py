import cv2
import os
import sys
def extractimage(videoname,imagepath):
    if not (os.path.exists(videoname) and os.path.exists(imagepath)):
        print('video does not exist or imagepath does not exist')
        return 
    if not (videoname.endswith('.flv') or videoname.endswith('.avi') or videoname.endswith('.mp4')):
        print('invalid video name')
        return
    video=cv2.VideoCapture(videoname)
    print(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    count=0
    while True:
        _,frame=video.read()
        if frame is None:
            break
        cv2.imwrite(imagepath.rstrip('/')+'/'+str(count)+'.jpg',frame)
        count+=1

if __name__=='__main__':
    extractimage(sys.argv[1],sys.argv[2])
