# coding=utf-8

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 前缀和
        n, sum, ans = len(nums), 0, 0
        if n == 1:
            return 0
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1

        prefixSum = {0: -1}
        for i in range(n):
            sum += nums[i]
            pre = prefixSum.setdefault(sum, i)
            if i - pre > ans:
                ans = i - pre
        return ans