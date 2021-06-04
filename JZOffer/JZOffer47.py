# coding=utf-8

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = grid[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]




# if __name__ == "__main__":