# coding=utf-8

def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n, pre, counter = len(nums), 0, 0
    myDict = {}
    for i in range(n):
        pre += nums[i]
        if pre == k:
            counter += 1
        if pre - k in myDict.keys():
            counter += myDict[pre - k]
        myDict[pre] = myDict.get(pre, 0) + 1

    return counter