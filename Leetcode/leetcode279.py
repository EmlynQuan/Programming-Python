# coding=utf-8

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 存储到指定大小n的所有平方和的可能
        dp = [float('inf') for _ in range(n+1)]

        dp[0] = 0
        for j in range(1, 101):
            if j**2 <= n:
                dp[j**2] = 1

        for i in range(n+1):
            for j in range(101):
                if i - j ** 2 >= 0 and j**2 <= n:
                    dp[i] = min(dp[i], dp[i-j**2]+1)
                else:
                    break
        return dp[n]

if __name__ == '__main__':
    n = 12
    print Solution().numSquares(n)
