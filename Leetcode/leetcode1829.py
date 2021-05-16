# coding=utf-8

def getMaximumXor(nums, maximumBit):
    n = len(nums)
    maxValue = 2**maximumBit - 1
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = dp[i-1] ^ nums[i]

    answer = []
    for i in range(n-1, -1, -1):
        k = dp[i] ^ maxValue
        answer.append(k)

    return answer


def getMaximumXor_bit(self, nums, maximumBit):
    """
    :type nums: List[int]
    :type maximumBit: int
    :rtype: List[int]
    """
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = dp[i - 1] ^ nums[i]

    answer = []
    for i in range(n - 1, -1, -1):
        temp = [1 for _ in range(maximumBit)]
        curValue = [0 for _ in range(maximumBit)]
        pos = 0
        while dp[i] > 0:
            curValue[pos] = dp[i] % 2
            dp[i] //= 2
            pos += 1

        k = 0
        for t in range(maximumBit):
            temp[t] = temp[t] ^ curValue[t]
            if temp[t] == 1:
                k += 2 ** t

        answer.append(k)

    return answer

