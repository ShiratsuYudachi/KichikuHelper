#config

#extrat one frame per $frameFrequency frames, higher value save OCR time but down the accuracy of time
#每x帧提取一帧，增加将节省OCR的时间但会降低时间精度
frameFrequency = 20
#Max Process used to OCR, higher value will shorten the time needed for OCR but YOU NEED PAY ATTTENTION TO YOUR HARDWARE
#最大OCR进程数，增加可节省OCR时间但请注意阁下的硬件性能
ProcessNumber = 1
#whether not to turn the SutitleImage to Black and Whie, generally you dont need to touch it 
#是否不将字幕图片转为黑白，一般不需要动这个
cropOnly = False
#0~255, threshold used when turnning image to Black and White. 
#if the colour of subtitle in your video is not pure white, try to decrease it(but most likely it wont normaly work)
#0~255, 用于黑白化图片的阈值
#如果视频中的字幕并非纯白，请尝试降低(不过尚未对非纯白字幕进行优化，大概率无法正常识别)
thresh = 250
#0~1, threshold used when merging two subtitles(because of the inaccuracy of OCR)
#0~1, 用于决定是否合并两个字幕的阈值(因为OCR的不准确性)
similarity_threshold = 0.4
#set it to True if the name of source video contain non-ascii characters
#it will rename them to 1,2,3,4,...
#是否开启强制重命名视频
#开启后所有视频会被重命名为1,2,3,4,...，如果你的片源包含中文等ASCII字符而不想批量修改，请将本选项改为True
force_rename = False