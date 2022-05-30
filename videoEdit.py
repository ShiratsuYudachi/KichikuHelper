import moviepy
from moviepy.editor import *
import time
from config import frameFrequency

path = os.path.dirname(__file__)+'\\'
if not os.path.exists(path+'outputs\\'):
        os.mkdir(path+'outputs\\')
def subclip(src,frameStart,frameEnd,keyword):
    if frameEnd == None:
        frameEnd = 0
    videoPath = path+'VideoLibs\\'+src
    fps = VideoFileClip(videoPath).fps
    timeStart = (frameStart-frameFrequency)/fps
    if timeStart<0:
        timeStart = 0
    timeEnd = (frameEnd+frameFrequency)/fps
    clip = VideoFileClip(videoPath).subclip(timeStart, timeEnd)
    outputPath = path+'outputs\\'+ keyword +'\\'
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
    
    clip.write_videofile(outputPath+str(len(os.listdir(outputPath))+1)+'.mp4')

if __name__ == "__main__":
    subclip(path+'VideoLibs\\1.mp4',10,80,'test')