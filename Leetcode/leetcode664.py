# coding=utf-8

def strangePrinter(s):
    # 动态规划
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # 初始化 每个字符需要打印的次数是1次
    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i][j-1]
            else:
                minValue = float('inf')
                for k in range(i, j):
                    minValue = min(minValue, dp[i][k]+dp[k+1][j])
                dp[i][j] = minValue

    return dp[0][n-1]


if __name__ == "__main__":
    s = "aba"
    strangePrinter(s)