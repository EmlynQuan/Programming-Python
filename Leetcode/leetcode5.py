# coding=utf-8

def longestPalindrome(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n-1, 0, -1):
        for j in range(i, -1, -1):
            if i == j:
                dp[i][j] = 1
            else:
                if dp[i][j] != 0 and j+1 < n and i-1 >= 0 and s[i-1] == s[j+1]:
                    dp[i][j] = dp[][]