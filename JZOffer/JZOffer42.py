# coding=utf-8

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [0 for i in range(len(nums)+1)]
    maxValue = float('-inf')
    for i in range(len(nums)):
        dp[i+1] = max(dp[i]+nums[i], nums[i])
        maxValue = max(maxValue, dp[i+1])
    return maxValue
