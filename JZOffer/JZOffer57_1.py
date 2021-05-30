# coding=utf-8

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return [nums[left], nums[right]]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1