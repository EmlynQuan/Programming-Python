# coding=utf-8

def cuttingRope_dp(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 3:
        return n-1
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(3, n+1):
        for j in range(1, i/2+1):
            dp[i] = max(dp[i], j*max(dp[i-j], i-j))

    return dp[n] % 1000000007


