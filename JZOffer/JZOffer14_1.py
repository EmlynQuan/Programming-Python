# coding=utf-8

def cuttingRope_1(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 3:
        return n-1
    x = n % 3
    a = n // 3
    if x == 0:
        return 3**a
    elif x == 1:
        return 3**(a-1) * 4
    elif x == 2:
        return 3**a * 2

def cuttingRope(n):
    if n <= 3:
        return n-1
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(3, n+1):
        for j in range(1, i/2+1):
            dp[i] = max(dp[i], j*max(dp[i-j], i-j))

    return dp[n]

