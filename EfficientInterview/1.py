# coding=utf-8

def twoSum(nums, target):
    myDict = {}
    for idx, num in enumerate(nums):
        temp = target - num
        if myDict.get(temp) is not None:
            return [idx, myDict.get(temp)]
        myDict[num] = idx
    return [-1,-1]