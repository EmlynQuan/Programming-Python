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

def JZOffer3_findRepeatNumber(self, nums):
    # 实现 a[i] = i 的映射关系
    n = len(nums)
    # i 从 0 到 n-1
    i = 0
    while i < n:
        # 如果出现了前面的数 说明已经重复了
        if nums[i] < i:
            return nums[i]
        # 交换 pos = nums[i] 和 pos = i 的数字
        elif nums[i] > i:
            # 二者相等
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
        else:
            i += 1
    return i


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print findRepeatNumber(nums)