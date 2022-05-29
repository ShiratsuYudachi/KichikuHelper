from requests import get
from getFrames import getFrames
from ProcessFrames import generateAllSubtitleImage
from OCR import readall
import time

if __name__ == '__main__':
    start = time.time()
    #getFrames()
    #generateAllSubtitleImage()
    readall()
    end = time.time()
    print('Time elapsed: '+str(end-start))
