# coding=utf-8

def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 9:
        return n
    dp = [0 for _ in range(10)]
    dp[1] = 10
    # 获得是m+1位数字
    m = 0
    for i in range(2, 10):
        dp[i] = dp[i - 1] + i * (10 ** i - 10 ** (i - 1))
        if n + 1 <= dp[i]:
            m = i - 1
            break

    x = (n - dp[m]) // (m + 1)
    i = (n - dp[m]) % (m + 1)
    ans = str(10 ** (m) + x)
    # print n,dp[m],ans,x,i
    return int(ans[i])


if __name__ == "__main__":
    findNthDigit(2)
