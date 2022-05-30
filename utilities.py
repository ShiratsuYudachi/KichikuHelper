from config import similarity_threshold

def getNo(fileName):
    if isinstance(fileName,str):
        return int(fileName.split('.')[0])
    else:
        return fileName

def sortList(list):
    for k in range(1,len(list)):
        for i in range(len(list)-k):
            if getNo(list[i])>getNo(list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
    return list

def MergeMKII(list):
    mergeReady = []
    isScanning = True
    i=0
    while i<len(list)-1:
        list1 = list[i][0]
        list2 = list[i+1][0]
        similarity = len(set(list1) & set(list2))/(0.5*(len(set(list1))+len(set(list2))))#相同字符数/平均字符数(不计算重复字符)
        if isScanning:
            if similarity > similarity_threshold:
                isScanning = False
                startPos = i
                mergeReady.append(list[i])
        else:
            if similarity > similarity_threshold:
                mergeReady.append(list[i])
            else:#start merging
                mergeReady.append(list[i])
                start = list[startPos][2]
                newEnd = list[startPos+len(mergeReady)-1][3]
                newEnd = newEnd if newEnd else list[startPos+len(mergeReady)-1][2]
                isScanning = True
                charaFreq = count_frequency(mergeReady)
                winner = filter(mergeReady,charaFreq)
                winner[2],winner[3] = start,newEnd
                list[startPos] = winner
                for i in range(len(mergeReady)-1):
                    del list[startPos+1]
                i = startPos
                del startPos
                del mergeReady
                mergeReady = []
        i+=1
    return list

def count_frequency(list):
    chara_set = set()
    chara_frequency = {}
    for i in list:
        chara_set = chara_set|set(i[0])#get the union of all characters in sentences
    for chara in chara_set:
        chara_frequency[chara] = 0
        for k in range(len(list)):#count_frequency
            if chara in list[k][0]:
                chara_frequency[chara]+=1
    return chara_frequency

def filter(list,charaFreq):#通过某字在所有句子中出现的次数为该字加权，之后以该权重为所有句子评分，取分最高者
    scoreList = []
    for i in range(len(list)):
        scoreList.append(0)
        for chara in list[i][0]:
            if chara in charaFreq:
                scoreList[i] += charaFreq[chara]
    return list[scoreList.index(max(scoreList))]