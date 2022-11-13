from getFrames import getFrames
from ProcessFrames import generateAllSubtitleImage
from OCR import readall
from OCR import getSubtitlesOf
from videoEdit import subclip
import time
import os

path = os.path.abspath(os.path.dirname(__file__))+'\\'

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
            while True:
                SubclipList = []
                keyword = input('Keyword=')
                norepeat = False
                if '-norepeat' in keyword.split(' '):#1 clip per video
                    norepeat = True
                keyword = keyword.split(' ')[0]
                entriesNum = 0
                for video in os.listdir(path+'subtitles\\'):
                    subtitles = getSubtitlesOf(video)
                    TGTList = []
                    for i in subtitles:
                        if keyword in i[0]:
                            if norepeat:
                                if len(TGTList) == 0:
                                    TGTList.append(i)
                                    entriesNum+=1
                            else:
                                TGTList.append(i)
                                entriesNum+=1

                    if len(TGTList)>0:
                        SubclipList.append(TGTList)
                cmd = input('Founded {0} entries matching {1} in {2} videos, continue to subclip video?(y/n), s for show all result.\n'.format(str(entriesNum),keyword,len(SubclipList))) #r for research
                
                if cmd=='s':
                    for i in SubclipList:
                        print(i)
                else:
                    if cmd:
                        for k in SubclipList:
                            for i in k:
                                subclip(i[1],i[2],i[3],keyword)
                        break

        elif cmd == 'genframe':
            getFrames()
        elif cmd == 'gensubimg':
            generateAllSubtitleImage()
        elif cmd == 'readsub':
            readall()
                


