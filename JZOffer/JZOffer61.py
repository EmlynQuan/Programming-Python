# coding=utf-8

def isStraight1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    counter = 0
    i = 0
    while nums[i] == 0 and i < 5:
        counter += 1
        i += 1

    if counter >= 4:
        return True

    start = nums[i]
    i += 1
    while i < 5:
        gap = nums[i] - start
        if gap == 0:
            return False
        elif gap == 1:
            start = nums[i]
            i += 1
        elif gap-1 > counter:
            return False
        else:
            counter -= gap-1
            start = nums[i]
            i += 1
    return True


def isStraight(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    counter = 0
    i = 0
    while i < 5:
        if nums[i] == 0:
            counter += 1
        elif i >= 1 and nums[i] == nums[i-1]:
            return False
        i += 1
    if counter >= 4:
        return True
    if nums[-1] - nums[counter] > 4:
        return False
    return True


if __name__ == "__main__":
    isStraight ([0,0,1,2,5])