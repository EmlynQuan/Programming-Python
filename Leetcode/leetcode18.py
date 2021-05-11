# coding=utf-8

def fourSum(nums, target):
    n = len(nums)
    if n < 4:
        return []

    nums.sort()
    ret = []
    for i in range(n):
        for j in range(i+1, n):
            left = j+1
            right = n-1
            while left < right:
                temp = nums[i] + nums[j] + nums[left] + nums[right]
                if temp == target:
                    temp = [nums[i], nums[j], nums[left], nums[right]]
                    if temp not in ret:
                        ret.append(temp)
                    left += 1
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    right -= 1

    return ret



if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print fourSum(nums, target)