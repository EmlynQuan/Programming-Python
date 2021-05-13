# coding=utf-8

class Solution(object):
    def findSquare(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #DP实现

        #边界判断--空矩阵
        if not matrix:
            return []

        row = len(matrix)
        col = len(matrix[0])

        #边界处理
        dp = [[[0,0] for _ in range(col+1)]for _ in range(row+1)]
        #dp数组赋值
        for i in range(1, row+1):
            for j in range(1, col+1):
                #是黑色
                if matrix[i-1][j-1] == 0:
                    dp[i][j][0] = dp[i-1][j][0]+1
                    dp[i][j][1] = dp[i][j-1][1]+1

        r,c,size = -1,-1,0
        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == 0:
                    #取最小才能保证是方阵
                    cur_size = min(dp[i][j])
                    while cur_size > size:
                        #判断另外两条边能不能满足cur_size的长度限制
                        if dp[i-cur_size+1][j][1] >= cur_size and dp[i][j-cur_size+1][0] >= cur_size:
                            r = i - cur_size
                            c = j - cur_size
                            size = cur_size
                            break
                        cur_size-=1

        if size == 0:
            return []

        return [r,c,size]


