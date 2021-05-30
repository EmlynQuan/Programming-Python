# coding=utf-8

def findContinuousSequence1(target):
    """
    :type target: int
    :rtype: List[List[int]]
    """
    nums = range(1,target)
    ret = []
    for i in range(1,target):
        arr = []
        sum = 0
        for j in range(i, target):
            if sum == target:
                ret.append(arr)
                break
            arr.append(nums[j])
            sum += nums[j]
            if sum > target:
                break

    return ret

def findContinuousSequence(target):
    """
    :type target: int
    :rtype: List[List[int]]
    """
    ret = []
    i, j = 1, 2
    while i < target and j < target:
        sum = (j + i) * (j - i + 1)
        if sum == 2 * target:
            ret.append([x for x in range(i, j+1)])
        if sum < 2 * target:
            j += 1
        else:
            i += 1
            j = i + 1


    return ret
