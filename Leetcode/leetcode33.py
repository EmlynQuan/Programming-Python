# coding=utf-8

def search(nums, target):
    return binarySearch(nums, target, 0, len(nums))

def binarySearch(nums, target, left, right):
    # 二分查找
    if left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        leftR = binarySearch(nums, target, left, mid)
        if leftR >= 0:
            return leftR
        else:
            rightR = binarySearch(nums, target, mid+1, right)
            if rightR >= 0:
                return rightR
            else:
                return -1

    return -1

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print search(nums, target)