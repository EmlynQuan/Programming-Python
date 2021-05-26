# coding=utf-8

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right, counter = 0, len(nums) - 1, 0
    if right == -1:
        return 0
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[left] == target:
            counter += 1
            left += 1
        elif nums[right] == target:
            counter += 1
            right -= 1
        else:
            left += 1
            right -= 1

    if nums[right] == target:
        counter += 1
    return counter