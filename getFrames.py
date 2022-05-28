import os
import cv2
path = (os.path.abspath(os.path.dirname(__file__)))+'\\'
frameFrequency = 20
outPutPath = path+'Frames\\'
if not os.path.exists(outPutPath):
        os.makedirs(outPutPath)
def getFrames():
    videoPath = path+'SourceVideos\\'
    for i in os.listdir(videoPath):
        if os.path.isdir(videoPath+i):
            for k in os.listdir(videoPath+i):
                getFramesFrom(videoPath+i+"\\"+k,k)
        else:
            getFramesFrom(videoPath+i,i)
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