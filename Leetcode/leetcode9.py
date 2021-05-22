# coding=utf-8

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        nums = []
        while x > 0:
            nums.append(x % 10)
            x = x // 10
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] != nums[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

