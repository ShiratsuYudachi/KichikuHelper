#config

#extrat one frame per $frameFrequency frames, higher value save OCR time but down the accuracy of time
#每x帧提取一帧，增加将节省OCR的时间但会降低时间精度
frameFrequency = 10
#Max Process used to OCR, higher value will shorten the time needed for OCR but YOU NEED PAY ATTTENTION TO YOUR HARDWARE
#最大OCR进程数，增加可节省OCR时间但请注意阁下的硬件性能
ProcessNumber = 2
#whether not to turn the SutitleImage to Black and Whie, generally you dont need to touch it 
#是否不将字幕图片转为黑白，一般不需要动这个
cropOnly = False
#0~255, threshold used when turnning image to Black and White. 
#if the colour of subtitle in your video is not pure white, try to decrease it 
#0~255, 用于黑白化图片的阈值
#如果视频中的字幕并非纯白，请尝试降低
thresh = 240
#0~1, threshold used when merging two subtitles(because of the inaccuracy of OCR)
#0~1, 用于决定是否合并两个字幕的阈值(因为OCR的不准确性)
similarity_threshold = 0.7