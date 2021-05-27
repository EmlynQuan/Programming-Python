# coding=utf-8

def exchange(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left, right = 0, len(nums)-1
    while left < right:
        # 是奇数
        while left < right and nums[left] % 2 == 1:
            left += 1
        # 是偶数
        while left < right and nums[right] % 2 == 0:
            right -= 1
        if left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
    return nums

