# coding=utf-8

def fib(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print dp
    return dp[n]

if __name__ == "__main__":
    fib(5)