# coding=utf-8

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


