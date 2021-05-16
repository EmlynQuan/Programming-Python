# coding=utf-8

def searchRange(nums, target):
    left, right = 0, len(nums)-1
    # 无元素
    if left > right:
        return [-1,-1]
    # 只有一个元素
    if left == right:
        if nums[left] == target:
            return [0,0]
        else:
            return [-1,-1]

    preflag, nextFlag = False, False
    # 大等于两个元素
    while left <= right:
        if nums[left] != target:
            left += 1
        else:
            preflag = True

        if nums[right] != target:
            right -= 1
        else:
            nextFlag = True

        if preflag and nextFlag:
            break

    if preflag or nextFlag:
        return [left, right]
    else:
        return [-1,-1]


if __name__ == "__main__":
    nums = [1,2,3]
    target = 2

    print searchRange(nums, target)