import cv2
import os
from config import cropOnly
from config import thresh
import shutil

path = os.path.abspath(os.path.dirname(__file__))+'\\'
savePath = path+'SubtitleImages\\'
if not os.path.exists(savePath):
    os.mkdir(savePath)

def getSubtitleImage(filePath,dirName=''):
    img = cv2.imread(filePath)
    print(img.shape)
    edited = img[900:1080, 0:1920]  # 裁剪坐标为[y0:y1, x0:x1],以左上角为原点，在(0,900)和(1920,1080)两点间裁出
    if not cropOnly:
        imgray = cv2.cvtColor(edited, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(imgray, thresh, 255, cv2.THRESH_BINARY)  # 输入灰度图，输出二值图
        edited = cv2.bitwise_not(binary)  # 取反
    if not os.path.exists(path+'SubtitleImages\\'+dirName):
        os.mkdir(path+'SubtitleImages\\'+dirName)
    cv2.imwrite(path+'SubtitleImages\\'+dirName+'\\'+filePath.split('\\')[-1], edited)

def generateAllSubtitleImage():
    pass
    for i in os.listdir(path+"Frames\\"):
        print(os.listdir(path+"Frames\\"))
        if os.path.isdir(path+'Frames\\'+i):
            for k in os.listdir(path+'Frames\\'+i):
                getSubtitleImage(path+'Frames\\'+i+'\\'+k,i)
                print('processed '+path+'Frames\\'+i+'\\'+k)
        else:
            getSubtitleImage(path+'Frames\\'+i)
            print('processed '+ path+'Frames\\'+i)
        shutil.rmtree(path+"Frames\\"+i)

if __name__ == '__main__':
    generateAllSubtitleImage()