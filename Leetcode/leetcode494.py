# coding = utf-8


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n, totalSum = len(nums), sum(nums)
        if abs(target) > abs(totalSum):
            return 0
        # dp[i][j]表示前i个元素中和为j-totalSum的表达式的数量
        dp = [[0 for _ in range(2 * totalSum + 1)] for _ in range(n)]
        dp[0][totalSum + nums[0]] = 1
        dp[0][totalSum - nums[0]] += 1

        for i in range(1, n):
            for j in range(-totalSum, totalSum + 1):
                if j - nums[i] >= -totalSum:
                    dp[i][totalSum + j] += dp[i - 1][totalSum + j - nums[i]]
                if j + nums[i] <= totalSum:
                    dp[i][totalSum + j] += dp[i - 1][totalSum + j + nums[i]]
        return dp[n - 1][totalSum + target]