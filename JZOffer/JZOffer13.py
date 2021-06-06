# coding=utf-8

class Solution(object):
    def digitsum(self, n):
        ans = 0
        while n:
            ans += n % 10
            n //= 10
        return ans

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        ans, x, y = 0, 0, 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # m 行 n 列
        for i in range(m):
            y = 0
            for j in range(n):
                if x + y <= k:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                        ans += 1
                    elif (i-1 >= 0 and dp[i-1][j]) or (j-1 >= 0 and dp[i][j-1]):
                        dp[i][j] = 1
                        ans += 1
                if j % 10 == 9:
                    y -= 8
                else:
                    y += 1

            if i % 10 == 9:
                x -= 8
            else:
                x += 1
        return ans