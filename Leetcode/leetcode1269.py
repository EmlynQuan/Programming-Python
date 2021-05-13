# coding=utf-8

def numWays(steps, arrLen):
    posNum = min(arrLen, steps+1)
    dp = [[0 for _ in range(posNum)] for _ in range(steps+1)]
    dp[0][0] = 1

    # 步数
    for i in range(1, steps+1):
        # 位置
        for j in range(posNum):
            # 原地保持不懂的方案
            dp[i][j] = dp[i-1][j]
            # 向右移动得到的方案
            if j >= 1:
                dp[i][j] += dp[i-1][j-1]
            # 向左移动得到的方案
            if j < posNum-1:
                dp[i][j] += dp[i-1][j+1]
                
        dp[i][j] %= 10 ** 9 + 7

    return dp[steps][0]