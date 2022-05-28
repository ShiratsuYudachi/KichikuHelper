from utilities import sortList
import easyocr
import os
import multiprocessing as mp
path = path = os.path.dirname(__file__)+'\\'
subtitleImagePath = path+'SubtitleImages\\'
def read(imagePath):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    rawText = '，'.join(result)
    text = [rawText,imagePath.split("\\")[-2],imagePath.split("\\")[-1].strip('.jpg')]
    print(text)

def readMP(imagePath,q):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    rawText = '，'.join(result)
    text = [rawText,imagePath.split("\\")[-2],imagePath.split("\\")[-1].strip('.jpg')]
    print(text)
    q.put(1)

def readall():
    for i in sortList(os.listdir(subtitleImagePath)):
        print(os.listdir(subtitleImagePath))
        if os.path.isdir(subtitleImagePath+i):
            for k in sortList(os.listdir(subtitleImagePath+i)):
                read(subtitleImagePath+i+'\\'+k)
                print('processed '+subtitleImagePath+i+'\\'+k)
        else:
            read(subtitleImagePath+i)
            print('processed '+ subtitleImagePath+i)

def readallMP():
    pass

if __name__ == "__main__":  
    readall()