# coding=utf-8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = [0 for _ in range(32)]
        # 统计在32位上的1的个数
        for i in range(len(nums)):
            for j in range(32):
                counter[j] += nums[i] & 1
                nums[i] >>= 1
        # 取模 3
        ans, m = 0, 3
        for j in range(32):
            ans <<= 1
            ans |= counter[31-j] % m
        return ans
