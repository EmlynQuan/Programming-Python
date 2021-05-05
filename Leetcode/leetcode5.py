# coding=utf-8

def longestPalindrome(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    maxLen = 0
    begin = -1
    # 子串的长度
    for length in range(1, n+1):
        # 子串的起始位置
        for i in range(0, n-length+1):
            j = i + length - 1
            # 如果两端的不相等 就不做处理 因为初始化已经为0
            # 如果相等
            # print s[i:j+1]
            if s[i] == s[j]:
                # 是同一个字母 或者是相邻两个
                if j-i < 2:
                    dp[i][j] = 1
                    if length > maxLen:
                        begin = i
                        maxLen = length

                # 子串是回文串 子串不是回文串不需要更新
                elif dp[i+1][j-1] != 0:
                    dp[i][j] = 1

                    if length > maxLen:
                        begin = i
                        maxLen = length

    return s[begin:begin+maxLen]

if __name__ == "__main__":
    print longestPalindrome("cbbd")