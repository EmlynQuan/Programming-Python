# coding=utf-8

def checkSubarraySum1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # 前缀和 无法
    n = len(nums)
    prefixSum = [0 for _ in range(n+1)]
    prefixSum[1] = nums[0] % k
    for i in range(1, n+1):
        prefixSum[i] = (prefixSum[i-1] + nums[i-1]) % k

    for i in range(2, n+1):
        for j in range(i-1):
            if prefixSum[i] == prefixSum[j]:
                return True
    return False


def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # 同余
    if len(nums) < 2:
        return False
    sum = 0
    n = len(nums)
    prefixSum = {0: -1}
    for i in range(n):
        sum += nums[i]
        sum %= k
        pre = prefixSum.setdefault(sum, i)
        if i - pre > 1:
            return True
    return False