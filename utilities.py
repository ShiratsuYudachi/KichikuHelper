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