import os
import sys
def addfile(a,b,c):
    '''add two files line by line'''
    afile=open(a)
    bfile=open(b)
    if not (os.path.exists(a) and os.path.exists(b)):
        print(a +' or '+b+' did not exists')
        return 
    try:
        c_file=open(c,'w')
    except:
        print('can not open '+ c +' to write')
    alines=afile.readlines()
    blines=bfile.readlines()
    for aline,bline in zip(alines,blines):
        c_file.write(aline.strip('\n')+' '+bline)
    afile.close()
    bfile.close()
    c_file.close()  
if __name__=='__main__':
    addfile(sys.argv[1],sys.argv[2],sys.argv[3])
        
