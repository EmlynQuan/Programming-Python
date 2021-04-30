# coding=utf-8

def calRabbitNum(arr):
    '''
    计算森林里有多少只兔子
    '''
    # 记录所有的数
    myDict = {}
    for i in range(len(arr)):
        if arr[i] in myDict.keys():
            myDict[arr[i]] += 1
        else:
            myDict[arr[i]] = 1

    sum = 0
    # 遍历字典
    for key in myDict.keys():
        counter = myDict[key] // (key+1)
        if myDict[key] % (key+1) != 0:
            counter += 1
        sum += counter * (key+1)

    return sum
