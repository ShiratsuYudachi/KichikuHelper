from copyreg import pickle
from multiprocessing.dummy import Process
from utilities import sortList
from utilities import MergeMKII
import easyocr
import os
import multiprocessing as mp
import time
import json
from config import ProcessNumber


path = path = os.path.dirname(__file__)+'\\'
savePath = path+'subtitles\\'
subtitleImagePath = path+'SubtitleImages\\'
symbols = ['-','_', '=', '！', '!', '@', '#', '￥', '%', '…','&','*','(',')','~',':','"','{',"'",'}','[',']','|','\\','?','/','<','>',',','.',';','+']

def save(list):
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    with open(savePath+list[0][1]+'.json','w') as f:
        f.write(json.dumps(list, indent=4))

def getSubtitlesOf(videoName):
    with open (savePath+videoName) as f:
        return json.loads(f.read())

def mergeSubtitle(list):
    for i in list:
        i[0] = i[0].replace('，','  ')
        for k in symbols:
            i[0] = i[0].replace(k,'')
    i = 0
    while i<len(list)-1:
        if list[i][0] == list[i+1][0]:
            list[i][3] = list[i+1][2]
            del list[i+1]
        else:
            i+=1
    return MergeMKII(list)
            
def read(imagePath):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    rawText = '，'.join(result)
    text = [rawText,imagePath.split("\\")[-2],int(imagePath.split("\\")[-1].strip('.jpg')),None]#format:[text, video, frame]
    print("extracted "+str(text))
    return text

def readall():
    print('preparing to extract subtitles from '+str(os.listdir(subtitleImagePath)))
    for i in os.listdir(subtitleImagePath):
        todo = []
        for k in sortList(os.listdir(subtitleImagePath+i)):
            todo.append(subtitleImagePath+i+'\\'+k)
            print('added '+subtitleImagePath+i+'\\'+k)
        print('ready to extract '+str(todo))
        pool = mp.Pool(ProcessNumber)
        result = mergeSubtitle(pool.map(read,todo))
        print(result)
        save(result)

if __name__ == "__main__":
    start_time = time.time()
    readall()
    end_time = time.time()
    print('Time elapsed: '+str(end_time-start_time))
    