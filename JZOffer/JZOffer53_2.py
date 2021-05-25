# coding=utf-8

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    left, right = 0, n-1
    if nums[right] == right:
        return right+1
    while left < right:
        mid = (left+right) // 2
        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid

    return nums[right]-1

if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    missingNumber(nums)