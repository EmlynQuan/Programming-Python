# coding=utf-8

def findRepeatNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tempArr = set()
    for i in range(len(nums)):
        tempArr.add(nums[i])
        if len(tempArr) < i+1:
            return nums[i]
    return -1


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print findRepeatNumber(nums)