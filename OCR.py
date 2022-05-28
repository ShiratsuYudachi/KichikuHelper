from utilities import sortList
import easyocr
import os
path = path = os.path.dirname(__file__)+'\\'
subtitleImagePath = path+'SubtitleImages\\'
def read(imagePath):
    reader = easyocr.Reader(['ch_sim','en'])
    result = reader.readtext(imagePath, detail=0)
    print('，'.join(result))

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

if __name__ == "__main__":  
    readall()