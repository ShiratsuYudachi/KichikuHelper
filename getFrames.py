import os
import shutil
import cv2
from config import frameFrequency

path = (os.path.abspath(os.path.dirname(__file__)))+'\\'
outPutPath = path+'Frames\\'
videoLibPath = path+'VideoLibs\\'
if not os.path.exists(outPutPath):
        os.mkdir(outPutPath)
if not os.path.exists(videoLibPath):
        os.mkdir(videoLibPath)
def getFrames():
    videoPath = path+'SourceVideos\\'
    times = 1
    for i in os.listdir(videoPath):
        if os.path.isdir(videoPath+i):
            for k in os.listdir(videoPath+i):
                new_name = str(times)+'.mp4'
                os.rename(videoPath+i+"\\"+k,videoPath+i+"\\"+new_name)#avoid non-ascii chracters
                getFramesFrom(videoPath+i+"\\"+new_name,new_name)
                shutil.move(videoPath+i+"\\"+new_name,videoLibPath)
                os.removedirs(videoPath+i)
        else:
            new_name = str(times)+'.mp4'
            os.rename(videoPath+i,videoPath+new_name)
            getFramesFrom(videoPath+new_name,new_name)
            shutil.move(videoPath+new_name,videoLibPath)
        times+=1
    print('End of extact Frames of Video')

def getFramesFrom(videoDir,videoName):
    if not os.path.exists(outPutPath+videoName+"\\"):
        os.mkdir(outPutPath+videoName+"\\")
    times = 0
    video = cv2.VideoCapture(videoDir)
    while True:
        times += 1
        exist, image = video.read()
        if exist:
            if times % frameFrequency == 0:#when times is the integer multiple of frameFrequency
                cv2.imwrite(outPutPath+videoName+'\\'+str(times) + '.jpg', image)#seems like it wont mkdir, with unfound dir it just do nothing even no error
                print(outPutPath+videoName+'\\'+str(times) + '.jpg')
        else:
            break

if __name__ == "__main__":
    getFrames()