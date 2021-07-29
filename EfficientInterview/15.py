# coding=utf-8

def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 存储结果
    ret = []
    n = len(nums)
    if n < 3:
        return ret
    # 首先对数组进行排序
    nums.sort()
    # 如果第一个元素都大于0
    if nums[0] > 0:
        return ret

    for one in range(0, n - 2):
        if one > 0 and nums[one] == nums[one - 1]:
            continue
        three = n - 1
        for two in range(one + 1, n - 1):
            if two > one + 1 and nums[two] == nums[two - 1]:
                continue
            while two < three and nums[one] + nums[two] + nums[three] > 0:
                three -= 1
            if two >= three:
                break
            if nums[one] + nums[two] + nums[three] == 0:
                ret.append([nums[one], nums[two], nums[three]])
    return ret