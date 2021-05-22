# coding=utf-8

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    preMax = [0 for _ in range(n)]
    preMax[0] = nums[0]
    maxValue = preMax[0]

    for i in range(1, n):
        if preMax[i-1] > 0:
            preMax[i] = preMax[i-1] + nums[i]
        else:
            preMax[i] = nums[i]

        maxValue = max(maxValue, preMax[i])

    return maxValue

