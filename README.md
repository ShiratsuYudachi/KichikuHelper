###I hope this project can help me pass the waiver for COMP2011

# KichikuHelper
A small tool to help you catch material for Kichiku Videos

It can generate all video excerpts that containing specified keyword in subtitle from a large amount of videos.

基于对字幕进行OCR，可从大量视频中批量导出字幕含有某关键词的片段



使用方法：

新建SourceVideos/目录，将所有源视频放入

运行main.py，输入gensub，等待运行结束(对于使用1060 3G来说，平均10分钟可处理一个5分钟视频)

输入genvideo(或gen)，输入目标关键词

在outputs\目录下可找到所有与关键词匹配的视频片段
