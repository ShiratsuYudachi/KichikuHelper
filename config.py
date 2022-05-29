#config

#extrat one frame per $frameFrequency frames, higher value will decrease the time needed for OCR and the accuracy of time
#每x帧提取一帧，增加将节省OCR的时间但会降低时间精度
frameFrequency = 10
#Max Process used to OCR, higher value will shorten the time needed for OCR but YOU NEED PAY ATTTENTION TO YOUR HARDWARE
#for reference, in my 3600x/16g@DDR4/GTX1060@3g PC, 6 Process have the best efficiency(with no extra Bakcground Process, except those from windows).
#Else it will reach the bottleneck of Memory(both GPU Mem and Mem), while ultilizing 70% of CPU and 20% of GPU
#最大OCR进程数，增加可节省OCR时间但请注意阁下的硬件性能
#参考：在3600x/16g@DDR4/GTX1060@3g的pc中，6进程可以达到最高效率(无后台)
#过多将降低效率，上述条件中超过会遇到显存与内存瓶颈，于6进程时占用70%CPU与20%GPU
ProcessNumber = 3
#whether not to turn the SutitleImage to Black and Whie, generally you dont need to touch it 
#是否不将字幕图片转为黑白，一般不需要动这个
cropOnly = False
#0~255, threshold used when turnning image to Black and White. 
#if the colour of subtitle in your video is not pure white, try to decrease it 
#0~255, 用于黑白化图片的阈值
#如果视频中的字幕并非纯白，请尝试降低
thresh = 250