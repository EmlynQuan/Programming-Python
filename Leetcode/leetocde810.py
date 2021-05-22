# coding-utf-8

def xorGame(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n % 2 == 0:
        return True
    else:
        xorSum = 0
        for i in range(n):
            xorSum ^= nums[i]
        if xorSum == 0:
            return True
    return False