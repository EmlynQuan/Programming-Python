# coding=utf-8

def waysToStep(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,n+1):
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000007

    return dp[n]
