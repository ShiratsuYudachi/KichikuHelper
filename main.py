from getFrames import getFrames
from ProcessFrames import generateAllSubtitleImage
from OCR import readall
from OCR import getSubtitlesOf
from videoEdit import subclip
import time
import os

path = os.path.dirname(__file__)+'\\'


if __name__ == '__main__':
    while True:
        cmd = input('Hi!\n')
        if cmd == 'gensubtitles' or cmd == 'gensub':
            start = time.time()
            getFrames()
            generateAllSubtitleImage()
            readall()
            end = time.time()
            print('Time elapsed: '+str(end-start))
        elif cmd == 'genvideo' or cmd == 'gen':
            keyword = input('Keyword=')
            for video in os.listdir(path+'subtitles\\'):
                subtitles = getSubtitlesOf(video)
                TGTList = []
                for i in subtitles:
                    if keyword in i[0]:
                        TGTList.append(i)
                #TODO: give the list, y/n?
                for i in TGTList:
                    subclip(i[1],i[2],i[3],keyword)
        elif cmd == 'genframe':
            getFrames()
        elif cmd == 'gensubimg':
            generateAllSubtitleImage()
        elif cmd == 'readsub':
            readall()
                


