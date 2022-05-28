from multiprocessing.dummy import Process
from utilities import sortList
import easyocr
import os
import multiprocessing as mp
import time
ProcessNo = 6
path = path = os.path.dirname(__file__)+'\\'
subtitleImagePath = path+'SubtitleImages\\'
def read(imagePath):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    rawText = '，'.join(result)
    text = [rawText,imagePath.split("\\")[-2],imagePath.split("\\")[-1].strip('.jpg')]#format:[text, video, frame]
    print("extracted "+str(text))
    return text

def readMP(imagePath):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    rawText = '，'.join(result)
    text = [rawText,imagePath.split("\\")[-2],imagePath.split("\\")[-1].strip('.jpg')]
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
    return done
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
    q = mp.Queue()
    pool = mp.Pool(ProcessNo)
    res = pool.map(readMP,todo)
    return res
if __name__ == "__main__":  
    #readall()
    start_time = time.time()
    print(readall())
    end_time = time.time()
    print('Time elapsed: '+str(end_time-start_time))