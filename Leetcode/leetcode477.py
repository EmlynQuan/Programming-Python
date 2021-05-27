# coding=utf-8

def totalHammingDistance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    bitNum = 30
    ans, n = 0, len(nums)
    for i in range(bitNum):
        temp = [(val >> i) & 1 for val in nums]
        c = sum(temp)
        ans += c * (n-c)
    return ans