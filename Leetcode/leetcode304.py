# coding=utf-8

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0:
            return
        n, m = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]
        return


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = self.dp[row2+1][col2+1]+self.dp[row1][col1]-self.dp[row1][col2+1] - self.dp[row2+1][col1]
        return ret

