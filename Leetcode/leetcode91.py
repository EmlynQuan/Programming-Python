# coding=utf-8
# leetocde 91. 解码方法 动态规划
def decoder_dp(s):
    n = len(s)
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    # 遍历每个字符
    for i in range(1, n + 1):
        # 如果当前字符可以单独解码
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        # 如果当前字符可以和前一个一起解码
        if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[n]


# leetcode LCP 12. 小张刷题计划
def minTime(time, m):
    # 每天都可以请小杨帮忙
    if len(time) < m:
        return 0
    # 二分查找 + 贪心
    # else:


if __name__ == "__main__":
    print decoder_dp('226')