# KichikuHelper
A small tool to help you catch material for Kichiku Videos

基于对字幕进行OCR，可从大量视频中批量导出含有某关键词的片段



使用方法：

将所有视频放入SourceVideos/目录(手动新建)

运行main.py，输入gensub，等待运行结束(对于使用1060 3G来说，平均10分钟可处理一个5分钟视频)

输入genvideo(或gen)，输入目标关键词

在outputs\目录下可找到所有与关键词匹配的视频片段
