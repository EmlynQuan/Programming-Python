# coding=utf-8
import collections
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 哈希表统计
    # 将数组 nums 排序，数组中点的元素 一定为半数以上的数
    # 摩尔投票法 
    n = len(nums)
    myDict = collections.Counter(nums)
    for key in myDict.keys():
        if myDict[key] > n // 2:
            return key