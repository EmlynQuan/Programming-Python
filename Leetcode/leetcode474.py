# coding=utf-8

class Solution(object):
    def getZerosOnes(self, s):
        n, z, o = len(s), 0, 0
        for i in range(n):
            if s[i] == '0':
                z += 1
            else:
                o += 1
        return z, o

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        length = len(strs)
        # 动态规划
        # 三维数组 dp[i][j][k] 表示在前i个字符串中，使用至多 j个1 和 k个0 可以包含字符串的最大数量
        dp = [[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(length+1)]

        # 最外层是字符串
        for i in range(1, length+1):
            # 1的个数
            for j in range(n+1):
                # 0的个数
                for k in range(m+1):
                    z, o = self.getZerosOnes(strs[i-1])
                    # 不能放当前字符串
                    if j < o or k < z:
                        dp[i][j][k] = dp[i-1][j][k]
                    # 可以放当前字符串
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-o][k-z]+1)

        return dp[length][n][m]
