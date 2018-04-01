import os
import sys
def splitfile(a,b,c,percentage):
    if not os.path.exists(a):
        print('file does not exists')       
        return 
    percentage=int(percentage)
    afile=open(a)
    alines=afile.readlines()
    try:
        b_file=open(b,'w')
        c_file=open(c,'w')
    except:
        print('fail to open file to write')
    for i,line in enumerate(alines):
        if i< len(alines)*percentage/100:
            b_file.write(line)
        else:
            c_file.write(line)
    afile.close()
    b_file.close()
    c_file.close()

if __name__=='__main__':
    splitfile(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
