from copyreg import pickle
from multiprocessing.dummy import Process
from utilities import sortList
import easyocr
import os
import multiprocessing as mp
import time
from config import ProcessNumber

path = path = os.path.dirname(__file__)+'\\'
subtitleImagePath = path+'SubtitleImages\\'
#曾经我有一个对象
'''
class Subtitle(object):
    def __init__(self,text,video,frameStart,frameEnd):
        self.text = text
        self.video = video
        self.frameStart = frameStart
        self.frameEnd = frameEnd
    
    def getText(self):
        return self.text

    def getSourceVideo(self):
        return self.video
    
    def getframe(self):
        pass

def create_subtitle_object(list):
    subtitles = []
    for i in list:
        subtitles.append(Subtitle(i[0],i[1],i[2],i[3]))
    return subtitles

'''
def save(list):
    pass
    
def mergeSubtitle(list):
    pass
    i = 0
    while i<len(list)-1:
        if list[i][0] == list[i+1][0]:
            list[i][3] = list[i+1][2]
            del list[i+1]
        else:
            i+=1
    return list
            

def read(imagePath):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    rawText = '，'.join(result)
    text = [rawText,imagePath.split("\\")[-2],int(imagePath.split("\\")[-1].strip('.jpg')),None]#format:[text, video, frame]
    print("extracted "+str(text))
    return text

def readMP(imagePath):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    rawText = '，'.join(result)
    text = [rawText,imagePath.split("\\")[-2],int(imagePath.split("\\")[-1].strip('.jpg')),None]
    print("extracted "+str(text))
    return text

def readall():
    todo = []
    for i in sortList(os.listdir(subtitleImagePath)):
        print(os.listdir(subtitleImagePath))
        if os.path.isdir(subtitleImagePath+i):
            for k in sortList(os.listdir(subtitleImagePath+i)):
                todo.append(subtitleImagePath+i+'\\'+k)
                print('added '+subtitleImagePath+i+'\\'+k)
        else:
            todo.append(subtitleImagePath+i)
            print('added '+ subtitleImagePath+i)
    done = []
    for i in todo:
        done.append(read(i))
    return mergeSubtitle(done)
def readallMP():
    #pool.apply_async(readMP, args=(r"D:\python\KichikuHelper\SubtitleImages\example.mp4\20.jpg", q))
    #pool.close()
    #pool.join()
    todo = []
    for i in sortList(os.listdir(subtitleImagePath)):
        print(os.listdir(subtitleImagePath))
        if os.path.isdir(subtitleImagePath+i):
            for k in sortList(os.listdir(subtitleImagePath+i)):
                todo.append(subtitleImagePath+i+'\\'+k)
                print('added '+subtitleImagePath+i+'\\'+k)
        else:
            todo.append(subtitleImagePath+i)
            print('added '+ subtitleImagePath+i)
    print(todo)
    pool = mp.Pool(ProcessNumber)
    res = pool.map(readMP,todo)
    return mergeSubtitle(res)

def getSubtitles():
    subtitles = readallMP()
    savePath = path+'subtitles\\'
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    with open(savePath+'save.txt','w') as f:
        f.write(str(subtitles))
    return subtitles

if __name__ == "__main__":  
    #readall()
    start_time = time.time()
    subtitles = readallMP()
    print(subtitles)
    end_time = time.time()
    print('Time elapsed: '+str(end_time-start_time))
    savePath = path+'subtitles\\'
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    with open(savePath+'save.txt','w') as f:
        f.write(str(subtitles))