# coding=utf-8

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 存储当前值对应的硬币组合数
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]



if __name__ == '__main__':
    Solution().change(amount=4, coins=[1,2])

