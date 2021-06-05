# coding=utf-8

class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp = [0.0 for _ in range(6*n+1)]
        dp[0] = 1
        self.dfs(dp, 1, n)
        print dp[n:-1]
        return dp[n:-1]

    def dfs(self, dp, curN, n):
        if curN == n+1:
            return
        else:
            self.dfs(dp, curN+1, n)
            temp = [dp[i] for i in range(curN-1, 6*(curN-1)+1)]
            for i in range(curN, 6*curN+1):
                dp[i] = 0

            # 遍历6个可能性
            for i in range(1,7):
                # 遍历之前存在的可能取之的概率
                for j in range(curN-1, 6*(curN-1)+1):
                    dp[j+i] += temp[j]*1.0/6


if __name__ == '__main__':
    Solution().dicesProbability(2)