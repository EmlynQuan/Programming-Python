# coding=utf-8

class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n, ans = len(nums), 0
        for i in range(n):
            ans ^= nums[i]

        # 找到了ans中某一位为1的数值 通过这一位去区分数组里的数
        div = 1
        while (div & ans) == 0:
            div <<= 1

        # 二次遍历
        a, b = 0, 0
        for i in range(n):
            if nums[i] & div:
                a ^= nums[i]
            else:
                b ^= nums[i]
        return a, b
