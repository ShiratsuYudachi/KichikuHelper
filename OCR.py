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

def save(list):
    savePath = path+'subtitles\\'
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    with open(savePath+list[0][1]+'.txt','w') as f:
        f.write(str(list))
    
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

def readall():
    print('preparing to extract subtitles from '+str(os.listdir(subtitleImagePath)))
    for i in sortList(os.listdir(subtitleImagePath)):
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
    