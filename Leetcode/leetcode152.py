# coding=utf-8

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    preMin = [0 for i in range(n)]
    preMax = [0 for i in range(n)]
    preMin[0] = nums[0]
    preMax[0] = nums[0]
    maxValue = preMax[0]

    for i in range(1,n):
        # 更新到当前位置的最大值
        preMax[i] = max(preMax[i-1]*nums[i], preMin[i-1]*nums[i], nums[i])
        preMin[i] = min(preMax[i - 1] * nums[i], preMin[i-1] * nums[i], nums[i])
        maxValue = max(maxValue, preMax[i])

    return maxValue
